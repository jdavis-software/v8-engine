# Verification and release evidence plan

## Status and interpretation

This is an acceptance specification. The application has not been implemented and none of its runtime, browser, accessibility, deployment, or performance checks has passed yet. The numeric derivation check documented in `MECHANICS.md` is planning evidence only.

Use four explicit result states: PASS, FAIL, NOT RUN, and BLOCKED. Optional sound may be DEFERRED. Never turn unavailable hardware, inaccessible reference footage, a missing deployment permission, or an unexecuted command into PASS. Record test environment and evidence paths against an exact commit.

## 1. Required commands

M01 must create real scripts and confirm their behavior. Intended baseline:

```sh
pnpm install --frozen-lockfile
pnpm lint
pnpm typecheck
pnpm test
pnpm test:e2e
pnpm build
pnpm preview
```

Add documented scripts for focused mechanical tests, fixed-environment visual tests, and repeatable performance capture if useful. Install Playwright browser dependencies through the actual supported command for the resolved version. Do not present a command transcript until it has run. Record exit codes and relevant failures rather than only saying 'tests passed'.

## 2. Mechanical unit and property tests

### Configuration and units

Reject nonfinite or nonpositive bore/radius/rod dimensions; require rod length greater than crank radius and compression ratio greater than one. Verify unique cylinder IDs, four valid journal references, two cylinders per journal, correct bank membership, eight unique firing phases, and finite unit conversions. Validate positive modulo for negative and multi-cycle values.

### Piston and rod geometry

At every required sample, compare the analytic and projected-endpoint piston travel. For default dimensions, target absolute agreement within `1e-9 m`; use scale-aware tolerances in randomized-dimension tests. Verify rod length within `1e-9 m`, wrist-pin confinement to the bore axis, identical axial coordinates for that rod's endpoints, and travel between zero and the stroke within tolerance.

Test 0, 1, 45, 90, 135, 179, 180, 181, 270, 359, 360, 540, 719, and 720 degrees, plus fine samples and randomized valid phases. Test every cylinder at its own firing phase and at that phase plus 180/360/540 degrees. Check 360-degree mechanical periodicity and 720-degree cycle periodicity separately.

Verify each rod attaches to the journal designated by configuration, not merely a mathematically convenient independently moving point. For the paired rods on a common journal, XY crank centers must agree while their Z center planes differ as specified. Confirm the visible rig uses the solver's sign convention and parent transforms.

### Timing and event correctness

Assert the chosen firing table lands at geometric TDC and the sequence is 1-8-4-3-6-5-7-2. Count events on half-open cycle intervals so the 0/720 endpoint is not counted twice. Verify eight events per cycle and 90-degree spacing. Test a single controller tick crossing multiple firing boundaries, wraparound, pause/resume, arbitrary seek, and strictly-next-event stepping.

Verify local stroke names and valve bounds at all boundaries. Exhaust lift peaks at phi 270, intake at phi 450, with zero lift at each interval boundary and no overlap in this simplified model. Check cam half-speed and lobe/follower phase against visible valve peak timing, not just a nominal ratio in a configuration object.

### Volume and pressure

Verify `Vmin=Vc`, `Vmax=Vc+Vd`, correct SI/cc/bar(abs) conversions, and total displacement from the selected dimensions. Verify pressure is finite/positive and follows the stated piecewise idealization. Changing RPM alone must not change P(V). Test chart samples on both sides of instantaneous heat-input/rejection jumps and right-continuous snapshot boundary behavior.

### Time integration policy

For equal accepted elapsed time under 30/60/120 Hz and jittered frame schedules, final phase must agree within a documented numerical tolerance. A default 900 RPM at 1/60 playback completes a 720-degree cycle in eight seconds. Hidden-tab resume must not replay hidden elapsed time. Test the explicit large-gap cap/suspension policy separately from normal frame-schedule invariance.

## 3. Integration contracts

Freeze the controller at known phases and assert that the render adapter, selected-cylinder text, stroke strip, valve cursor, pressure marker, and cylinder highlighting all consume the same evaluated state. Selecting cylinder 3 must not change global phase. Seeking must refresh sampled UI immediately, even though moving telemetry is throttled.

Check stable registry IDs, parent/world transform composition, shared material selection behavior, and visibility rules. Hidden parts must not accidentally absorb selection hits. Test explosion amount zero returns original transforms after repeated use and preserves the frozen operating phase. Camera state does not affect mechanism output.

If an optimized preallocated evaluator is introduced, compare it against the pure evaluator across the same fixtures. Test cleanup of subscriptions and event listeners to avoid multiple controller ticks after remounts or development strict-mode cycles.

## 4. Browser journey matrix

| Journey | Required steps | Passing evidence |
| --- | --- | --- |
| Fresh visit | Open clean state; inspect default engine, controls, and explicit slow-motion label | Actual canvas renders and no console errors; no key/login required |
| Transport | Play, pause, change nominal RPM and playback scale, step, seek 0..720, next firing | Every control changes the real model; pause/seek state is coherent |
| Selection | Select piston through canvas; choose cylinder 3 in HTML list; focus/isolate/hide/show | Both selection paths agree; useful metadata and visible focus |
| Assembly views | Assembled -> section -> exploded -> reassembled | Internals legible; explosion pauses; reassembly has no transform drift |
| Explanation | Show valve/PV charts; scrub boundaries and intermediate phases; change cylinders | Chart/text/scene agree and idealization remains labeled |
| Tour | Start, Next, Back, Cancel, restart, Finish | Commands work, cancellation restores state, focus stays accessible |
| Share | Copy URL, reload it, try malformed/nonfinite/oversized fields and unknown IDs | Safe bounded parsing; intended view restored paused and muted |
| Capture | Export after selection, section, resize, and quality change | Valid original PNG reflects current engine view; resources restored |
| Persistence | Change permitted preferences; reload; corrupt/old local storage; reset all | No crash, no surprise sound/autoplay, defaults recover |
| Lifecycle | Resize, hide/resume, context loss/fallback, unmount/reopen where relevant | No event backlog, duplicated listeners, or blank recovery state |

Run repeatable automated journeys in Chromium, Firefox, and WebKit where the environment supports them. Also record manual checks in actual Safari/Chrome/Firefox for the supported desktop release. Playwright WebKit is not identical to testing every Safari version or iPhone GPU; label the distinction.

## 5. Visual evidence and fidelity

Create a deterministic mode with fixed configuration, crank phase, selection, camera, lighting, random seed, viewport, pixel ratio, and quality tier. Disable animation, audio, time-dependent labels, and variable network assets. Wait for fonts/assets/layout and the known ready state before capture. Keep visual baselines in a consistent browser/OS environment; consult [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).

Required captures: desktop three-quarter inspection at phase zero, both-bank inspection, selected piston/rod, visible educational charts at a defined phase, exploded assembly, reassembled view, mobile 390×844, narrow 360×800, and unsupported-WebGL/reduced-motion state. Compare each to the adopted M00 design rather than an inaccessible imagined original video.

An actual image review must inspect at least: engine silhouette, joint alignment, geometry collisions, materials/lighting, typography, panel/canvas balance, selected-state legibility, chart axes/labels, and mobile controls. Keep a short fidelity ledger with mismatch, evidence, fix, and remaining intentional deviation. Passing DOM assertions does not prove the model is rendered correctly. Do not approve changed baselines without viewing them.

Exact fidelity to the original X video remains NOT RUN/BLOCKED until that footage is directly reviewed. This does not prevent passing fidelity to the independent adopted design.

## 6. Performance budgets — targets, not achieved measurements

At M00/M01, record a named available desktop/laptop and a real mobile device for measurement. Do not invent hardware. A mobile-sized browser window is valid for layout testing but not evidence of mobile GPU performance. If a real mobile device is unavailable, leave its performance result NOT RUN and state that limitation.

### Measurement protocol

Use a production build, a visible foreground tab, fixed viewport/quality/DPR, no open performance-heavy browser tools during the timing capture, and recorded browser/OS/hardware/power mode. Warm up for ten seconds, then collect thirty seconds of frame deltas during the same scripted slow-engine plus orbit sequence. Repeat three times and report each run plus the aggregate. Measure high-RPM and chart-visible cases separately. Record instrumentation overhead and background/system interference where relevant.

| Metric | Initial acceptance budget |
| --- | --- |
| Balanced desktop, 1440×900 | Median at least 55 FPS, aiming at display-capped 60; p95 frame time at most 25 ms on the named reference machine |
| Low mobile, 390×844 | Median at least 28 FPS, aiming at 30; p95 frame time at most 50 ms on the named real device |
| Balanced desktop pixel ratio | Cap at 1.5 by default |
| Low mobile pixel ratio | Cap at 1.0 by default |
| High scene complexity | Aim at <=250,000 visible triangles and <=180 total draw calls per rendered frame, including additional passes |
| Low scene complexity | Aim at <=100,000 visible triangles and <=100 total draw calls per frame |
| First-load compressed JavaScript | Target <=1 MiB transferred; justify any overage with a measured bundle analysis |
| First-load non-JavaScript assets | Target <=3 MiB, excluding optional user-requested media/capture |
| Resource stability | No monotonic geometry/material/listener growth after 30 repeated view/quality/explode cycles and cleanup |

These are project budgets, not universal device guarantees. If the named baseline cannot meet a target, optimize and report the actual result; changing a budget requires a reasoned decision, not deleting the failing test. Do not fabricate draw-call data from a statistic reset that ignores postprocessing passes. Distinguish bounded caches from unbounded leaks and account for warm-up allocations.

Prefer shared/instanced geometry, sane tessellation, cached materials, throttled DOM updates, bounded DPR, and fewer shadow/postprocessing passes before changing the architecture. Quality reduction must not remove cylinders, desynchronize time, or alter the mechanical result.

## 7. Accessibility and input

Perform an automated accessibility scan where available plus a manual keyboard-only journey. Verify semantic buttons/sliders, accessible names, input ranges/units, focus visibility, logical tab order, drawer focus handling, contrast, and text alternatives for the mechanism and charts. Do not flood screen readers with live changing telemetry.

Stroke colors must have written labels or patterns. The HTML parts list is a real alternative to pointing at small 3D objects. All core controls remain reachable at 200% text zoom and narrow viewports. Test reduced-motion initial pause, nonanimated camera transitions, optional slow playback, and no automatic audio. Confirm shortcuts do not steal keystrokes from text/range inputs or ordinary browser actions.

## 8. Failure and lifecycle tests

Simulate unsupported WebGL, renderer initialization failure, context loss/restoration when available, invalid share links, corrupt local preferences, missing optional assets, failed capture, and optional audio denial. Provide useful fallback text and a retry/reset action where applicable. A black rectangle or infinite loader fails.

Repeat creation/destruction and quality/view changes, checking timers, subscriptions, geometry/material counts, event streams, and optional audio nodes/contexts. Hide the tab long enough to expose elapsed-time bugs, then verify no catch-up storm. Resize during camera and explosion transitions. Ensure command ordering is deterministic under rapid user input.

## 9. Optional sound verification

Only required if P2 audio ships. Check explicit user consent, denied autoplay handling, supported secure contexts, average firing frequency, chosen cylinder/bank order, conservative volume, no clipping, and smooth state transitions. Confirm silence during non-1x playback, pause, scrub, explosion, and hidden tabs. Listen on a documented output device; an automated mocked AudioContext test is not a listening test. Record simplified-sound limitations.

If deferred, record DEFERRED and remove misleading active sound controls. Do not add six passing checkmarks to the roadmap for unimplemented audio.

## 10. Deployment and reproducibility

A clean clone must install with the committed lockfile and complete the real verification commands. Serve production output under `/v8-engine/` and verify asset URLs, reload, shared state, About/source links, capture, and fallback behavior. Build output must not contain API keys, personal data, reference video copies, or unlicensed bundled assets.

Prepare a narrowly permissioned static-deployment workflow. Do not publish or change repository settings without authorization. Once actually authorized and deployed, record workflow run, deployed commit, real URL, and an external post-deploy browser check. A successful local preview is deploy-ready evidence, not proof of a public deployment.

## 11. Release result matrix

Copy this matrix into `PROGRESS.md` when executing and add evidence paths/URLs.

| Gate | Required for | Initial result |
| --- | --- | --- |
| Reproducible install/lint/typecheck/build | Implementation completion | NOT RUN |
| Mechanical invariants and controller tests | Implementation completion | NOT RUN |
| Complete browser user journey | Implementation completion | NOT RUN |
| Adopted-design screenshot review | Implementation completion | NOT RUN |
| Accessibility/reduced-motion/input review | Implementation completion | NOT RUN |
| Resource/lifecycle/error handling | Implementation completion | NOT RUN |
| Desktop performance on named hardware | Implementation completion | NOT RUN |
| Mobile layout and documented device coverage | Implementation completion | NOT RUN |
| Real mobile performance | Claimed real-device performance support | NOT RUN |
| Optional sound checks | Only if audio ships | DEFERRED pending scope decision |
| Original media and honest README | Portfolio handoff | NOT RUN |
| License/provenance decisions | Explicitly licensed public release | NOT RUN |
| Repository-base static preview | Deploy-ready claim | NOT RUN |
| Authorized live deployment plus smoke test | Live-demo claim | NOT RUN |
| Original-video direct review | Exact-reference-fidelity claim | BLOCKED during planning |

The release summary must distinguish implementation complete, deploy-ready, live deployed, and optional/unverified conditions. Never compress these into an unsupported 'everything done' statement.
