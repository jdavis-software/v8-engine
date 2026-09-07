# V8 Engine Lab — executable roadmap

## Execution contract

There are **72 tasks: 12 phases with six tasks each**. Tasks are not complete merely because this plan exists. Every checkbox starts unchecked. P0 and P1 are required for v1; M09 is optional P2 sound and may be explicitly deferred. Record evidence and the next unblocked task in `PROGRESS.md`; keep the corresponding GitHub phase checklist synchronized.

`PRODUCT_SPEC.md` defines behavior, `MECHANICS.md` defines the engine, `ARCHITECTURE.md` defines ownership, and `TEST_PLAN.md` defines release evidence. A task's acceptance criteria supplement those documents. Do not silently discard a requirement because a generic starter template makes it inconvenient.

Default execution is sequential. M04 geometry and M05 UI work may run in separate worktrees after M03 freezes the model/registry contract. M06 follows the relevant M05 controls. M10/M11 do not depend on optional sound if it is deferred. Do not start visual polish before the mechanism proof passes.

```mermaid
flowchart LR
  M00[Reference and specification] --> M01[Foundation]
  M01 --> M02[Single cylinder]
  M02 --> M03[Complete V8]
  M03 --> M04[Detailed geometry]
  M03 --> M05[Exploration controls]
  M05 --> M06[Cycle education]
  M04 --> M07[Visual polish]
  M06 --> M07
  M07 --> M08[Tour and sharing]
  M08 --> M10[Hardening]
  M08 -. optional .-> M09[Sound]
  M09 -. if implemented .-> M10
  M10 --> M11[Portfolio release]
```

## M00 — Reference, scope, and design targets [P0]

Entry: read all planning documents. Exit: a bounded specification and complete visual targets exist, with the reference-access boundary honestly recorded.

- [ ] **M00-01 — Recheck the original reference.** Dependencies: none. Targets: `docs/REFERENCE_ANALYSIS.md`. Attempt the supplied post/video in the available browser. If accessible, inspect the full clip and record real timestamps, controls, camera states, and uncertainty. If blocked, record the attempt and retain `REFERENCE_VIDEO_UNVERIFIED`. Acceptance: no invented observations; independent implementation remains unblocked.
- [ ] **M00-02 — Freeze v1 scope and limitations.** Depends: M00-01. Targets: `docs/PRODUCT_SPEC.md`, `docs/DECISIONS.md`. Confirm the one engine configuration, required P0/P1 features, optional sound, and excluded physics/platform features. Acceptance: a scope matrix distinguishes proposed functionality from observed reference features and prevents unsupported accuracy claims.
- [ ] **M00-03 — Establish the reference and asset register.** Depends: M00-01. Targets: `docs/SOURCES.md`. Verify technical sources and document external asset/license policy. Record original-code license as an owner decision rather than selecting one silently. Acceptance: all contemplated bundled assets have provenance or are explicitly original; missing footage is not redistributed.
- [ ] **M00-04 — Design the complete desktop surface.** Depends: M00-02. Targets: `docs/design/desktop.*`, design notes. Produce a full 1440×900 design reference covering canvas, transport, inspector, cycle strip, charts, selected part, and exploded state. Acceptance: readable control typography and engine-first composition; no marketing-page detour or invented telemetry.
- [ ] **M00-05 — Design responsive and failure states.** Depends: M00-04. Targets: `docs/design/mobile.*`, state inventory. Cover 390×844, narrow 360px, tablet, drawer/focus behavior, loading, unsupported WebGL, reduced motion, and context loss. Acceptance: all primary controls remain reachable and no essential interaction relies only on hover or color.
- [ ] **M00-06 — Freeze contracts and the review checklist.** Depends: M00-03..05. Targets: mechanical fixtures/design tokens/checklist in docs. Adopt coordinates, cylinder numbering, phase table, dimensions, and visual tokens from the specifications. Acceptance: one authoritative convention with no unassigned geometry-versus-animation responsibility; document intentional design deviations before coding.

## M01 — Toolchain, module boundaries, and test foundation [P0]

Entry: M00 complete. Exit: a reproducible application shell and real automated checks, not a completed simulator.

- [ ] **M01-01 — Bootstrap the pinned application.** Depends: M00-06. Targets: `package.json`, generated lockfile, Vite/TypeScript configs. Resolve compatible stable React, Three.js, R3F, test tools, and selected helper versions using official docs. Acceptance: clean install and production build succeed; no manually fabricated lockfile or runtime API keys.
- [ ] **M01-02 — Establish modules and code standards.** Depends: M01-01. Targets: `src/app`, `src/engine`, `src/scene`, `src/features`, lint/format configuration. Add strict TypeScript, path conventions, and composition roots. Acceptance: engine modules import neither React nor Three.js; no unused placeholder modules or monolithic App implementation.
- [ ] **M01-03 — Wire unit and integration testing.** Depends: M01-02. Targets: Vitest config, `tests/unit`, `tests/integration`. Add positive-modulo and configuration-validation tests and prove a deliberately wrong expected value fails. Acceptance: noninteractive test script exits correctly and meaningful engine-module coverage can be reported.
- [ ] **M01-04 — Wire browser testing and deterministic mode.** Depends: M01-02. Targets: Playwright config, `tests/e2e`, test-only bootstrap. Add a reachable test page/state mechanism and fixed phase/camera hooks for screenshots. Acceptance: smoke test opens the shell without console errors; deterministic hooks are not an unsafe production mutation API.
- [ ] **M01-05 — Establish CI and executable commands.** Depends: M01-03..04. Targets: CI workflow and scripts. Run lockfile install, lint, typecheck, tests, build, and browser smoke with bounded permissions. Acceptance: local commands and one available CI run are recorded separately; inaccessible CI is not falsely marked passed.
- [ ] **M01-06 — Build the accessible application shell.** Depends: M01-02, M00-04..05. Targets: layout/tokens/basic controls/error boundary. Implement semantic regions, typography, focus states, responsive panels, and an honest loading/fallback surface. Acceptance: shell matches design structure at desktop/mobile and contains no fake operational engine metrics.

## M02 — Single-cylinder mathematical proof [P0]

Entry: M01 complete. Exit: one visibly correct piston/rod/crank mechanism with deterministic transport. This is the first critical gate.

- [ ] **M02-01 — Implement validated configuration and units.** Depends: M01-03. Targets: `src/engine/types.ts`, `config.ts`, `math.ts`. Encode SI dimensions, bank/journal/firing metadata, and finite/range validation. Acceptance: invalid radii, rod lengths, compression ratios, duplicate cylinder IDs, and nonfinite inputs fail clearly.
- [ ] **M02-02 — Implement analytic slider-crank geometry.** Depends: M02-01. Targets: `kinematics.ts`, focused unit tests. Compute pin position, wrist position, piston travel, and rod direction from physical endpoints. Acceptance: analytic and projected formulas agree, travel stays in range, and rod length is invariant through a full rotation.
- [ ] **M02-03 — Implement the phase controller.** Depends: M02-01..02. Targets: `EngineController.ts`, `events.ts`. Implement play/pause, RPM, playback scale, seek, step, cycle count, visibility suspension, and boundary events. Acceptance: frame-schedule invariance, exact seek behavior, no hidden-tab catch-up, and no skipped multi-event crossings.
- [ ] **M02-04 — Render an inspectable proof rig.** Depends: M02-02..03. Targets: temporary proof scene and reusable transform adapter. Show one piston, rod, wrist pin, crankpin, and bore guide. Acceptance: endpoints remain connected at 0/90/180/270 degrees; piston does not rotate with the rod; proof geometry is labeled development-only.
- [ ] **M02-05 — Test boundaries and parameter properties.** Depends: M02-02..04. Targets: unit/property tests and fixtures. Cover negative/wrapped phases, 360/720 periodicity, randomized valid dimensions, and different frame schedules. Acceptance: tolerances are named, failures are meaningful, and no clamp hides invalid geometry.
- [ ] **M02-06 — Pass the visual mechanism gate.** Depends: M02-05. Targets: screenshots and `PROGRESS.md`. Inspect front/side/three-quarter views and a complete slow cycle. Acceptance: evidence shows constant rod length and coincident joints; record math-test results separately from visual findings. Do not proceed with known detached or reversed parts.

## M03 — Complete cross-plane V8 and valvetrain [P0]

Entry: M02 gate passes. Exit: eight cylinders genuinely share the specified crankshaft and timing model.

- [ ] **M03-01 — Construct the shared crank configuration.** Depends: M02-06. Targets: config and crank rig. Implement four journal stations/angles, paired axial rod planes, eight cylinder definitions, and bank numbering. Acceptance: each pair attaches to the same physical journal; the crank mesh and solver use the same rotation sign and offsets.
- [ ] **M03-02 — Solve all eight piston/rod assemblies.** Depends: M03-01. Targets: evaluator and EngineRig transform map. Apply the single-cylinder solver to the complete table without ad hoc animation offsets. Acceptance: all firing angles are geometric TDC; all rods maintain length across fine phase samples; no double-counted bank transform.
- [ ] **M03-03 — Implement four-stroke and firing state.** Depends: M03-02. Targets: `cycle.ts`, `events.ts`. Implement local 720-degree phase and the specified 1-8-4-3-6-5-7-2 order. Acceptance: eight events per half-open cycle, 90-degree spacing, correct stroke boundaries, and no second firing at the other TDC.
- [ ] **M03-04 — Add cam and valve timing.** Depends: M03-03. Targets: cycle model, cam/valve rig. Implement half-speed cam rotation, derived lobe phase, 16 idealized valve lifts, and corresponding follower/rocker motion. Acceptance: visible lobes, valves, and lift values agree at peaks and seated boundaries; no independent valve timer.
- [ ] **M03-05 — Establish the stable part registry.** Depends: M03-02..04. Targets: `scene/registry.ts`, metadata fixtures. Register assemblies, selectable kinds, cylinder associations, materials, authored transforms, and visibility/explosion groups. Acceptance: unique stable IDs, correct hierarchy, and no selection identity based on mutable array ordering.
- [ ] **M03-06 — Pass the complete-engine consistency gate.** Depends: M03-01..05. Targets: mechanical integration tests and visual evidence. Inspect a full cycle from both banks and the crankshaft view; test shared journal and cam invariants. Acceptance: no disconnected endpoints, mirrored firing labels, swapped banks, or major rod collisions; freeze the model contract for parallel work.

## M04 — Detailed original procedural engine [P1]

Entry: M03 passes. Exit: the proof rig becomes a convincing, inspectable engineered object.

- [ ] **M04-01 — Detail pistons, rings, and wrist pins.** Depends: M03-06. Targets: geometry/piston builders. Add crown, skirt, ring grooves/rings, and wrist-pin connection with consistent dimensions. Acceptance: details remain attached throughout motion, repeated geometry is shared, and piston crowns align with defined chamber volume assumptions.
- [ ] **M04-02 — Detail rods and bearing connections.** Depends: M04-01. Targets: rod geometry and materials. Add recognizable small/big ends, shank, bearing-cap details, and selected fasteners. Acceptance: correct authored axis and exact solver center length; two rods on a journal do not occupy the same axial volume.
- [ ] **M04-03 — Detail crankshaft and flywheel.** Depends: M03-06. Targets: crank builder. Add main journals, rod journals, webs, counterweights, flywheel, and front timing detail. Acceptance: every visible crankpin follows its configured position; geometry remains coherent at all camera presets and does not obscure all rod connections.
- [ ] **M04-04 — Build block, heads, and chambers.** Depends: M04-01..03. Targets: housing/head builders and inspection variants. Align banks, bore centers, head surfaces, chambers, and bearing support. Acceptance: assembled exterior is recognizable, inspection mode reveals real internals, and housing is not a solid box intersecting moving pistons.
- [ ] **M04-05 — Complete valvetrain and manifolds.** Depends: M04-04, M03-04. Targets: cam, spring, pushrod, rocker, valve, and manifold builders. Add 16 readable valve assemblies and aligned intake/exhaust paths. Acceptance: peak/seated poses fit packaging; disclosed simplified linkages remain visually coherent and correctly identified.
- [ ] **M04-06 — Review geometry and optimize repetition.** Depends: M04-01..05. Targets: registry/geometry cache and evidence. Audit silhouettes, contact points, repeated detail, triangle counts, and instancing. Acceptance: no development-only proof meshes remain in default presentation; maintain the M03 invariants and record a model inventory with measured resource counts.

## M05 — Exploration controls, selection, and assembly views [P0/P1]

Entry: M03 passes; use M04 geometry as it lands. Exit: a complete manual exploration journey.

- [ ] **M05-01 — Implement transport and speed controls [P0].** Depends: M03-06, M01-06. Targets: controls and command adapter. Wire real play/pause, 600–6000 nominal RPM, playback presets, effective speed, seek, step, and next event. Acceptance: all values agree with the controller; seeking pauses and never queues historical events.
- [ ] **M05-02 — Implement camera presets and fitting [P0].** Depends: M03-05. Targets: scene/camera and controls. Add bounded orbit/zoom, six named presets, reset, and safe panel-aware framing. Acceptance: normal and exploded bounds fit; reduced motion removes transitions; pointer drags do not select parts accidentally.
- [ ] **M05-03 — Implement selection and the parts inspector [P0].** Depends: M03-05, M05-02. Targets: raycast adapter and inspector. Support canvas and HTML-list selection, useful descriptions, cylinder associations, focus, isolate, and visibility. Acceptance: stable selections agree in both interfaces and hidden parts do not silently capture clicks.
- [ ] **M05-04 — Implement engineered section views [P0].** Depends: M04-04, M05-03. Targets: section policy/materials/housing variants. Provide assembled and explicit inspection/section options. Acceptance: the mechanism remains legible from both banks, clipping policy is understandable, and no uncapped clipping is advertised as a solid capped CAD section.
- [ ] **M05-05 — Implement staged exploded assembly [P1].** Depends: M04-06, M05-02..04. Targets: explosion controller and grouped transforms. Freeze operating pose, separate assemblies coherently, and restore exact local transforms. Acceptance: 30 explode/reassemble cycles produce no drift; returning to zero leaves the engine paused and fully connected.
- [ ] **M05-06 — Complete input and reset semantics [P0].** Depends: M05-01..05. Targets: keyboard handlers, focus management, reset actions. Implement shortcuts without hijacking typing, touch access, drawer closure/focus return, Reset view versus Reset all. Acceptance: the core journey works by keyboard and at 390px width with no dead controls.

## M06 — Cycle education and synchronized charts [P0/P1]

Entry: M03 model and M05 selection/transport available. Exit: explanation is accurate to the disclosed model and follows real application state.

- [ ] **M06-01 — Build the 720-degree cycle timeline [P0].** Depends: M05-01, M03-03. Targets: timeline and stroke legend. Show all four strokes, selected-cylinder phase, and global angle without mixing coordinate origins. Acceptance: boundary labels match the model at 0/180/360/540 and negative/wrapped inputs.
- [ ] **M06-02 — Build firing-order and cylinder status [P0].** Depends: M06-01, M05-03. Targets: cylinder strip/status panel. Show configured order and current cylinder phases, selectable through semantic buttons. Acceptance: sequence is event-correct across 720 wrap and shared snapshot state drives the canvas highlight and DOM text.
- [ ] **M06-03 — Implement volume and idealized pressure [P1].** Depends: M02-02, M03-03. Targets: `pressure.ts`, tests. Implement the documented assumptions, units, volume bounds, and piecewise pressure. Acceptance: functions are deterministic and finite, RPM does not change the curve, and the UI cannot label the values measured/real combustion.
- [ ] **M06-04 — Build the pressure-volume chart [P1].** Depends: M06-03, M05-03. Targets: SVG chart and text alternative. Precompute the cycle including vertical heat-addition/rejection legs and animate the selected marker. Acceptance: axes/units and idealization are visible; marker equals current snapshot and no incorrect diagonal connects pressure discontinuities.
- [ ] **M06-05 — Build valve-lift and stroke explanations [P1].** Depends: M03-04, M06-01. Targets: valve SVG chart and explanatory content. Use the actual lift function, both valve curves, moving cursor, and concise accessible stroke descriptions. Acceptance: charts, visible valves, and text agree at peaks and boundaries; no color-only explanation.
- [ ] **M06-06 — Pass synchronized-education review [P1].** Depends: M06-01..05. Targets: integration/browser tests and limitations copy. Scrub all cylinders through boundary and intermediate phases with diagrams visible. Acceptance: no mismatched cylinder/global phase, fabricated sensor values, or conflicting stroke text; telemetry updates are throttled without becoming stale when paused.

## M07 — Rendering polish, responsive fidelity, and quality tiers [P1]

Entry: M04 geometry and M06 explanation pass. Exit: a cohesive portfolio-grade application, not a proof rig with panels.

- [ ] **M07-01 — Establish the final lighting/material system.** Depends: M04-06. Targets: materials, lights, environment/floor. Differentiate cast and machined surfaces, preserve readable joints, and tune restrained shadows/highlights. Acceptance: all camera presets are legible without excessive glare, blacked-out interiors, or unnecessary transparency.
- [ ] **M07-02 — Match the full desktop design.** Depends: M07-01, M06-06. Targets: application styles and panel composition. Compare actual 1440×900 screenshots with M00's full-surface reference. Acceptance: typography, spacing, canvas prominence, controls, inspector, and charts are reviewed explicitly; fix material visual drift rather than merely updating baselines.
- [ ] **M07-03 — Finish tablet/mobile interactions and layout.** Depends: M07-02. Targets: responsive panels/touch behavior. Validate 1024, 768, 390, and 360px widths, portrait/landscape, safe areas, and drawer focus. Acceptance: no horizontal overflow, clipped primary action, trapped page scrolling, or unreadable chart axis.
- [ ] **M07-04 — Implement measured quality tiers.** Depends: M04-06, M07-01. Targets: quality feature and geometry/render settings. Add high/balanced/low and cautious auto adaptation of detail/DPR/shadows. Acceptance: tiers preserve the full mechanism and phase; log triangle/draw-call/resource differences instead of claiming unmeasured gains.
- [ ] **M07-05 — Finish startup and resilience presentation.** Depends: M07-02..04. Targets: loading, error boundaries, context-loss UI, reduced-motion behavior. Avoid a blank screen or infinite spinner on failure. Acceptance: unsupported WebGL has meaningful text/diagram fallback, restore actions work where supported, and reduced motion opens paused without camera auto-rotation.
- [ ] **M07-06 — Pass visual fidelity and screenshot review.** Depends: M07-01..05. Targets: baseline fixtures and fidelity ledger. Capture assembled/inspection, selected piston, charts, exploded view, and mobile. Acceptance: inspect actual images; record at least five concrete design comparisons; no silent baseline approval or unresolved major overlap/z-fighting/legibility defects.

## M08 — Guided tour, share state, and capture [P1]

Entry: M07 passes. Exit: the portfolio experience is understandable and shareable without a backend.

- [ ] **M08-01 — Implement the guided-tour state machine.** Depends: M07-06, M05/M06. Targets: tour model and overlay. Build the six specified educational steps using ordinary app commands. Acceptance: Next/Back/Cancel work, no orphaned timers remain, and Cancel restores the pre-tour state.
- [ ] **M08-02 — Add contextual help and About.** Depends: M08-01. Targets: help/limitations/attribution UI. Explain controls, nominal versus visual RPM, ideal pressure, and inspiration. Acceptance: important limitations are discoverable; source links and project identity are accurate without affiliation or unverified one-shot claims.
- [ ] **M08-03 — Implement validated versioned URL state.** Depends: M05-06. Targets: share parser/serializer and tests. Encode only allowed bounded fields and stable IDs. Acceptance: roundtrip retains intended view; malformed, huge, nonfinite, and unknown-version inputs safely fall back; shared views always open paused and muted.
- [ ] **M08-04 — Implement original PNG capture.** Depends: M07-06. Targets: capture utility and UI. Export the rendered engine view at a bounded resolution and restore renderer settings/resources. Acceptance: downloaded PNG contains the actual current view, works after resize, and does not require permanently retaining the drawing buffer.
- [ ] **M08-05 — Complete preference and session behavior.** Depends: M08-03..04. Targets: safe preference storage and reset behavior. Persist only appropriate UI preferences; schema-version storage; honor reduced motion over stored autoplay intent. Acceptance: corrupt storage cannot crash startup and audio never auto-enables on reload.
- [ ] **M08-06 — Pass the visitor journey.** Depends: M08-01..05. Targets: browser scenario/evidence. Start clean, take/cancel tour, inspect a cylinder, change views, copy/reopen a link, and capture an image. Acceptance: all actions work on desktop and narrow layout; no hidden dependency on developer tools, login, or a paid service.

## M09 — Optional synthesized sound [P2; may be deferred]

Entry: required visual/educational experience is complete. Exit: tested opt-in sound or a documented deferral. M10/M11 may bypass this entire phase.

- [ ] **M09-01 — Define optional audio scope and capability checks.** Depends: M08-06. Targets: audio decision notes and feature gate. Limit to simplified real-time sound and specify muted behavior in slow/paused/seek/exploded/hidden states. Acceptance: user gesture and secure-context requirements are handled; unsupported sound does not affect the engine.
- [ ] **M09-02 — Build the audio-clock bridge.** Depends: M09-01. Targets: audio scheduler/processor contracts. Map controller phase and RPM to sample-accurate or bounded-lookahead events with resynchronization. Acceptance: correct average RPM/15 firing frequency and bank order; no main-thread per-frame sample triggering or historical seek playback.
- [ ] **M09-03 — Implement conservative synthesized timbre.** Depends: M09-02. Targets: processor and mix controls. Combine bounded event pulses/filtering into a disclosed simplified sound with modest volume. Acceptance: no clipping, runaway gain, unlicensed samples, or claims of calibrated exhaust acoustics.
- [ ] **M09-04 — Wire consent, mute, and transport transitions.** Depends: M09-03. Targets: sound UI and lifecycle. Create/resume only after a click and crossfade on start/stop. Acceptance: pause, slow speed, seek, explode, hidden tab, and reset immediately silence/reset as specified; UI explains unavailable sound.
- [ ] **M09-05 — Test audio isolation and resource cleanup.** Depends: M09-04. Targets: audio tests and manual checks. Exercise denied autoplay, missing worklet, rapid RPM change, and repeated enable/disable. Acceptance: visual simulation survives all failures and no contexts/nodes/events leak.
- [ ] **M09-06 — Review or explicitly defer sound.** Depends: M09-01..05 if implemented. Targets: `PROGRESS.md`, README feature matrix. Record listening/device evidence and synchronization checks, or mark the whole P2 phase deferred before implementation. Acceptance: final status distinguishes absent sound from shipped/verified sound; unchecked deferred tasks are not counted as completed.

## M10 — Correctness, performance, accessibility, and resilience [P1]

Entry: M08 passes; include M09 tests only if sound exists. Exit: the required release evidence matrix passes on the tested environments.

- [ ] **M10-01 — Complete mechanical regression coverage.** Depends: M08-06. Targets: unit/integration suite and model fixtures. Consolidate all geometric, timing, volume/pressure, event, and controller invariants. Acceptance: required tolerances and known-phase cases pass and tests catch deliberately introduced sign/phase/rod-length errors during test development.
- [ ] **M10-02 — Complete end-to-end browser journeys.** Depends: M10-01. Targets: `tests/e2e`. Exercise transport, seek/wrap, both selection paths, hide/section/explode, tour, share, capture, reset, and persistence. Acceptance: no console errors or inert controls; run Chromium/Firefox/WebKit automation where supported and label actual-browser checks separately.
- [ ] **M10-03 — Measure and meet performance budgets.** Depends: M07-04, M10-02. Targets: repeatable performance scene/script and report. Measure defined warm-up, duration, phase/camera script, DPR, hardware, browser, frame timing, and resources. Acceptance: pass the recorded desktop/mobile targets or fix/explicitly document the constrained environment; emulation is not claimed as a real-device benchmark.
- [ ] **M10-04 — Audit accessibility and motion.** Depends: M10-02. Targets: semantic/focus fixes and audit report. Test keyboard-only journey, visible focus, labels, stroke text, contrast, drawer behavior, reduced motion, and noncanvas explanations. Acceptance: no critical accessibility failures or rapidly announced telemetry; note automated versus manual evidence.
- [ ] **M10-05 — Test lifecycle, bad inputs, and browser recovery.** Depends: M10-02..04. Targets: cleanup paths and robustness tests. Repeat 30 view/quality/explode cycles; hide/resume, resize, corrupt URL/storage, and simulate WebGL loss/failure. Acceptance: no accumulated transform drift, unbounded resource growth, hidden-tab event storm, or blank recovery screen.
- [ ] **M10-06 — Pass the release-candidate gate.** Depends: M10-01..05 and optional audio checks if shipped. Targets: `TEST_PLAN.md` result matrix and `PROGRESS.md`. Rerun required commands and review final screenshots on the documented browsers/devices. Acceptance: evidence links, versions, failures, limitations, and exact release-candidate commit are recorded; no unrun check is marked passed.

## M11 — Portfolio documentation, media, and delivery [P1]

Entry: M10 release-candidate gate passes. Exit: reproducible, accurately documented, deploy-ready portfolio project; publication only when authorized.

- [ ] **M11-01 — Write the final project README.** Depends: M10-06. Targets: README and feature matrix. Replace planning-only copy with actual features, setup commands, architecture summary, controls, limitations, attribution, and tested environments. Acceptance: every claim matches shipped behavior; no fake live-demo URL, badge, test result, or sound claim.
- [ ] **M11-02 — Produce original portfolio screenshots and recording.** Depends: M11-01. Targets: original assets/demo media. Capture a strong three-quarter view, cutaway, exploded view, and educational chart; record a 45–75 second working-control walkthrough. Acceptance: assets come from this app, are optimized, and reveal the mechanism rather than only a static beauty shot.
- [ ] **M11-03 — Document engineering decisions and reproducibility.** Depends: M11-01. Targets: architecture/performance/mechanics write-up, command reference. Explain derived geometry, shared clock, procedural model, tradeoffs, actual benchmarks, and tests. Acceptance: another developer can install/build/test from a clean clone and understand what was verified versus idealized.
- [ ] **M11-04 — Prepare and verify static deployment artifacts.** Depends: M11-03. Targets: Vite base configuration, Pages-compatible workflow, deployment notes. Build and serve under `/v8-engine/`, checking assets, share links, deep reload, and fallback behavior. Acceptance: static preview passes without API keys; workflow availability is not presented as an already deployed site.
- [ ] **M11-05 — Resolve release-only owner decisions.** Depends: M11-04. Targets: license/provenance register and publication status. Obtain the original-code license decision and hosting/release authorization if needed. Acceptance: publish/tag only with authorization and permissions, then verify the actual URL; otherwise record a narrowly scoped owner-gated unpublished state without blocking the completed local build.
- [ ] **M11-06 — Deliver the final evidence-backed handoff.** Depends: M11-01..05, allowing explicitly owner-gated publication status. Targets: final `PROGRESS.md`, GitHub tracker, release summary. Record commit, commands, screenshots, measured budgets, limitations, P2 deferral, live or deploy-ready status, and next owner action. Acceptance: required implementation work is complete and independently reproducible; never count an unpublished or unverified condition as a passing deployment check.

## Completion accounting

Implementation-complete requires all required P0/P1 implementation gates, with any owner-only license/publication decision tracked explicitly. Public-release-complete additionally requires appropriate licensing/publication decisions and a verified live site when a live release is claimed. P2 sound can remain deferred; do not check its six tasks as completed merely to make the total read 72/72.

Task IDs and acceptance text in this file are the source of truth. GitHub phase issues are the execution surface; `PROGRESS.md` records evidence and continuity. Keep all three consistent when changing scope or status.
