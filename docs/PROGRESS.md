# V8 Engine Lab — progress and execution checkpoint

## Current status

**Planning handoff prepared. Application implementation has not started.**

The target repository was empty when planning began. The README and this documentation package define the proposed product, model, architecture, 72-task roadmap, verification gates, and ASTRA goal. No development server, application build, browser journey, CI workflow, or deployment has been created or run by this planning handoff.

The original post's indexed description identifies an interactive V8 visualization. The actual video was not playable during planning, and no original V8 source bundle was inspected. Status: `REFERENCE_VIDEO_UNVERIFIED`. The plan explicitly separates observed post text, secondary author-statement leads, and proposed features.

## Planning evidence

The selected bank/journal/firing table and slider-crank formulas were numerically checked at 721 integer crank phases for each of eight cylinders, totaling 5,768 samples. Maximum disagreement between projected-endpoint and analytic piston travel was approximately `8.33e-17 m`; rod-length and firing-TDC checks also passed for the selected configuration. This is a derivation check only, not proof that any application implements it. Reproduce it as committed tests in M02/M03.

No code license has been selected on behalf of the owner, no external assets have been copied, and no site has been deployed. Sound is proposed optional P2 work, not a shipped capability.

## Execution counters

| Category | Status |
| --- | --- |
| Planning documents | Prepared; verify repository commit before handoff |
| Required P0/P1 implementation tasks | 0 / 66 completed |
| Optional P2 sound tasks | 0 / 6 completed; decision pending |
| Total roadmap tasks | 0 / 72 completed |
| Application runtime/build/browser tests | NOT RUN |
| Public deployment | NOT DEPLOYED |
| Exact original-video fidelity | UNVERIFIED |

## Phase checkpoints

| Phase | Tasks | State | Exit evidence |
| --- | ---: | --- | --- |
| M00 Reference and specification | 6 | NOT STARTED | None |
| M01 Foundation | 6 | NOT STARTED | None |
| M02 Single-cylinder proof | 6 | NOT STARTED | None |
| M03 Complete V8 | 6 | NOT STARTED | None |
| M04 Detailed geometry | 6 | NOT STARTED | None |
| M05 Exploration controls | 6 | NOT STARTED | None |
| M06 Cycle education | 6 | NOT STARTED | None |
| M07 Visual polish and tiers | 6 | NOT STARTED | None |
| M08 Tour/share/capture | 6 | NOT STARTED | None |
| M09 Optional sound | 6 | OPTIONAL / NOT STARTED | None |
| M10 Hardening | 6 | NOT STARTED | None |
| M11 Portfolio delivery | 6 | NOT STARTED | None |

## Next action

**M00-01:** read `AGENTS.md` and the goal/specification documents, then recheck the supplied reference in the coding environment's available browser. Record actual observations or the continued access boundary. Continue M00's independent scope/design work either way. Do not begin by constructing an untested eight-piston animation or by creating cloud infrastructure.

## GitHub tracking

The authoritative task definitions are in `docs/ROADMAP.md`. A master tracker and one issue per phase are the planned remote execution surface. Add verified issue references after creation; do not invent issue numbers. This document, the roadmap, and phase issue checkboxes must remain consistent during implementation.

## Per-task evidence template

```text
Task ID:
Status: NOT STARTED / IN PROGRESS / PASS / FAIL / BLOCKED / DEFERRED
Branch and commit:
Changed modules:
Implementation summary:
Commands actually run and exit results:
Browser/device and visual states actually inspected:
Evidence paths or issue/workflow URLs:
Known limitations or blockers:
Next unblocked task:
```

Use DEFERRED only for optional or explicitly respecified scope. A blocked test is not a passing test. Preserve useful failing-test evidence and distinguish planning notes from implementation results.

## Release-only owner decisions

An original-code license decision and authorization to publish/configure hosting or tag a release remain owner-controlled. These do not prevent implementation, tests, original screenshots/recordings, or a deploy-ready static preview. Real-device availability affects the coverage that can honestly be claimed. The inaccessible original video affects only direct-reference verification, not the independent project specification.
