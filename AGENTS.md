# Research Vault Agent Contract

Read [the governance contract](docs/GOVERNANCE.md) before changing research state. Classify each mutation as `CAPTURE`, `ROUTINE_UPDATE`, or `CANONICAL_CHANGE`; a commit or passing check never grants scientific authority. Human review is required for canonical meaning, evidence admission, and terminology. Nested `AGENTS.md` files may narrow these rules but cannot weaken them.

## Ownership and boundaries

This vault owns cross-project canonical concepts, literature understanding, cross-project methods, knowledge maps, project portals and summaries, and bibliographic-facing Markdown. It does not own project executable state, project code, experiments, raw simulation results, adopted project architecture, the Zotero database or attachment tree, or large durable assets.

`inbox/` is provisional capture. An admitted agent may append bounded capture material there only when explicitly authorized. Inbox material is not canonical knowledge until deliberately promoted, merged, or discarded.

A design-lab repository is canonical for its executable research state. Vault project notes are portals and synthesized knowledge only. Never duplicate a project's complete experiment register, decision log, verification state, run history, or code tree here.

## Routing a note

Use the smallest canonical home that answers the question:

- `inbox/` for authorized, bounded, unreviewed capture.
- `concepts/`, `literature/`, or `methods/` for cross-project knowledge that has been reviewed and synthesized.
- `projects/` for a portal or summary that links outward to the project repository.
- `terminology/` for reviewed cross-project bilingual canonical terms; a Lab owns its project-local terms.
- the project repository for executable state, experiments, decisions, code, or run evidence.

Before creating a canonical note, search its home and links for the same subject, citekey, DOI, method, or project. Update the existing note when it is the same enduring subject; create a new note only when it has a distinct scope. See [the promotion workflow](docs/PROMOTION_WORKFLOW.md) and the [templates](templates/).

Use [canonical terminology guidance](docs/TERMINOLOGY.md) for bilingual wording, provenance, deprecation, and explicit Lab-to-Vault promotion. A project reference does not automatically promote or synchronize a term.

## Zotero and durable assets

Zotero is authoritative for bibliographic records and managed attachments. Vault notes may contain a citekey, Zotero item key, DOI, URL, annotations, interpretation, and links; never copy Zotero databases or storage.

Large durable assets belong in `ResearchLibrary`. Refer to them logically, for example:

```yaml
asset_ref: projects/<project>/<artifact>
```

Never use a machine path as canonical asset identity, and never create a symlink or junction from this vault into OneDrive.

## Agent writes and Git

Direct Markdown edits are allowed only within the admitted mutation scope. Web ChatGPT may add bounded capture directly when authorized; canonical knowledge refactors require a branch/PR or another explicitly reviewable Git change. Local Codex keeps all edits reviewable. No agent may silently bulk-rewrite canonical knowledge.

An agent may commit directly only when its admitted scope explicitly permits it; otherwise prepare a review branch. Treat Zotero metadata and OneDrive assets as references, not content to import. The workflow states the create-versus-update and review rules precisely.

Git is authoritative for knowledge history. Do not rewrite Git history merely to reorganize notes.

## Obsidian and minimalism

Track only stable baseline Obsidian configuration. Ignore workspace state, community plugins, plugin data, and other machine-specific state.

Do not add services, databases, asset registries, MCP layers, or custom CLIs unless a later concrete requirement establishes necessity.

See [Obsidian conventions](docs/OBSIDIAN.md), [template specialization](docs/SPECIALIZATION.md), and [safe instance upgrades](docs/UPGRADE.md) before changing tracked configuration or creating an instance. A specialized instance reviews template evolution semantically on a branch; it never lets a template update overwrite its knowledge, identity, governance, or local configuration.
