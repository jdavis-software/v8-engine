# Sources and attribution register

Reviewed during planning on 2026-09-06. Recheck current official documentation when implementing; this register is not a package-version lockfile. Original formulas, geometry choices, performance budgets, and UX decisions in this plan are our proposed design unless explicitly attributed otherwise.

## Inspiration and evidence leads

| ID | Source | Used for | Limit |
| --- | --- | --- | --- |
| R01 | [Original X post](https://x.com/DilumSanjaya/status/2096280244663775423) | Subject and creator attribution from indexed original text | Video and full original page not retrievable in planning |
| R02 | [Supplied video link](https://x.com/DilumSanjaya/status/2096280244663775423/video/1) | Future direct reference review | Not played or visually inspected |
| R03 | [Creator reply about code-generated geometry](https://x.com/DilumSanjaya/status/2096622677155078408) | Follow-up verification lead | Original reply could not be retrieved |
| R04 | [Creator reply about Three.js](https://x.com/DilumSanjaya/status/2096622051654287519) | Follow-up verification lead | Original reply could not be retrieved |
| R05 | [Third-party mirror of creator posts](https://w.twstalker.com/DilumSanjaya) | Located R03/R04 and reproduced creator statements | Secondary transport; not source-code evidence and not the technical basis of the implementation |

Do not use commentary reposts as proof that the original physics, numerical values, or UI behavior were independently validated. Do not infer rights to original media from a public post or a community collection.

## Mechanical principles

| ID | Primary source | Application |
| --- | --- | --- |
| M01 | [NASA: Internal Combustion Engine — Otto Cycle](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/internal-combustion-engine-otto-cycle/) | Distinction between mechanical operation and thermodynamic explanation; four-stroke fundamentals |
| M02 | [NASA: Engine Thermodynamic Analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) | Idealized pressure-volume cycle and explicit idealization |
| M03 | [NASA: Compression Stroke](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/compression-stroke/) | Closed-valve compression explanation |
| M04 | [NASA: Power Stroke](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/power-stroke/) | Expansion/power explanation |
| M05 | [NASA: Exhaust Stroke](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/exhaust-stroke/) | Exhaust explanation |

NASA's historical teaching engine is not the proposed V8. Its pages support general cycle principles, not our V8 dimensions, journal layout, firing order, materials, or fidelity to the reference. Our 90-degree bank arrangement and phase table are explicitly derived in `MECHANICS.md`; selected dimensions are fictional educational defaults, not an OEM specification.

## Rendering and state

| ID | Official source | Application |
| --- | --- | --- |
| T01 | [Three.js WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html) | WebGL 2 baseline; local clipping; render statistics |
| T02 | [Three.js WebGPURenderer overview](https://threejs.org/manual/en/webgpurenderer) | A possible later renderer, deliberately not required in v1 |
| T03 | [Three.js ClippingGroup](https://threejs.org/docs/pages/ClippingGroup.html) | WebGPURenderer-only API; do not accidentally use it in the WebGLRenderer baseline |
| T04 | [React Three Fiber performance pitfalls](https://r3f.docs.pmnd.rs/advanced/pitfalls) | Reusing geometry/materials; fast updates via refs rather than React state |
| T05 | [Three.js scene fundamentals](https://threejs.org/manual/en/creating-a-scene.html) | Scene, camera, renderer responsibilities |

## Audio, testing, and delivery

| ID | Official source | Application |
| --- | --- | --- |
| A01 | [MDN: AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet) | Optional low-latency audio processor; secure-context requirement |
| A02 | [MDN: Web Audio best practices](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices) | Start/resume sound after a user gesture |
| A03 | [MDN: Autoplay guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay) | Graceful handling of blocked audio |
| Q01 | [Playwright: Visual comparisons](https://playwright.dev/docs/test-snapshots) | Repeatable screenshot baselines and environment sensitivity |
| D01 | [Vite: Static deployment](https://vite.dev/guide/static-deploy) | Build output, repository base path, GitHub Pages workflow |

## Asset register required before release

For each external texture, font, audio clip, model, icon package, or copied code fragment, record name, author, original URL, license, modification, attribution location, and bundled path. Prefer original procedural geometry, system fonts, and no external audio. Absence of this register is not permission to reuse assets. Original application screenshots and recordings must be produced from this implementation, not the inspiration clip.
