# V8 Engine Lab — progress and execution checkpoint

## Current status

**Planning handoff committed and GitHub task trackers created. Application implementation has not started.**

The target repository was empty when planning began. Twelve Markdown files now define the proposed product, mechanical model, architecture, 72-task roadmap, verification gates, and ASTRA goal. The package was committed in `5067633e4aedf6f8a967c73bc35e5ca8e5ec585a`; the repository tree was read back and all twelve files confirmed. This checkpoint update adds the verified issue references below.

No development server, application build, browser journey, CI workflow, or deployment has been created or run by this planning handoff. All 72 implementation tasks remain unchecked.

The original post's indexed description identifies an interactive V8 visualization. The actual video was not playable during planning, and no original V8 source bundle was inspected. Status: `REFERENCE_VIDEO_UNVERIFIED`. The plan explicitly separates observed post text, secondary author-statement leads, and proposed features.

## Planning evidence

The selected bank/journal/firing table and slider-crank formulas were numerically checked at 721 integer crank phases for each of eight cylinders, totaling 5,768 samples. Maximum disagreement between projected-endpoint and analytic piston travel was approximately `8.33e-17 m`; rod-length and firing-TDC checks also passed for the selected configuration. This is a derivation check only, not proof that any application implements it. Reproduce it as committed tests in M02/M03.

No code license has been selected on behalf of the owner, no external assets have been copied, and no site has been deployed. Sound is proposed optional P2 work, not a shipped capability.

## Execution counters

| Category | Status |
| --- | --- |
| Planning documents | 12 files committed; repository tree verified |
| GitHub tracking | Master #1 and 12 phase issues #2–#13 created |
| Required P0/P1 implementation tasks | 0 / 66 completed |
| Optional P2 sound tasks | 0 / 6 completed; decision pending |
| Total roadmap tasks | 0 / 72 completed |
| Application runtime/build/browser tests | NOT RUN |
| Public deployment | NOT DEPLOYED |
| Exact original-video fidelity | UNVERIFIED |

## Phase checkpoints and verified issues

Master tracker: [#1 — Build V8 Engine Lab](https://github.com/jdavis-software/v8-engine/issues/1).

| Phase | Issue | Tasks | State | Exit evidence |
| --- | --- | ---: | --- | --- |
| M00 Reference and specification | [#2](https://github.com/jdavis-software/v8-engine/issues/2) | 6 | NOT STARTED | None |
| M01 Foundation | [#3](https://github.com/jdavis-software/v8-engine/issues/3) | 6 | NOT STARTED | None |
| M02 Single-cylinder proof | [#4](https://github.com/jdavis-software/v8-engine/issues/4) | 6 | NOT STARTED | None |
| M03 Complete V8 | [#5](https://github.com/jdavis-software/v8-engine/issues/5) | 6 | NOT STARTED | None |
| M04 Detailed geometry | [#6](https://github.com/jdavis-software/v8-engine/issues/6) | 6 | NOT STARTED | None |
| M05 Exploration controls | [#7](https://github.com/jdavis-software/v8-engine/issues/7) | 6 | NOT STARTED | None |
| M06 Cycle education | [#8](https://github.com/jdavis-software/v8-engine/issues/8) | 6 | NOT STARTED | None |
| M07 Visual polish and tiers | [#9](https://github.com/jdavis-software/v8-engine/issues/9) | 6 | NOT STARTED | None |
| M08 Tour/share/capture | [#10](https://github.com/jdavis-software/v8-engine/issues/10) | 6 | NOT STARTED | None |
| M09 Optional sound | [#11](https://github.com/jdavis-software/v8-engine/issues/11) | 6 | OPTIONAL / NOT STARTED | None |
| M10 Hardening | [#12](https://github.com/jdavis-software/v8-engine/issues/12) | 6 | NOT STARTED | None |
| M11 Portfolio delivery | [#13](https://github.com/jdavis-software/v8-engine/issues/13) | 6 | NOT STARTED | None |

## Next action

**M00-01 in issue #2:** read `AGENTS.md` and the goal/specification documents, then recheck the supplied reference in the coding environment's available browser. Record actual observations or the continued access boundary. Continue M00's independent scope/design work either way. Do not begin by constructing an untested eight-piston animation or by creating cloud infrastructure.

## Tracking rules

The authoritative task definitions, per-task dependencies, target files, and acceptance criteria are in `docs/ROADMAP.md`. The master tracker and phase issues are the remote execution surface. This document records evidence and continuity. Keep all three consistent when changing implementation status or scope. If an implementation environment cannot update GitHub, record the unsynchronized remote status honestly and still maintain this repository checkpoint.

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
