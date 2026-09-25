# Obsidian conventions

The tracked portable baseline is `.obsidian/app.json`, `.obsidian/appearance.json`, and `.obsidian/core-plugins.json`. They contain only stable vault defaults. Workspace layouts, graph/cache state, snippets, community plugins, and plugin data are ignored because they are machine- or user-specific.

At template release these three files are reusable baseline defaults. Once a vault is instantiated they are `INSTANCE_SPECIALIZED`: a later template change is a reviewed suggestion, not authority to replace an instance's preferences. Compare the prior template baseline, new template release, and current configuration; use `ADAPT` or `SKIP` where appropriate, and preserve legitimate local choices.

Community plugins are not installed or required. They may be documented later as optional integrations only when a concrete need exists.

Markdown text, YAML front matter, descriptive paths, and links are the durable contract. Obsidian properties edit front matter, and native Bases can provide optional views; neither a Base nor a community plugin is needed to read or validate the notes. Keep a note intelligible from its text and recorded identifiers even when Obsidian is unavailable.

Use descriptive, stable Markdown filenames in the appropriate directory; prefer clear titles and ordinary Obsidian links over numeric IDs. Keep attachments out of Git when they are Zotero-managed or large durable assets. Cite or link to Zotero using citekeys, item keys, DOI, or URL, and reference durable assets with logical `asset_ref` values. This avoids embedding OneDrive or Zotero content while preserving provenance and portability.
