# V8 Engine Lab

An interactive, browser-based V8 engine explorer: inspect the mechanism, scrub a four-stroke cycle, reveal the internals, and understand how the parts move together.

**Status: implementation planning. The application has not been built or deployed.**

This is Jordan Davis's independent portfolio project, inspired by [Dilum Sanjaya's V8-engine visualization](https://x.com/DilumSanjaya/status/2096280244663775423). It is not an Earth simulator and is not affiliated with the original creator. The reference video was not playable during planning; no frame-by-frame or source-code reverse engineering is claimed. See the evidence boundaries below.

## Start here

| Document | Purpose |
| --- | --- |
| [ASTRA goal](docs/ASTRA_GOAL.md) | Copy-ready implementation goal and execution rules |
| [Roadmap](docs/ROADMAP.md) | 72 implementation tasks across 12 gated phases |
| [Product specification](docs/PRODUCT_SPEC.md) | Required experience, controls, visual direction, and scope |
| [Mechanical specification](docs/MECHANICS.md) | Coordinate system, valid cross-plane rig, equations, and timing |
| [Architecture](docs/ARCHITECTURE.md) | Modules, data contracts, state ownership, and deployment |
| [Test plan](docs/TEST_PLAN.md) | Mechanical, functional, visual, accessibility, and performance gates |
| [Reference analysis](docs/REFERENCE_ANALYSIS.md) | Verified facts, unknowns, reconstruction strategy, and reference review procedure |
| [Decisions](docs/DECISIONS.md) | Pre-decided engineering choices and change policy |
| [Progress](docs/PROGRESS.md) | Execution checkpoint and evidence ledger |
| [Sources](docs/SOURCES.md) | Attribution and authoritative implementation references |
| [Agent instructions](AGENTS.md) | Repository-specific rules for implementation agents |

## Intended experience

A detailed, procedurally modeled 90-degree cross-plane V8 in a restrained technical studio. Visitors can orbit the engine, pause or slow its motion, inspect individual cylinders and components, switch between assembled/sectioned/exploded views, and see a synchronized cycle diagram and educational pressure-volume trace. A guided tour and an original demonstration recording make the engineering accessible to portfolio visitors.

The project prioritizes correct slider-crank geometry and consistent four-stroke timing over cosmetic complexity. It is an **educational mechanism and idealized-cycle visualization**, not a validated combustion, acoustic, stress, emissions, or engine-design simulator.

## Planned stack

TypeScript, React, Vite, Three.js through React Three Fiber, a small UI state store, Vitest, and Playwright. Static hosting; no backend, login, database, paid API, or AI inference required at runtime. Version selection and lockfile generation are implementation tasks, not completed setup.

## Implementation order

Reference and scope -> toolchain -> single-cylinder proof -> complete V8 rig -> detailed geometry -> exploration controls -> cycle education -> visual polish -> sharing/tour -> optional sound -> hardening -> portfolio release.

All required P0/P1 tasks must pass their acceptance gates before release. Optional P2 audio must not delay the core release. Exact reference fidelity remains unverified until footage can be reviewed.

## Local development

There is no runnable app yet. M01 will establish and verify `pnpm install --frozen-lockfile`, `pnpm dev`, `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm test:e2e`, `pnpm build`, and `pnpm preview`. Do not interpret these planned commands as a currently functioning installation.

## Attribution and licensing

Credit the original inspiration in the eventual application About panel and final README. Build original code and geometry. Do not copy the creator's video, audio, models, screenshots, or source into distributable assets without an appropriate permission/license. Public visibility does not itself establish permission to reuse content. Select the license for Jordan's original project before an explicitly open-source release; no license has been assumed for external material.
