# Obsidian conventions

The tracked portable baseline is `.obsidian/app.json`, `.obsidian/appearance.json`, and `.obsidian/core-plugins.json`. They contain only stable vault defaults. Workspace layouts, graph/cache state, snippets, community plugins, and plugin data are ignored because they are machine- or user-specific.

Community plugins are not installed or required. They may be documented later as optional integrations only when a concrete need exists.

Use descriptive, stable Markdown filenames in the appropriate directory; prefer clear titles and ordinary Obsidian links over numeric IDs. Keep attachments out of Git when they are Zotero-managed or large durable assets. Cite or link to Zotero using citekeys, item keys, DOI, or URL, and reference durable assets with logical `asset_ref` values. This avoids embedding OneDrive or Zotero content while preserving provenance and portability.
