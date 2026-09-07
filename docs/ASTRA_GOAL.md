# ASTRA implementation goal

Use this as a goal prompt in a coding environment opened on `jdavis-software/v8-engine`. The `/goal` prefix below is the user's intended invocation style, not a claim that this planning session has started an autonomous run. No application implementation has been executed by this handoff.

## Copy-ready goal

```text
/goal Build V8 Engine Lab in this repository into an original, portfolio-quality, browser-based interactive V8 engine explorer.

First read AGENTS.md and docs/PROGRESS.md, then docs/PRODUCT_SPEC.md, docs/MECHANICS.md, docs/ARCHITECTURE.md, docs/ROADMAP.md, docs/TEST_PLAN.md, docs/REFERENCE_ANALYSIS.md, docs/DECISIONS.md, and docs/SOURCES.md. Follow the existing 72-task roadmap rather than replacing it with a generic plan. Work only in this repository and preserve any user changes.

This is a 90-degree cross-plane V8 internal-combustion engine project, not an Earth simulator and not the JavaScript V8 runtime. The original inspiration is https://x.com/DilumSanjaya/status/2096280244663775423 and its /video/1 view. The planning session could retrieve the post description but could not play the video or inspect the original V8 source. Recheck the reference in the available browser, record only genuine observations, and proceed with our independent specification if access is still blocked. Never claim video/source fidelity without evidence.

Use TypeScript, React, Vite, and Three.js through React Three Fiber, with pure TypeScript engine math, semantic HTML controls, small SVG charts, Vitest, and Playwright. Resolve and pin a compatible stable toolchain from official documentation and generate the real lockfile. Keep the application static, local-first, and runnable without a backend, account, database, API key, paid asset, or AI inference service.

Implement the single-cylinder proof first, then the complete shared-crank V8 before polishing geometry. Follow the exact coordinate system, paired journal layout, firing table, finite-rod slider-crank equations, cam ratio, idealized valve timing, and event-boundary logic in docs/MECHANICS.md. A single authoritative phase must drive pistons, rods, valves, firing indicators, and charts. Test the physical endpoints and rod lengths; do not animate eight independent pistons or hide an impossible rig behind attractive materials.

Deliver original detailed procedural engine geometry; orbit and camera presets; play/pause, nominal RPM, explicit playback scale, scrub and stepping; canvas and keyboard-accessible part selection; inspection/section and reversible paused exploded views; synchronized four-stroke, firing-order, valve-lift, and explicitly idealized pressure-volume explanations; responsive desktop/mobile UI; reduced motion and WebGL failure handling; a six-step guided tour; validated share URLs; and original PNG capture. Match the adopted full-surface visual design and inspect actual browser screenshots as well as test outputs.

Finish all required P0/P1 tasks in dependency order. P2 synthesized sound is optional and must not delay the core release; defer it explicitly if necessary. Do not add advanced physics, arbitrary engine configuration, racing gameplay, authentication, cloud services, or unrelated features. Do not copy the reference creator's media/code/assets without appropriate permission and retain inspiration attribution.

After each coherent task, run its focused tests, inspect affected rendered states, fix defects, make a task-sized commit, and update docs/PROGRESS.md plus the matching roadmap/GitHub checklist with actual evidence. Use separate worktrees and nonoverlapping file ownership for parallel work; one owner controls the engine model until M03 passes. Do not mark unrun tests or unimplemented sound as complete.

Do not stop at a scaffold, a screenshot, a pretty spinning object, or a successful build. Complete the verification matrix, browser journeys, accessibility review, resource-stability checks, and measured performance report. Produce an accurate README, architecture/mechanics explanation, original screenshots, and a working-control demo recording. Verify the production build under /v8-engine/ and prepare static deployment. Publish, change repository settings, select the owner's code license, or tag a public release only with the appropriate authorization; otherwise leave a fully tested deploy-ready handoff and a narrowly scoped owner-action note.

At completion report the exact commit, implemented versus deferred features, commands and results, screenshots/media, tested browser/device details, measured performance, deployment status, and remaining limitations. If an external permission, inaccessible reference, or real-device test is blocked, record that fact without inventing evidence and complete all independent work. Leave a precise resumable checkpoint if the execution environment ends before completion.
```

## Execution guidance

### First work session

Read the progress checkpoint before editing. Perform M00-01 through M00-06, recording the reference-access outcome and adopting a complete independent design. Then establish the real toolchain and tests in M01. Before building all eight cylinders, prove the single-cylinder equations and transforms in M02. The highest-risk failure is a visually attractive but mechanically inconsistent rig, so M02/M03 are mandatory gates.

### Evidence required per task

Record task ID, implementation summary, changed modules, exact command/result, visual inspection evidence when applicable, commit, and the next task. A screenshot path must point to a real capture; a passing command must have actually run. Keep GitHub issue checkboxes and `ROADMAP.md` aligned with `PROGRESS.md`. If GitHub write access is unavailable in the implementation environment, update repository progress and document the unsynchronized issue state rather than claiming remote changes.

### Parallelization boundaries

Do not parallelize the initial engine math, phase convention, and render adapter. After M03 passes, a geometry worker may own `src/scene/geometry` and part builders while a UI worker owns `src/features` and styles, with a single integration owner for registry and scene root. Chart/tour/test work can be delegated against the frozen model contract. Do not let agents independently change the firing table, package manifest, coordinate system, or simulation clock.

### Stop and recovery rules

A failure in rod geometry, shared-journal alignment, event sequence, or cycle synchronization blocks downstream polish until fixed. An inaccessible original video does not block the independent design. Unsupported optional sound does not block the visual application. A missing publication permission does not block a production build and local preview. A missing real device does not justify pretending mobile performance was measured.

Do not erase history, force-push, replace user work, modify other repositories/global development configuration, or create paid resources. Do not ask the owner to resolve ordinary engineering choices already decided in the specification. Escalate only genuinely owner-controlled decisions or new conflicts, and continue all work not dependent on them.

### Completion vocabulary

- Implementation complete: required P0/P1 implementation and verification gates passed with documented environment coverage.
- Deploy-ready: production output and repository-base preview verified, but not necessarily public.
- Live deployed: an authorized actual public URL is verified against the deployed commit.
- Deferred: optional sound or explicitly approved later scope; never counted as an implemented feature.
- Unverified: no evidence, including the original video until it is actually inspected.
