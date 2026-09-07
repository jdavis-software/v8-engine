# Mechanical model and deterministic simulation contract

## 1. Scope and conventions

This is a derived educational 90-degree cross-plane V8 configuration, not recovered source code and not an OEM specification. It defines a coherent rigid slider-crank mechanism under the stated assumptions. It does not model combustion dynamics, bearing forces, flex, friction, valve float, or manufacturing tolerances.

Use SI units internally: meters, seconds, radians, pascals, and cubic meters. External/UI angles may be degrees, but convert only at explicit boundaries. Define `mod(x,n) = ((x % n) + n) % n`; JavaScript remainder is not a positive modulo operation for negative inputs.

### Default dimensions

| Parameter | Symbol | Default |
| --- | --- | ---: |
| Bore | B | 0.100 m |
| Stroke | S | 0.090 m |
| Crank radius | r = S/2 | 0.045 m |
| Connecting rod center length | l | 0.150 m |
| Compression ratio | CR | 10 |
| Cylinder count | N | 8 |
| Nominal axial cylinder/journal pitch | d | 0.112 m |
| Bank angle | total | 90 degrees |
| Idealized maximum valve lift | h | 0.010 m |

Dimensions are chosen for this educational model. Axial rod width, bearing clearance, piston compression height, block thickness, and valve geometry must be derived consistently during packaging; do not pretend these defaults describe a manufacturable engine.

Swept volume per cylinder is `Vd = pi * B^2 / 4 * S = 0.0007068583470577036 m^3`, about 706.858 cc. Total displacement is about 5.654867 L. Clearance volume is `Vc = Vd / (CR - 1)`, about 78.540 cc. These are calculated design values, not measurements of the reference.

## 2. World coordinate system and numbering

The crankshaft axis is +Z, with journal stations increasing from front to rear. +Y is upward. +X points toward Bank B. Describe sides as Bank A and Bank B, not driver/passenger or viewer-left/right.

Bank angle beta is measured from +Y toward +X in the XY plane. Bank A uses beta = -45 degrees and cylinders 1,3,5,7. Bank B uses beta = +45 degrees and cylinders 2,4,6,8. The outward cylinder axis is:

```text
u(beta) = (sin(beta), cos(beta), 0)
```

Cylinder bores are offset along Z to accommodate the two side-by-side rods on each shared journal. For each rod, its crankpin attachment and wrist pin use the same axial coordinate `z_j + delta_bank`. Set rod widths and the two bank offsets together so the rods occupy separate center planes within the common journal. Do not use one z plane for a crank attachment and a different one for that rod's wrist pin; that would invalidate the planar rod-length calculation.

## 3. Shared crankshaft geometry and firing table

Let Theta be the increasing global crank phase in degrees. Journal angle, measured from +Y toward +X, is:

```text
alpha_j(Theta) = alpha0_j - Theta
p_j.xy = (r * sin(alpha_j), r * cos(alpha_j))
```

Trigonometric functions receive radians. The minus sign belongs to this particular alpha-angle convention. It is NOT an instruction to apply a negative Three.js Euler Z rotation. Use the explicit conversion below so the mesh and solver agree.

### Solver-to-render rotation conversion

Standard right-handed rotation about +Z obeys:

```text
Rz(t) * (sin(a), cos(a)) = (sin(a-t), cos(a-t))
```

Therefore, when the crank geometry is authored at its angle-zero journal positions `(r*sin(alpha0), r*cos(alpha0), z)`, the correct parent mesh Euler rotation is:

```ts
crankGroup.rotation.z = degreesToRadians(Theta);       // POSITIVE
camGroup.rotation.z = degreesToRadians(Theta / 2);     // POSITIVE
```

The corresponding journal alpha decreases by Theta, and each cam lobe's alpha decreases by Theta/2. These are the same physical rotations expressed in different angular conventions. A bank component authored along local +Y uses `rotation.z = -beta` to point along u(beta). Alternatively, orient it by a tested quaternion from its authored axis to u.

Bake static journal/lobe offsets once or apply them as static local transforms, not both. Do not give rods the crank rotation as an inherited transform and also apply a world-space solved rod pose. Add a test that applies the actual render rotation matrix to authored journal centers and compares the resulting world points with the solver. This conversion was separately numerically checked during planning; it must still be reproduced in implementation tests.

Front-to-rear journal starting angles are `[-45, -135, +45, +135]` degrees. Four different quadrature orientations make this a cross-plane configuration. Each journal is shared by one cylinder from each bank.

| Cylinder | Bank / beta | Shared journal | alpha0 | Firing Theta modulo 720 |
| --- | --- | --- | ---: | ---: |
| 1 | A / -45 | J0 | -45 | 0 |
| 2 | B / +45 | J0 | -45 | 630 |
| 3 | A / -45 | J1 | -135 | 270 |
| 4 | B / +45 | J1 | -135 | 180 |
| 5 | A / -45 | J2 | +45 | 450 |
| 6 | B / +45 | J2 | +45 | 360 |
| 7 | A / -45 | J3 | +135 | 540 |
| 8 | B / +45 | J3 | +135 | 90 |

Firing order is `1, 8, 4, 3, 6, 5, 7, 2`, at global phases `0,90,180,270,360,450,540,630`. This is our selected convention; do not attach a specific engine manufacturer's label to it.

For every row, `mod(alpha0_j - F_i - beta_i, 360) = 0`. Therefore its crankpin is aligned with its outward bore axis at the stated firing top-dead-center. The other top-dead-center, 360 crank degrees later, is the exhaust/intake transition, not another firing event. This relationship is a required invariant, not merely a labeling preference.

## 4. Slider-crank equations and rod pose

For a cylinder, local cycle phase is `phi_i = mod(Theta - F_i, 720)`. Let psi be phi reduced modulo 360 and converted to radians. Piston travel from top-dead-center is:

```text
x(psi) = r * (1 - cos(psi)) + l - sqrt(l*l - r*r*sin(psi)^2)
```

The finite rod term is essential. A sine-wave animation or `r*(1-cos(psi))` alone is not the defined mechanism. At 0 degrees x = 0; at 180 degrees x = 2r; at 90 degrees x is not exactly half the stroke.

Use physical endpoints for the visual rig. Let p be the actual crank attachment's XY coordinates and u the bank axis. Project `q = dot(u,p)` and solve the wrist-pin distance from the crank axis:

```text
s = q + sqrt(l*l - r*r + q*q)
w.xy = s * u.xy
w.z = p.z = z_j + delta_bank
x = (r + l) - s
```

Then the rod endpoints are p and w. Its center is `(p+w)/2`, direction is `normalize(w-p)`, and its length must stay l. Orient a rod authored along a documented local axis using a quaternion that maps that axis onto this direction. The piston translates on u but does not rotate with the rod; wrist-pin geometry bridges the components.

Assert the two x formulas agree. Do not independently animate pistons from phi while letting rod endpoints follow an inconsistent bank angle. The crank's mesh journals must occupy p, including axial offsets. Use positive dimensions with `l > r > 0`. Invalid configurations produce a clear error. Only tiny round-off below zero may be clamped inside a validated square root; do not hide a physically invalid configuration with a general clamp.

### Planning verification already performed

The proposed table and equations were evaluated at all 721 integer phases from 0 through 720 for all eight cylinders: 5,768 samples. The largest difference between the projected-endpoint piston position and the analytic slider-crank result was approximately `8.33e-17 m`; rod lengths stayed at the selected l within the numeric tolerance used. Every firing phase aligned with that cylinder's geometric top-dead-center.

This is a planning derivation check, not an application test, a collision check, or validation of a manufactured engine. M02/M03 must reproduce the invariants in committed tests and inspect the rendered rig. Test with finer sampling, negative/wrapped phases, randomized valid dimensions, and browser frame schedules as well.

## 5. Four-stroke cycle and valves

Our local cycle starts at firing top-dead-center, not at the beginning of intake:

| Local phi range | Stroke | Piston direction | Idealized valve state |
| --- | --- | --- | --- |
| [0,180) | Power / expansion | Toward bottom-dead-center | Both closed |
| [180,360) | Exhaust | Toward top-dead-center | Exhaust open within interval |
| [360,540) | Intake | Toward bottom-dead-center | Intake open within interval |
| [540,720) | Compression | Toward top-dead-center | Both closed |

Valve lift is zero exactly at interval boundaries. For an active interval `[a,b]`, use an educational smooth profile:

```text
lift(phi,a,b) = h * sin(pi * (phi-a)/(b-a))^2   when a <= phi <= b
lift = 0 otherwise
```

Exhaust uses a=180, b=360. Intake uses a=360, b=540. This excludes valve overlap and ignition advance deliberately. It is not an OEM cam profile. Peak lift occurs at local phi=270 for exhaust and phi=450 for intake.

The camshaft rotates at half crank speed: its lobe alpha angles decrease by Theta/2, equivalent to a positive Theta/2 Euler Z rotation of an angle-zero-authored cam mesh as explained in section 3. Derive fixed lobe orientations against each follower's actual contact direction so the lobe's peak agrees with the matching valve-lift maximum. Do not rotate decorative lobes at half speed while opening unrelated valves on a separate clock. A simplified cam/follower/rocker construction is acceptable if its linkage assumptions are stated and visible parts agree; exact contact-surface and elasticity simulation is not required.

Use 16 valves, with corresponding simplified springs, rockers, pushrods, and lifters. Both the visible valve transform and lift chart consume the same function. The named stroke is a cycle interval; UI text should distinguish an interval label from a valve being exactly seated at its boundary.

General cycle explanations are supported by NASA's [Otto-cycle overview](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/internal-combustion-engine-otto-cycle/). That source does not supply this V8 geometry or its firing table.

## 6. Time, frame rate, seeking, and firing events

The authoritative angle advances as:

```text
dThetaDegrees = 6 * nominalRPM * playbackScale * dtSeconds
```

Keep nominal RPM separate from playback scale and show their product as effective visible RPM. Default 900 nominal RPM at 1/60 scale is 15 visible crank RPM. A 720-degree cycle then takes eight seconds, which is readable for teaching. At 1x it takes about 0.1333 seconds, so visible motion can alias at display refresh rates; do not promise that individual firing events remain visually resolvable at all speeds.

The model is an analytic function of angle, so no rigid-body timestep integration is required. The controller owns elapsed-time policy and event delivery. Keep a cycle counter plus a bounded phase, or an equivalently safe monotonic representation, to avoid long-run precision loss. Generate each firing event whose global boundary lies in `(previousAngle, nextAngle]`, including multiple crossings during one tick. Never use a narrow 'near TDC' window that can be skipped at high RPM.

At initialization, cylinder state at angle zero may show the correct phase without emitting an audio event. On seek, set the requested phase atomically, pause, refresh all dependent state, and clear event history/pending sound. Do not replay the intervals crossed by scrubbing. A next-event command seeks to the strictly next boundary, not the current boundary again.

On document hide, suspend advancement and sound. On return, reset the elapsed-time origin; do not catch up minutes of motion or combustion events. For anomalously long active-frame gaps, use an explicit capped/paused advancement policy and record it in controller tests. Ordinary frame-rate differences below that policy threshold must produce the same angle after equal elapsed time. Exploded mode freezes the operating phase; reassembly does not auto-resume.

## 7. Volume and explicitly idealized pressure

Area A is `pi * B^2 / 4`. Instantaneous cylinder volume is `V(phi) = Vc + A*x(phi)`. Maximum volume is `Vmax = Vc + Vd`. Use calculated volume and the exact same piston x as the rig.

For the teaching plot, choose explicitly disclosed constants: absolute intake/exhaust pressure p0 = 100000 Pa, idealized gamma = 1.35, and an instantaneous heat-addition pressure multiplier H = 2.2. These are illustrative assumptions, not a calibration. Compression-end pressure is `P2 = p0 * CR^gamma`.

```text
Power,       0 <= phi < 180: P = H * P2 * (Vc / V)^gamma
Exhaust,   180 <= phi < 360: P = p0
Intake,    360 <= phi < 540: P = p0
Compression,540 <= phi <720: P = p0 * (Vmax / V)^gamma
```

The plotted cycle includes an instantaneous constant-volume pressure increase at firing TDC and a constant-volume drop at expansion BDC. Include paired pre/post points at those volumes so the chart draws vertical segments rather than an accidental diagonal across finite volume. The state function is right-continuous at boundaries; chart samples can represent both sides separately.

This combined educational plot simplifies gas exchange to a common intake/exhaust pressure and uses idealized adiabatic compression/expansion. It omits the pumping loop, real heat release duration, heat transfer, residual gas, flow losses, ignition advance, friction, and changing gas properties. An idealized chamber-pressure label must remain visible whenever numeric pressure is shown. Axes may use cc and bar absolute, with explicit conversion from SI. Do not label these values live measured pressure.

RPM changes time traversal only; it does not alter this curve. Do not compute or advertise realistic horsepower, torque, fuel consumption, efficiency, or temperatures from this illustrative model. NASA's [thermodynamic analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) supports the distinction between an idealized cycle and actual engine behavior.

## 8. Required mechanical test invariants

Test piston travel bounds `[0,2r]`, TDC/BDC values, 360-degree mechanical periodicity, 720-degree cycle periodicity, rod length, shared-journal endpoints, bank-axis confinement, finite outputs, and phase-table TDC consistency. Test actual render-matrix journal points against solver points, including the alpha-to-Euler sign conversion. Test exactly eight firing events in a complete half-open 720-degree cycle and uniform 90-degree event spacing, without duplicating an endpoint. Test valve lift bounds, seated boundaries, half-speed cam phase, volume bounds, and pressure/volume unit conversions.

Integration tests must compare all displayed/scene values with one snapshot at selected phases, including wraparound. Rendering a plausible screenshot is not evidence that these equations are implemented correctly. Passing these equations does not replace an inspection of collisions, ring/skirt alignment, crank web layout, or exploded assembly geometry.
