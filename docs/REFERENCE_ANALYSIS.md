# Reference analysis and reconstruction brief

Planning review: 2026-09-06. Repository: `jdavis-software/v8-engine`.

## 1. Evidence boundary

The supplied reference is [Dilum Sanjaya's X post](https://x.com/DilumSanjaya/status/2096280244663775423) and its [video view](https://x.com/DilumSanjaya/status/2096280244663775423/video/1). The indexed original post describes a detailed interactive V8-engine visualization attributed by its author to GPT-6 Astra. It is not an Earth simulator.

**The video could not be played or downloaded with the available tools during this planning session. No individual frame, exact UI layout, interaction sequence, camera path, pressure readout, audio track, or timestamp was directly inspected. No original application bundle or V8 source repository was located and inspected.** This document is an evidence-bounded reconstruction specification, not a claim that source code was recovered or the live application was tested.

The GitHub connector confirmed that Jordan's public target repository was empty before the planning files were created. The only initial content is this planning handoff; no application behavior has been implemented.

## 2. Evidence classification

| Item | Classification | Consequence |
| --- | --- | --- |
| Subject is an interactive V8-engine visualization | Verified from indexed original-post text | Use this subject and interaction category |
| Creator attributes the work to Astra | Author self-report | Attribution only; do not infer prompt count, duration, or reliability |
| Original rendering uses Three.js and code-generated geometry | Creator replies reproduced by a third-party mirror; original reply pages were not retrievable | A useful lead, not independently inspected implementation evidence |
| Framework, versions, renderer, asset pipeline, physics model | Unknown | Our stack is a deliberate proposal, not a discovered original stack |
| Exact bank geometry, firing order, dimensions, UI ranges | Unknown | Use our explicitly defined and tested educational configuration |
| Cutaway, explode, pressure/valve charts, sound, tour | Not directly verified in the footage | Treat every such feature below as a proposed requirement for Jordan's version |
| Original simulation's scientific accuracy or frame rate | Unverified | Never repeat third-party accuracy or performance claims as fact |
| Reuse rights for source, video, sound, and assets | Not established | Build original work; retain attribution links |

A search of the creator's public repositories surfaced an older jet-engine project, not an inspected source for this V8 demonstration. Do not substitute that different mechanism as the V8 implementation.

## 3. Product interpretation

The worthwhile portfolio idea is an explorable engineering object, not a video player with controls and not a dashboard filled with unrelated gauges. The intended demonstration should answer three questions quickly: what am I looking at, what can I manipulate, and why do the parts move this way?

The proposed version has three layers. The first is a convincing, detailed engine rendered as the main object. The second is direct manipulation: rotation, section views, isolated parts, phase scrubbing, and exploded assembly. The third is explanation: cylinder phases, firing order, valve movement, and a labeled idealized pressure-volume diagram. All three consume the same engine state.

A plausible implementation can be decomposed into a parametric geometry builder, an analytic mechanism model, a deterministic animation controller, an interaction/selection layer, and HTML/SVG explanatory UI. This is our reconstruction strategy; a video alone would not establish the original internals even if it were fully accessible.

## 4. Proposed subsystem analysis

### Engine geometry

Build a 90-degree V with four cylinders per bank, four shared crankpins, eight pistons, eight rods, a flywheel, crank counterweights, a central camshaft, and a simplified OHV valvetrain. Two banks and independent piston animations are not sufficient: each rod must terminate on its assigned point on the common crankshaft.

Use parameterized cylinder/lathe/extrusion/tube geometry and reusable detail groups. Keep an explicit part registry with stable IDs. Prefer build-time or initialization-time geometry composition over per-frame boolean operations. A single imported static mesh would make individual part inspection and reliable motion harder to implement and validate.

### Motion

Use slider-crank geometry rather than a sine wave for piston position. A finite connecting rod changes the travel curve. Use the actual crankpin and wrist-pin positions to construct the rod pose. The phase table in `MECHANICS.md` reconciles cylinder bank orientation, shared journals, top-dead-center events, and the chosen firing order.

### Interaction

Orbit and camera presets give the visitor spatial control. Section view makes internals legible. An exploded layout explains assembly but pauses rotation so disconnected parts do not appear to be an operating mechanism. Part selection should be available through both the canvas and a semantic HTML parts list.

### Explanation

A 720-degree timeline tracks a selected cylinder. Intake, compression, power, and exhaust have consistent names, patterns, and colors. Educational pressure is explicitly idealized and computed from volume and stated assumptions, not fabricated as measured telemetry. The curve does not change merely because RPM changes.

### Rendering

A neutral technical-studio setting, distinct metal finishes, restrained shadows, and carefully controlled highlights should communicate physical construction. Transparent shells and many overlapping effects can undermine readability. Make the default view legible before adding postprocessing.

### Portfolio narrative

The project's differentiator should be inspectable engineering: tested mechanics, original procedural geometry, synchronized explanations, documented tradeoffs, reproducible screenshots, and measured performance. A short original demo plus a clear architecture write-up is more valuable than unsupported claims about one-prompt development.

## 5. Reference review procedure for ASTRA

Timebox a new access attempt in M00. Open the supplied post in the available browser. If playback works, inspect the complete clip and record real timestamps for the opening state, each demonstrated control, camera change, selected part, chart, and final state. Do not infer a slider's full range from its current displayed value. Do not infer working interactions from a still image.

For each observation record `timestamp`, `visibleEvidence`, `confidence`, `proposedRequirement`, and `differenceFromOurSpec`. Record whether audio was actually enabled and heard. Identify any linked live demo or source from the creator; inspect those only if genuinely available. Separate visual resemblance from mechanically verified behavior.

If playback remains blocked, keep the evidence status `REFERENCE_VIDEO_UNVERIFIED`, document the attempt, and proceed with our original design. Do not hold the entire build hostage to X access. A later user-supplied MP4 or screenshots can refine visual targets without discarding the correct mechanism or expanding scope automatically.

Do not commit copied reference footage or third-party screenshots as public portfolio assets without an established right to redistribute. Local review notes may refer to timestamped material without publishing it.

## 6. Fidelity and honesty rules

The opening README and final About panel must credit inspiration without claiming affiliation. Exact visual parity is not a release criterion until a concrete reference has actually been reviewed and adopted. Our own approved design and functional specification remain testable even when the original is unavailable.

Do not claim a reverse-engineered original React app, a recovered prompt, a specific original model format, an accurate original pressure simulation, or an observed FPS. The valid deliverable is an independently engineered application inspired by the publicly described concept.

## 7. Principal risks and mitigations

| Risk | Mitigation and checkpoint |
| --- | --- |
| Pretty but impossible moving engine | M02/M03 rod-length, journal-sharing, and TDC tests before detailed modeling |
| Reference access remains unavailable | Record the boundary; continue the independent specification |
| Rig difficult to inspect through opaque housing | Default open inspection view and part groups; section mode in M05 |
| Unrealistic pressure presented as science | Idealized-cycle label, formula-based curve, no dyno/CFD claims |
| Excessive detail destroys interactivity | Instanced details, quality tiers, measured draw-call/triangle budgets |
| Scope becomes a game/engineering suite | One engine, one application, no backend, no advanced dynamics in v1 |
| Agent stops after the first render | Explicit phase gates, screenshot review, release evidence matrix |

Source URLs and retrieval qualifications are retained in `SOURCES.md`.
