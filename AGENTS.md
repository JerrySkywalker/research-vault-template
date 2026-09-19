# Research Vault Agent Contract

## Ownership and boundaries

This vault owns cross-project canonical concepts, literature understanding, cross-project methods, knowledge maps, project portals and summaries, and bibliographic-facing Markdown. It does not own project executable state, project code, experiments, raw simulation results, adopted project architecture, the Zotero database or attachment tree, or large durable assets.

`inbox/` is provisional capture. An admitted agent may append bounded capture material there only when explicitly authorized. Inbox material is not canonical knowledge until deliberately promoted, merged, or discarded.

A design-lab repository is canonical for its executable research state. Vault project notes are portals and synthesized knowledge only. Never duplicate a project's complete experiment register, decision log, verification state, run history, or code tree here.

## Zotero and durable assets

Zotero is authoritative for bibliographic records and managed attachments. Vault notes may contain a citekey, Zotero item key, DOI, URL, annotations, interpretation, and links; never copy Zotero databases or storage.

Large durable assets belong in `ResearchLibrary`. Refer to them logically, for example:

```yaml
asset_ref: projects/<project>/<artifact>
```

Never use a machine path as canonical asset identity, and never create a symlink or junction from this vault into OneDrive.

## Agent writes and Git

Direct Markdown edits are allowed only within the admitted mutation scope. Web ChatGPT may add bounded capture directly when authorized; canonical knowledge refactors require a branch/PR or another explicitly reviewable Git change. Local Codex keeps all edits reviewable. No agent may silently bulk-rewrite canonical knowledge.

Git is authoritative for knowledge history. Do not rewrite Git history merely to reorganize notes.

## Obsidian and minimalism

Track only stable baseline Obsidian configuration. Ignore workspace state, community plugins, plugin data, and other machine-specific state.

Do not add services, databases, asset registries, MCP layers, or custom CLIs unless a later concrete requirement establishes necessity.
