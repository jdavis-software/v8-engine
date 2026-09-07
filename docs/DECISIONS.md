# Architecture decisions and scope controls

These are proposed implementation defaults approved for use by this planning brief, not observations about the original video's source code. Changing a decision requires a short documented reason, alternatives considered, migration impact, and tests. Do not reopen every choice during implementation.

## ADR-001: Static application, not a product platform

Use one React/TypeScript/Vite application. A backend, authentication, database, subscriptions, live data, and AI runtime are not needed for an engine explorer. Keep hosting static and setup free of API keys. Do not adopt Next.js solely for familiarity; SSR does not solve the core rendering or mechanism problem here.

## ADR-002: Three.js with React Three Fiber; WebGL 2 first

Use React Three Fiber for scene composition and direct Three.js math/geometry as appropriate. Keep the model independent of both. Use Drei selectively for well-scoped conveniences such as orbit controls; avoid importing an entire UI or postprocessing stack without a requirement. Resolve compatible stable versions at M01.

Use WebGLRenderer as the baseline. Do not mix WebGPU-only ClippingGroup/TSL APIs into it. WebGPU may be evaluated after the required release, but a renderer migration is not a substitute for performance work. Official references: T01–T04 in `SOURCES.md`.

## ADR-003: Analytic kinematics, not a rigid-body physics solver

Use the crank geometry and slider-crank constraint directly. A generic rigid-body engine adds constraint drift, timestep sensitivity, and tuning without improving this controlled educational mechanism. We are not simulating bearing friction, torsional vibrations, crank flex, or valve float. Correct visible connections are required; a validated dynamic engine model is outside v1.

## ADR-004: One coherent cross-plane configuration

Use the exact bank, journal, firing, and coordinate convention in `MECHANICS.md`. Do not expose arbitrary firing-order editing in v1: changing firing labels without changing cam/event and mechanical consistency can make the model impossible. A future flat-plane engine would be a separate fully specified configuration with its own tests.

## ADR-005: Procedural geometry and stable part IDs

Create geometry in code and share repeated meshes. Avoid large external model downloads and opaque skeletal animation. Geometry builders take dimensions; the part registry owns relationships, labels, selection, and exploded offsets. Code-generated 3D engine geometry is intentional engineering content, not a substitute for a decorative image asset.

## ADR-006: Separate simulation truth from display state

The pure model computes snapshots. A controller owns time and event boundaries. React owns UI intent and sampled text. Three.js consumes snapshots through refs. No per-cylinder timers, no per-frame React state updates, and no multiple authoritative RPM values.

## ADR-007: Teach slowly and disclose the playback scale

Default engine RPM is 900, but the default educational playback is 1/60 speed (15 visible crank revolutions/minute). Display both engine RPM and visual playback speed. Real-time playback is an explicit choice; do not imply that a smoothly readable slow crank is actually turning at 900 RPM. Seeking and exploded inspection pause the clock.

## ADR-008: Idealized pressure and valve profiles

Use the equations in `MECHANICS.md`. Display an idealized-cycle label. No live measured bar, horsepower, torque, temperature, or fuel-efficiency claims. Pressure depends on the defined volume and cycle assumptions, not RPM alone. The idealized lift curve is not an OEM cam profile. Advanced valve overlap and ignition advance are deferred until separately specified and tested.

## ADR-009: Original technical-studio design

Use the complete product surface described in `PRODUCT_SPEC.md`: large engine canvas, compact control rail, parts/inspection drawer, and cycle/telemetry region. Do not build a long marketing landing page before the actual explorer. Establish full desktop and mobile reference designs before detailed UI implementation. The original X video's exact style is unknown, so this is an independent visual direction.

## ADR-010: Sound is optional P2

The required application is complete when muted. Sound requires a user gesture, a supported secure context, a conservative volume cap, and a proper audio clock. Do not trigger individual samples from React renders or pretend a looped recording is physically synthesized combustion. Simplified synthesized sound must be labeled. Sound is automatically muted during slow playback, seeking, pause, explosion, and hidden-tab suspension in the first implementation.

## ADR-011: Small deterministic charts

Use HTML/SVG for the cycle strip, valve-lift plot, and pressure-volume diagram. Compute a complete cycle from pure model samples; animate only a cursor/marker. Heavy charting dependencies are not required. Provide labels and text alternatives; color cannot be the only phase indicator.

## ADR-012: Quality gates and measured budgets

Mechanical property tests precede aesthetic work. Screenshot baselines run in a fixed environment and include deterministic phase/camera. Performance targets are acceptance budgets measured on named hardware, not claims about all devices. A faster but mechanically wrong implementation does not pass.

## ADR-013: Deployment is an explicit final action

Prepare a static GitHub Pages-compatible build with `/v8-engine/` base-path support and a workflow. Verify build artifacts locally first. Publishing, repository-setting changes, and release tags require the appropriate owner authorization and available permissions. Record a deploy-ready but unpublished state honestly if those are absent. Never publish a fake live-demo URL.

## ADR-014: Reference recovery does not block independent progress

M00 records either actual reference observations or the continuing access boundary. Unverified reference fidelity cannot be marked passed. Later footage can guide visual refinements, but does not automatically authorize code/media copying or an uncontrolled feature expansion.

## Open owner decisions

A license for Jordan's original code must be selected before advertising an explicitly licensed open-source release. A deployment publication decision and optional custom domain can be made at M11. No paid services are needed. These decisions do not block local implementation, mechanical validation, or creation of original portfolio media.
