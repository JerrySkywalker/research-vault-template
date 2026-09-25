# External integration boundaries

The Vault is ordinary Git and Markdown. Its notes remain readable without an open Zotero library, Obsidian installation, asset mount, or agent provider. External tools can help produce or navigate material but cannot become the authority for a Vault interpretation or a scientific decision merely by writing a file.

## Bibliography

Zotero owns managed bibliographic records and attachments. A Vault literature note owns cross-project reading, interpretation, links, and limitations. A `citekey` is a convenient citation label and may change with export style or local convention. A `zotero_item_key` points to a managed Zotero item; it is not a universal publication identifier. A DOI identifies a registered work when available; a URL or other locator identifies the source accessed. Keep the identifiers that exist, record the source consulted, and do not invent missing ones. None of these fields by itself admits an interpretation as evidence.

No Zotero plugin is required. If a specialized instance uses another bibliography manager, preserve the separation between managed source records/attachments and the Vault's interpretation, and keep a usable DOI, URL, or source locator. Do not silently relabel a different provider's ID as a Zotero item key.

## Obsidian and Markdown

The tracked `.obsidian` files are portable defaults. Markdown headings, front matter, ordinary relative links, and descriptive note paths carry the durable content. Obsidian properties are a user interface to front matter; native Bases may be useful views, but no Base, community plugin, or plugin data is required to read or validate the Vault. Wiki links are convenient navigation and should retain enough descriptive context to be understood as Markdown. Zotero attachments and large assets stay outside Git; a note references them by managed identity or logical `asset_ref`.

## Durable assets and agents

An `asset_ref` is a logical identity, not a machine path or an asset-service URI. A note using one should identify the producing project/run where relevant, a content hash and size when meaningful, and the revision or reproduction context needed to interpret older references. The asset may live on any durable storage provider; the note must remain intelligible if the storage is temporarily unavailable. No asset service, registry, or Git LFS is required.

Web ChatGPT, Codex, local models, and future agents all follow `AGENTS.md` and `docs/GOVERNANCE.md`. Provider choice does not change `CAPTURE`, `ROUTINE_UPDATE`, or `CANONICAL_CHANGE` authority, review, provenance, or Git conflict rules. No provider runtime, MCP endpoint, automatic promotion, or synchronization is required.
