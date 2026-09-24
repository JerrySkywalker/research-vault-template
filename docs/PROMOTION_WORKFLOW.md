# Promotion workflow

## Lifecycle

`conversation or capture -> inbox -> review -> canonical note`

An authorized human or agent may add a bounded factual capture to `inbox/` using the inbox template. Capture can contain a source link, question, observation, or a short provisional interpretation. It is not canonical and must not silently become a project record.

During review, search the relevant canonical directory and linked notes by subject, project, citekey, Zotero item key, DOI, and method. Update an existing note when it covers the same enduring subject. Create a note when the subject is distinct or the existing note would become an incoherent mixed topic. Link related notes rather than duplicating their prose. Resolve the capture by promoting its useful content, merging it into an existing note, or discarding it; record enough provenance in the canonical note to make the conclusion intelligible.

## Canonical destinations

- `concepts/`: durable cross-project ideas and definitions.
- `literature/`: interpretation of a source, retaining its Zotero-native identifiers.
- `methods/`: reusable methods, assumptions, and limitations.
- `projects/`: a portal or synthesis that points to the project's canonical repository.
- `terminology/`: reviewed cross-project bilingual wording and definitions. See [terminology](TERMINOLOGY.md) for explicit project-local promotion, origin provenance, and historical revision references.

Project code, experiment registers, run histories, raw results, adopted architecture, and verification evidence remain in the project repository. A vault portal may summarize or link to them, but does not mirror them.

## Review and Git

Canonical refactors use a review branch or another explicitly reviewable Git change. Direct commit is appropriate only when the admitted scope explicitly grants it. Keep capture changes narrow; do not bulk-rewrite knowledge merely to reorganize it. Follow `AGENTS.md` for the ownership boundary.
