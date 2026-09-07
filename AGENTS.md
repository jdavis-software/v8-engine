# Implementation agent instructions

## Mission and reading order

Build V8 Engine Lab, an original portfolio-quality interactive engine explorer. Read `docs/ASTRA_GOAL.md`, `docs/PRODUCT_SPEC.md`, `docs/MECHANICS.md`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, `docs/TEST_PLAN.md`, and `docs/PROGRESS.md` before changing application code. Read `docs/REFERENCE_ANALYSIS.md` before making any assertion about the original demonstration.

This repository is a V8 internal-combustion engine project, not an Earth simulator and not the Chromium V8 JavaScript engine. Work only in this repository. Do not change Jordan's other projects or global development configuration.

## Non-negotiable boundaries

- Build the mechanism first: one cylinder, then a mechanically consistent eight-cylinder crankshaft, then detail and polish. Do not decorate an incorrect rig.
- A single simulation phase drives pistons, rods, valves, firing indicators, and charts. Render transforms cannot invent independent per-part clocks.
- The primary specification is a 90-degree cross-plane educational V8. Do not silently replace it with eight independent crank mechanisms, a flat-plane rig, an inline engine, or a canned model animation.
- Use original procedural geometry. A cylinder/block primitive is a development scaffold, not the final engine. Final geometry must visibly include rings, rod ends, crank journals and counterweights, heads, valvetrain, manifolds, and fastener detail.
- No backend, authentication, database, paid service, AI inference endpoint, cloud infrastructure, billing, or unrelated framework migration. The app must run without API keys.
- No physical accuracy claims beyond verified kinematics and disclosed idealizations. No fabricated telemetry, dyno numbers, temperature maps, CFD claims, or passing-test statements.
- Do not copy or redistribute the reference creator's assets or code without an appropriate license. Attribution is not a substitute for permission.
- Read current official dependency documentation, resolve a compatible stable set, pin it, and commit a real generated lockfile. Do not invent package versions or a lockfile by hand.

## Delivery loop

Take the first unblocked task in `docs/ROADMAP.md`. Read its dependencies and acceptance criteria. Implement a small coherent slice; run its focused tests; run the relevant integration checks; inspect the rendered result when visuals change; repair defects before moving on. Check a task only after recording evidence in `docs/PROGRESS.md`. A successfully compiling application is not proof that the mechanism or UI works.

Use separate worktrees/branches for concurrent agents, and assign nonoverlapping file ownership. The simulation contract and `src/engine/` have one owner until M03 passes. UI and documentation work may proceed in parallel once their contracts are frozen. Integrate frequently; do not let multiple agents edit the same package manifest, simulation clock, or scene root concurrently.

Use task-sized commits. Do not force-push, delete existing work, merge unrelated branches, or change repository settings without authorization. This planning handoff does not authorize release publication or paid service creation. Preserve user edits discovered after planning.

## Rendering and state rules

Keep the engine model pure TypeScript without React/Three.js imports. Update fast transforms through refs in the render loop, not React state on each frame. Reuse geometry, materials, scratch vectors, and matrices. The UI store owns user intent; the simulation controller owns time and current snapshots; the scene consumes snapshots. Throttle DOM telemetry to at most 10 Hz. Geometry creation, CSG, and material allocation must not happen in the hot loop.

Exploded view pauses the mechanism. Seeking never emits historical combustion/audio events. Hidden tabs do not build an event backlog. Sound is opt-in and must fail independently of the visual application. Ordinary pause, reduced-motion mode, unsupported WebGL, context loss, and malformed URL state all need intentional behavior.

## Verification and honest reporting

Use the available interactive browser first for manual inspection and Playwright for repeatable testing. Compare desktop and mobile screenshots, not just DOM assertions. Freeze simulation phase, camera, lighting, seed, and quality for visual baselines. Do not accept a new screenshot baseline solely because a test failed.

Record exact commands, exit results, browser/device details, screenshot paths, and unresolved defects. Never mark an unrun browser/device test as passed. A missing video or unavailable deployment credential is a scoped blocker, not a reason to invent evidence or abandon independent local implementation.

## Completion

Finish required P0/P1 tasks, satisfy `docs/TEST_PLAN.md`, and produce original portfolio media and an accurate README. P2 audio is optional and may be deferred explicitly. A release-ready implementation and a publicly deployed release are separate statuses. Leave a resumable checkpoint with the next task, current branch/commit, commands to run, and any narrowly defined owner action.
