# Reproducible planning-equation audit

This additive audit follows [MECHANICS.md](MECHANICS.md) at source commit `45a9dbd8ca2991ad6f17bba558fd147cfc5d6348`. It preserves the existing product, mechanics, roadmap, goal, and GitHub trackers. It does not supersede their requirements or complete an application task.

## Reproduce

```sh
python3 scripts/verify_spec.py
```

Python 3.10+ and its standard library are sufficient. The script prints JSON and exits nonzero on a failed invariant. Its constants are explicit fixtures transcribed from the named specification revision, not dynamically parsed from Markdown. Reconcile them when the specification changes. No application packages, backend, API key, browser, or renderer are used.

## Actual execution

Executed `python3 /mnt/data/v8-engine-audit/verify_spec.py` in the planning container with Python 3.13.5; exit code 0. Script SHA-256: `be444a8c969deeef635b803f4061dc2e9410d10326c6e97b6c8e4a661c27986a`.

The regular sweep covers 0 through 720 degrees inclusive at 0.25-degree intervals for all eight cylinders: **23,048 poses**. An additional 48 poses cover negative and beyond-cycle angles. This finer independent check supplements the earlier 5,768-sample derivation check recorded in MECHANICS.md and PROGRESS.md; it does not rewrite that historical evidence.

| Invariant | Measured maximum error |
| --- | ---: |
| Fixed rod center length | 5.551115123125783e-17 m |
| Projected endpoint versus analytic piston displacement | 1.1102230246251565e-16 m |
| Positive crank Euler rotation matrix versus journal solver | 5.003707553108401e-17 m |
| 360-degree wrist-position periodicity | 1.5700924586837752e-16 m |
| Wrist position confined to bank axis | 2.7755575615628914e-17 m |
| Positive half-speed cam matrix versus angular convention | 4.96749206466014e-17 m |

Tolerance: 1e-12 m. These tiny errors are numerical roundoff, not measured manufacturing tolerances. TDC/BDC and piston-travel bounds passed. The chosen dimensions calculate to approximately 5.654867 L total displacement.

Shared-journal radial equality passed for each cylinder pair throughout the regular sweep. The audit uses explicit **arbitrary axial fixtures** of -10/+10 mm bank offsets at 112 mm journal pitch, with the same axial plane for each rod's crank and wrist endpoints. This does not finalize rod width, bearing clearance, journal width, block packaging, or bank offset for the detailed model; MECHANICS.md leaves those to consistent packaging work.

The audit checks the specified firing order `1-8-4-3-6-5-7-2`, eight events per 720-degree cycle, open-left/closed-right event boundaries, wraparound, no duplicate event for an empty interval, and matching event lists when the same constant-speed path is partitioned into 30/60/120 updates per second. This is event-function partition testing, not a implemented browser-controller benchmark.

The rotation convention tested is the CURRENT main specification: odd cylinders on Bank A at -45 degrees; even cylinders on Bank B at +45 degrees; journal alpha0 `[-45,-135,45,135]`; journal angle `alpha0-Theta`; crank Euler rotation **+Theta** and cam Euler rotation **+Theta/2**. Do not combine it with a mirrored bank convention or an alternative negative-Euler rig.

## What this does not validate

No application implementation or actual Three.js transform adapter was executed. Mathematical matrix checks still need reproduction against the real scene in M02/M03. No solid clearances, valvetrain contact, thermodynamic accuracy, acoustic accuracy, original-video fidelity, browser interaction, accessibility, performance, CI, or deployment was validated.

All 72 application roadmap tasks remain unchecked. The independent script is a planning fixture, not the TypeScript production test suite. Follow [TEST_PLAN.md](TEST_PLAN.md) and attach real application evidence as implementation proceeds.
