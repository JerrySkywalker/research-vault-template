# Research Vault governance

This Git-native contract applies to human researchers, agents, automation scripts, and external contributors. An admitted task defines its paths and permitted actions. A branch, commit, or PR makes a proposed change reviewable; it does not grant scientific authority. No agent runtime or permission service is required.

## Classify each mutation

| Class | Use | Review and authority |
| --- | --- | --- |
| `CAPTURE` | Record bounded provisional material in `inbox/`, with source and uncertainty. | Follow the admitted scope and local review rule. Capture stays provisional even after commit or merge. |
| `ROUTINE_UPDATE` | Fix links, formatting, navigation, or other mechanical/editorial detail without changing meaning or authority. | Check the diff for semantic changes. A routine label cannot make content canonical or admit evidence. |
| `CANONICAL_CHANGE` | Add or change cross-project interpretation, reusable methods, canonical terminology, provenance meaning, or an explicit adopted decision. | Prepare a reviewable diff. A human reviewer must explicitly accept the scientific or semantic change; the Owner decides any reserved adoption decision. Record the review and supporting provenance. |

Classify by effect, not by actor, path, file size, or whether a tool generated the text. Split mixed changes so the canonical part receives its review. If classification is uncertain, keep the material provisional and request human review. The repository's `AGENTS.md`, promotion workflow, and admitted task can narrow where a contributor writes; they cannot remove the canonical review gate.

## Authority and state

1. **Generated output** is a tool or agent product. Keep its producer, inputs, and limits identifiable. It is not evidence by default.
2. **Evidence** is a traceable observation or output deliberately admitted under the repository's review rules. Preserve provenance and limitations. A Git commit alone does not admit it.
3. **Interpretation** explains what admitted evidence may mean. Identify inference and uncertainty; it is not an adopted decision.
4. **Decision** is an explicit human or Owner adoption within the actor's authority, linked to the relevant evidence and interpretation.

No transition follows automatically from the previous state, a passing validator, a merge, or a persuasive summary. Agents and contributors may propose, draft, analyze, and prepare diffs. Automation may validate and perform admitted mechanical maintenance. Neither may independently admit evidence, adopt a hypothesis or project state, alter an Owner decision, or canonicalize a term. The Vault does not own a Lab's experiment evidence or project decisions.

`inbox/` is provisional. Reviewed cross-project notes in `concepts/`, `literature/`, `methods/`, and `terminology/` may be updated through the canonical review gate; navigation maps and living summaries may be reviewed mutable state. Explicit decisions, sealed evidence or receipts, and release/audit receipts are append-oriented: correct them with a linked superseding record, not a silent rewrite. Git history alone is not a substitute for visible supersession.

## Concurrent work and nested instructions

Use ordinary Git branches or worktrees, commits, reviewable diffs or PRs, and merge conflict resolution. When concurrent edits conflict on meaning or authority, preserve both proposals and obtain human semantic resolution before merging. A clean textual merge does not prove semantic agreement.

A nested `AGENTS.md` may narrow paths, actions, and review requirements for its subtree. It cannot weaken this repository's authority, evidence, provenance, review, or safety rules. Resolve contradictory instructions at the stricter boundary and escalate an unresolved authority conflict to the human reviewer.

For capture promotion, follow [the promotion workflow](PROMOTION_WORKFLOW.md). For bilingual canonical terms, follow [terminology guidance](TERMINOLOGY.md).
