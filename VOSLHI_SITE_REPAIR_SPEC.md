# VOLSHi Website Architecture Repair — Builder Handoff

## Mission

Repair the existing VOLSHi website so it communicates the actual architecture coherently and professionally without redesigning the established visual identity.

This is an implementation assignment, not an architecture-discovery assignment. Do not infer VOLSHi architecture, component maturity, or product boundaries from public GitHub visibility. This document is the source of truth for the website work.

Work on branch `fix/coherent-architecture`. Do not merge to `main` until review.

## Non-negotiable architectural thesis

VOLSHi builds infrastructure between machine intelligence and human experience.

The architecture is horizontal and domain-agnostic. A deployment into a new company, role, workflow, or vertical does NOT create a fork or modified version of the core engine.

The separation is:

- **Engine / core architecture:** invariant infrastructure and durable system capabilities.
- **Cartridge:** situated operating context for a deployment — company/domain concerns, rules, constraints, knowledge, priorities, permissions, role/persona context, and developmental state as appropriate.
- **Vertical/application:** a deployment of the same core with appropriate context; not a different architecture.

The website must make this distinction understandable without implying that VOLSHi maintains industry-specific forks.

Use this conceptual line where useful:

> The core remains the core. Context changes through the cartridge.

Do not claim that the cartridge rewrites or customizes core mechanisms.

## Public narrative hierarchy

The site should support progressive disclosure:

1. 30 seconds: VOLSHi builds the span between machine intelligence and human experience.
2. 2 minutes: the span is domain-agnostic infrastructure; models can change while durable system capabilities remain.
3. Architecture: invariant core + cartridges supplying situated context.
4. Systems: individual components and their bounded responsibilities.
5. Research/evidence: why those boundaries exist and what has actually been demonstrated.

Do not turn the homepage into an investor deck or documentation dump.

## Preserve

Preserve the existing dark cinematic / near-black / white / gold visual language, existing VOLSHi and ARCHETRON assets, cinematic backgrounds, slide-based navigation, typography direction, and overall polish.

This is NOT permission to:
- redesign the brand;
- switch to paper/editorial styling;
- introduce generic SaaS cards;
- introduce terminal/grid/cyberpunk clutter;
- replace the existing hero concept;
- add decorative diagrams that do not explain architecture.

Existing hero thesis should remain recognizable:
“Building the span between machine intelligence and human experience.”

## Required architecture correction

The current ARCHETRON section presents an orbit of jobs around a core. Preserve the useful interaction idea, but make the architecture boundary explicit.

The visitor must be able to understand:

**Human / deployment context → Cartridge → invariant VOLSHi architecture → model/tool/runtime ecosystem**

The cartridge is not another engine alongside ERIE or ELLE. It is the situated context loaded into/used by the architecture.

The visual should communicate:
- the core does not become “sales ARCHE,” “healthcare ARCHE,” etc.;
- different deployments can use different cartridges while sharing the same underlying architecture;
- replaceable models/runtimes/tools are not the durable intelligence-control architecture.

Do not depict the cartridge as containing the entire core or as a code plugin that mutates the engine.

## Canonical component boundaries

Use these descriptions as authoritative for public copy. Keep claims concise and do not invent capabilities.

### ARCHE
Role: attention / pressure architecture.
Purpose: allocates cognition by pressure, consequence, and user cost; determines what deserves attention.
Invariant: “Validity is mutable. History isn’t.”
Do not describe ARCHE as the whole VOLSHi architecture.

### ERIE
Role: Epistemic Retrieval & Intelligence Engine.
Boundary: externalizes knowing — Evidence → Conclusion.
Purpose: evidence-first retrieval/intelligence, provenance, claims/knowledge relationships, custody/dockets.
Implemented engine foundation exists. Do not call it merely research or a concept.

### ELLE
Role: External Learning Loop.
Boundary: externalizes developmental learning — Experience → Rule.
Purpose: developmental continuity outside replaceable models; durable Rules, learning ancestry/provenance, scoped project/persona learning.
Status: in development. Do not present it as fully production-proven, and do not present it as merely an idea.

### CHRONOS
Role: temporal architecture / temporal state.
Foundational invariant: “The recorded past cannot change. What the system knows about the past can.”
Purpose: immutable recorded history with append-only corrections/revisions; separates event/observation/state-time concerns; supports changing knowledge without rewriting custody.
Current implementation/proof includes append-only temporal history, revision semantics, crash-safe storage/compaction work, atomic batch ingestion, authentication/per-tenant authorization, observability/runtime exposure, and active performance/calibration proof work.
Do NOT reduce CHRONOS to a one-line research concept. Do NOT claim public-repository absence means it is unimplemented.

### BOUNCER
Role: authority/governance boundary.
Purpose: controls consequential crossings — approve/deny/pause/resume/escalate/revoke/require human authority as appropriate.
Keep authority distinct from capability: being able to perform an action does not itself grant permission.

### PEEP
Role: execution observation.
Purpose: observes execution environments and normalizes operational events/telemetry. It is observation, not reasoning.
Sources can include shells/terminals, runtimes, browsers, IDEs and CI as the system expands.

### RATTER
Role: instrumentation / telemetry support.
Do not collapse RATTER and PEEP into reasoning or governance.

### CTRL TOWER
Role: operator surface.
Purpose: human-facing operational visibility/control over system state, evidence, execution and governance.

### ROSIE
Role: local runtime bridge.
ROSIE is NOT “the autonomous software builder.”
It provides local execution/runtime bridging and remains a bounded runtime component.
Do not redesign or rename ROSIE.

### ARCHESTRATOR
Role: build/execution orchestration.
Owns the Prep → Plan → Execute → Verify lifecycle and authority-aware build orchestration.
Autonomous software development is an action domain/proof surface, not the definition of VOLSHi.

### NIRMATA / persona tooling
Treat persona engineering separately from ROSIE. Do not invent maturity claims. If the current public site uses NIRMATA, retain only claims supported by this source-of-truth framing.

### SHERLOCK
Role: evidence-first investigation application/proof surface.
It demonstrates application of evidence/provenance architecture; it is not the core company.

### Personas: BRUNEL / CHIMERA / others
Personas are operating identities/configurations built on the wider architecture. They are not separate core engines.
BRUNEL has been used as a concrete operating persona/proof. CHIMERA is an apex persona concept/implementation direction.
Avoid unnecessary persona detail on the top-level architecture view.

## Engine + cartridge content requirement

Add a clear architecture explanation, preferably interactive but readable without interaction.

Suggested copy hierarchy:

**ONE ENGINE. SITUATED CONTEXT.**

“The core architecture does not change when the domain changes. A cartridge supplies the concerns, rules, constraints, knowledge and operating context of a particular deployment.”

Then visually show several illustrative cartridges entering the SAME engine. Do not use industry examples that imply current customers or validated deployments. Generic labels such as “Organization A,” “Workflow B,” or “Domain Context” are safer unless an existing VOLSHi project is explicitly presented as an internal proof/application.

The visitor should leave understanding:
- VOLSHi is infrastructure, not a vertical SaaS product.
- models are replaceable;
- deployment context is portable/separable from the invariant core;
- the durable value lies in the architecture governing knowing, learning, time, attention, authority, observation and accountable action.

## Technology page/section corrections

The current index is useful but incomplete and has incorrect boundaries.

Required:
- add CHRONOS;
- add ARCHESTRATOR if presenting build orchestration;
- correct ROSIE to local runtime bridge;
- avoid grouping that implies all listed names have equivalent maturity or architectural status;
- make Engines / Infrastructure / Operations / Applications / Personas (or a similarly accurate taxonomy) semantically defensible.

Do not add a “maturity score” or fake roadmap.

If status is shown, use factual language only:
- implemented / operational proof where established;
- in development for ELLE;
- application/proof surface where appropriate.

## ARCHETRON section

ARCHETRON is the assembled system/architecture, not a synonym for any one component.

The existing job-based interaction (observe / know / attend / learn / govern / act / account) is worth preserving because it explains responsibilities. Correct the mappings rather than throwing it away.

Preferred responsibility map:
- Observe → PEEP / instrumentation
- Know → ERIE
- Attend → ARCHE
- Learn → ELLE
- Time / preserve temporal state → CHRONOS
- Govern / authorize → BOUNCER
- Act / execute → ARCHESTRATOR + runtime/tool substrates as appropriate
- Account → evidence + operator surfaces (ERIE / PEEP / CTRL TOWER as appropriate)

Do not force every component into exactly one job if that makes the architecture false.

The architecture should show the cartridge/context boundary in relation to this assembled system.

## Research section

Retain the existing research direction but ensure Temporal Reasoning/Temporal Architecture is consistent with CHRONOS rather than sounding like an unimplemented abstract topic.

Research themes can include:
- epistemic systems;
- temporal architecture;
- attention;
- human authority;
- provenance;
- autonomous execution;
- developmental learning.

Avoid marketing claims disguised as research conclusions.

## Company section

Preserve:
“The model can change. The relationship shouldn’t have to.”

Strengthen the surrounding explanation only as needed to connect it to horizontal infrastructure and durable continuity.

Do not make the company section about autonomous software development. That is one action domain.

## Evidence / proof discipline

Public copy must distinguish:
- architectural thesis;
- implemented capability;
- active development;
- application/proof surface.

Never infer “not built” because a repository is private or absent from a public organization.

Never invent customer deployments, revenue, production scale, certifications, partnerships, or benchmark results.

CHRONOS performance numbers should not be published on the marketing site unless explicitly approved after the active calibration/proof work is finalized.

## Visual requirements

Create architecture visuals that explain boundaries, not decorative complexity.

At minimum the site should communicate two visual ideas:

1. **The Span / system flow**
Human experience ↔ durable VOLSHi intelligence-control infrastructure ↔ replaceable models/tools/runtimes.

2. **Invariant Engine + Cartridge**
A stable architecture receives situated deployment context without being forked per vertical.

The existing ARCHETRON responsibility interaction can serve as the deeper third level.

Use CSS/SVG/HTML for precise architecture diagrams when practical. Do not generate unreadable AI-image diagrams containing baked-in text.

## Mobile / interaction requirements

The existing site is slide-driven and interaction-heavy. Verify:
- no clipping of architecture labels at common mobile widths;
- cartridge/engine diagram remains understandable on touch devices;
- hover-only information has tap/focus equivalents;
- modal/detail surfaces remain dismissible;
- keyboard navigation still works;
- horizontal slide gestures do not make internal architecture controls unusable;
- text remains readable without zooming.

## Acceptance gate

Do not declare completion until all are true:

1. A first-time visitor can explain VOLSHi as horizontal infrastructure rather than a vertical product.
2. They can explain engine vs cartridge correctly.
3. They do not come away believing each vertical modifies/forks the core.
4. CHRONOS is present and not described as vaporware.
5. ROSIE is not described as the autonomous software builder.
6. ARCHESTRATOR/build orchestration and ROSIE/runtime responsibilities are not collapsed.
7. ERIE, ELLE and CHRONOS have distinct knowing/learning/time boundaries.
8. BOUNCER authority is distinct from execution capability.
9. Autonomous software development is presented as one action domain/proof, not VOLSHi’s identity.
10. Existing visual identity is preserved.
11. Desktop and mobile interactions work.
12. No unsupported commercial or maturity claims were added.
13. No architecture was inferred from public repo visibility.
14. All changed copy is internally consistent across Technology, ARCHETRON, Research and Company.

## Builder behavior

Do not interview the founder for information already specified here.
Do not perform open-ended public GitHub archaeology to redefine the architecture.
If implementation details in the current site conflict with this document, this document wins for the website repair.
If a genuinely unresolved contradiction blocks implementation, identify the exact contradiction and the smallest decision required; do not ask broad discovery questions.

## Delivery

Implement on `fix/coherent-architecture`.
Keep commits logically grouped.
At completion report:
- files changed;
- architecture/copy corrections made;
- interaction/visual changes made;
- desktop/mobile verification performed;
- any remaining uncertainties;
- commit SHA(s).

Do not merge to `main`.
