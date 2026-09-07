# V8 Engine Lab — product specification

## Product goal

Create an original, portfolio-quality browser application that makes a V8 engine understandable through direct manipulation. The engine is the product, not a decorative hero behind a marketing page. A visitor should recognize the object immediately, discover a useful interaction within ten seconds, and be able to explain the four-stroke cycle after exploring the guided tour.

The original X post is inspiration, not an inspected implementation specification. All requirements below are proposed for Jordan's version. Read `REFERENCE_ANALYSIS.md` before describing reference fidelity.

## Audience and scope

The primary audience is a recruiter, engineering peer, or curious visitor opening a GitHub portfolio link. The secondary audience is a student learning mechanism and cycle fundamentals. The application must be useful without knowing engine terminology, installing software, creating an account, or providing an API key.

Build one configurable-in-code, 90-degree, cross-plane, eight-cylinder educational engine. Required public controls change the viewing experience and playback; they do not allow arbitrary mechanical configurations. See `MECHANICS.md` for the single source of truth.

The release is an educational mechanism and idealized-cycle visualization. It is not a validated engine design tool, CFD solver, emissions predictor, stress model, dyno, acoustic measurement instrument, or exact OEM engine replica. Do not present synthetic quantities as measured telemetry.

## Priority definitions

P0 means core correctness and a working explorer. P1 means required portfolio polish and delivery. Both are required for the planned v1. P2 means optional synthesized sound; explicitly defer it rather than compromising or delaying the required release.

### Core required capabilities

| Capability | Required behavior | Priority |
| --- | --- | --- |
| Complete V8 mechanism | One connected crankshaft drives eight correctly constrained piston/rod assemblies and a synchronized cam/valvetrain | P0 |
| Engine controls | Play/pause, RPM, playback scale, cycle scrubbing, one-degree stepping, next firing event, and reset | P0 |
| Camera control | Orbit, bounded zoom, reset, and named camera presets | P0 |
| Part inspection | Canvas selection plus an accessible parts list, useful descriptions, isolate/hide/show, and selection focus | P0 |
| Section view | Reveal internals without obscuring the mechanism or silently changing its motion | P0 |
| Exploded assembly | Reversible, collision-conscious staged separation; operating animation pauses | P1 |
| Cycle explanation | Selected cylinder's stroke, firing strip, crank angle, valve lift, and idealized pressure-volume plot agree | P0/P1 |
| Visual quality | Original detailed geometry, legible materials, purposeful lighting, restrained UI, responsive layout | P1 |
| Guided tour | A stoppable six-step educational path that drives actual application state | P1 |
| Share and capture | Safe versioned URL state and original downloadable engine-view PNG | P1 |
| Graceful operation | Reduced motion, keyboard access, WebGL fallback, context-loss handling, and stable performance | P1 |
| Portfolio delivery | Accurate README, architecture explanation, test evidence, original screenshots and demo recording | P1 |
| Sound | User-enabled, simplified synthesized sound synchronized with the engine clock; isolated failure path | P2 |

## Opening experience

The default is a three-quarter technical-studio inspection view with enough housing opened or hidden to reveal the pistons and crankshaft. The engine occupies roughly two thirds of the usable desktop viewport. Use a dark graphite background, neutral metallic components, subtle ground contact, and a restrained accent palette. Stroke indicators use four distinguishable treatments plus written labels; color alone is insufficient.

Default nominal engine speed is 900 RPM, educational playback is 1/60 speed, and visible effective crank speed is 15 RPM. Show this distinction beside the controls. Sound is off. The initial selected cylinder is 1. A first visit may animate the mechanism slowly unless reduced motion is requested; do not automatically spin the camera. Under reduced motion, open paused with a clear Play action.

No fake sensor cards, invented horsepower figure, meaningless component count, exaggerated one-shot claim, login call to action, or generic analytics dashboard. Do not add a long landing page before the working explorer.

## Layout and visual direction

### Desktop, reference viewport 1440 × 900

Use a compact header containing the project name, help/tour entry, and source/About access. The main body is an expansive 3D canvas with a compact controls rail and an optional inspector. The bottom region holds the selected-cylinder cycle strip and collapsible charts. Do not let panels cover the currently focused cylinder; camera fitting must account for panel-safe viewport space.

The primary controls should remain visible: Play/Pause, RPM, playback scale, view mode, and reset. Secondary controls belong in the inspector or a settings disclosure. Use one coherent typography system, 4/8-pixel spacing increments, restrained borders, visible focus states, and explicit control labels. Dense information must still read at a normal laptop scale.

Before detailed UI work, create or adopt complete desktop and mobile design references. Cover assembled/inspection, selected part, expanded charts, exploded view, and fallback states. Concept images may guide layout, but the engine itself must be real interactive 3D geometry, never a screenshot substituted for the application.

### Tablet and mobile

At 768–1023 CSS pixels, collapse the inspector to a drawer and reduce simultaneous charts. At less than 768 pixels, keep a usable canvas above a compact control area, with a bottom sheet for inspection and charts. At 390 × 844 and 360 × 800, primary controls must not clip or require horizontal scrolling.

A single-finger drag orbits inside the canvas; browser scrolling still works outside it. Support pinch zoom where the browser permits it without disabling page accessibility globally. Avoid hover-only actions. Touch targets should be at least 44 × 44 CSS pixels where practical. Close drawers with an explicit button and Escape; restore focus to the triggering control.

## Control semantics

| Control | Defined behavior |
| --- | --- |
| Play/Pause | Freezes or advances the single authoritative phase; pausing does not reset selection, camera, or charts |
| RPM slider | Nominal speed from 600 to 6000 RPM; initial 900; input validation clamps finite values; pause is separate from RPM |
| Playback scale | Presets 1/120, 1/60, 1/30, 1/10, and 1×; show effective visual RPM; reduced speed is not mislabeled real time |
| Cycle scrubber | Global crank phase from 0 to 720 degrees; seeking pauses atomically, updates every view, and clears pending sound events |
| Step | Advance one degree while paused; Shift + step may advance ten degrees; next-event action goes to the next firing boundary |
| Camera presets | Three-quarter, front, Bank A, Bank B, top, and crankshaft detail; smooth transitions can be disabled |
| View mode | Assembled, inspection/section, and exploded; assembled does not mean internals must remain visible through opaque metal |
| Explode amount | 0–100%; entering any nonzero amount pauses simulation; fully reassembling remains paused until Play |
| Part selection | Select stable part ID; show name, role, related assembly, and useful dimensions; select through canvas or HTML list |
| Isolate/hide/show | Operates on documented groups; hidden selection receives an explicit state, not a lost or misleading highlight |
| Reset view | Resets camera and visibility only; a separate Reset all action restores the complete default state |
| Quality | Auto, high, balanced, and low; auto may reduce rendering cost, never silently alter mechanism timing |
| Sound | Off by default; optional P2 control is absent or explicitly unavailable if sound is not implemented |

Keyboard shortcuts are optional conveniences, not the only access path. Proposed shortcuts: Space toggles playback when focus is not in a form control; Left/Right step when the timeline is focused; R resets view when not typing; Escape cancels tour or closes the topmost drawer. Never intercept native input editing or browser shortcuts.

## Part and geometry inventory

Model crankshaft main journals, four shared rod journals, crank webs/counterweights, flywheel, eight connecting rods with big/small ends, eight pistons with crowns/skirts/ring grooves and rings, wrist pins, two cylinder banks, heads and simplified chambers, intake and exhaust ports/manifolds, a central camshaft with visibly phased lobes, lifters, pushrods, rockers, 16 valves and springs, and selected bolts/bearing-cap details.

The block is not just a solid box hiding floating cylinders. Heads, rod bearings, valve locations, and manifold connections should visibly line up. Repeated fasteners may be instanced. Decorative detail must not introduce impossible intersections or undermine the cylinder numbering. Manufacturing tolerances, cooling passages, lubrication dynamics, valve float, and exact casting geometry are not required.

Each selectable part needs a stable ID and metadata. At minimum support selection by cylinder, piston, connecting rod, crankshaft, camshaft, head, intake/exhaust valve, and manifold. Avoid hundreds of individually focusable decorative bolts in the default keyboard tree.

## Educational UI

The cycle timeline uses 720 degrees and names all four strokes. A global firing strip shows the configured order; a selected-cylinder panel explains its current stroke and valve states. A simple valve-lift chart has a moving phase cursor. The pressure-volume diagram displays an explicitly idealized cycle, labeled axes and units, and the selected point.

Selecting a different cylinder changes the explanatory context, not the global engine angle. Charts and the 3D mechanism share the same snapshot. RPM changes how quickly the marker moves, not the idealized pressure curve's shape. A compact limitations disclosure explains omitted gas dynamics, friction, heat loss, valve overlap, and real combustion behavior.

Suggested tour: (1) meet the V8 and its two banks; (2) inspect a piston and finite-length connecting rod; (3) scrub four strokes of one cylinder; (4) reveal the shared crank and firing order; (5) inspect valve timing and the idealized cycle; (6) explode and reassemble the engine. Tour steps are cancellable, keyboard accessible, and use the same commands as ordinary controls. Restore the pre-tour state on Cancel; Finish leaves a useful inspection state.

## Sharing and portfolio capture

Encode only a bounded, versioned set of state: phase, selected part, camera preset, view, explosion amount, nominal RPM, and playback scale. A loaded shared link opens paused and muted. Reject malformed/nonfinite fields, unknown IDs, and unsupported schema versions safely. No personal data or tracking is required.

PNG capture exports the actual rendered engine view at a controlled resolution with an unobtrusive project label if desired. Do not misrepresent a canvas-only export as a full browser screenshot. The final README and demo recording should show this original implementation, including real controls and a mechanically revealing angle.

## Out of scope

No racing game, drivetrain/car simulator, generic engine configurator, multiplayer, arbitrary firing-order editor, OEM-certified dimensions, advanced thermodynamics, live hardware data, emissions, structural analysis, realistic fluid flow, paid asset marketplace dependency, cloud runtime, or AI chatbot. Flat-plane V8, alternative cylinder counts, realistic ignition advance, and dynamic load/torque are post-v1 work requiring separate specifications.

## Release definition

Required P0/P1 roadmap tasks and the release matrix in `TEST_PLAN.md` pass with evidence. The README reflects what actually exists. Unavailable reference footage, optional sound deferral, unpublished hosting, and untested real devices remain explicitly labeled. A visually appealing first render is not release completion.
