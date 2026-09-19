# Research Vault Template

A public, Git-native research knowledge vault that is compatible with Obsidian, aware of Zotero ownership, and designed for careful human-and-agent collaboration.

## Model

The vault holds cross-project knowledge. Each design-lab repository holds its own executable research state and evidence. Zotero owns bibliographic records and managed attachments. Durable large assets live in `ResearchLibrary`; high-churn execution belongs in a local work area and rebuildable output belongs in a cache. These locations are roles, not a synchronization system.

Use logical durable-asset references rather than machine paths:

```yaml
asset_ref: projects/<project>/<artifact>
```

## Directory roles

- `inbox/` — provisional, bounded capture.
- `concepts/`, `literature/`, `methods/` — canonical cross-project understanding.
- `projects/` — portals and summaries, not duplicated project evidence.
- `maps/` — human and agent navigation maps.
- `templates/` and `bibliography/` — reusable note material and bibliographic-facing Markdown.

## Start a note

Copy the smallest matching file from `templates/`, give it a clear descriptive filename, and replace only the relevant placeholders. The templates use a small shared vocabulary (`type`, `status`, `tags`, `projects`) so people and agents can navigate them without a universal ontology. Bibliographic notes retain Zotero-native identifiers; asset references remain logical.

See the [promotion workflow](docs/PROMOTION_WORKFLOW.md) before promoting capture to canonical knowledge, and the [Obsidian conventions](docs/OBSIDIAN.md) before changing vault settings.

## Working with agents

Capture authorized material in `inbox/`, promote it deliberately, and make canonical refactors reviewable Git changes. Keep project code, experiment registers, run histories, and adopted designs in their canonical design-lab repository. Keep Zotero databases, attachment trees, and durable binary assets out of this repository.

## Quick start

1. Create a private repository from this template.
2. Open the clone as an Obsidian vault; only stable baseline settings are tracked.
3. Create a project portal that links to its executable design-lab repository.
4. Record durable assets with logical `asset_ref` values and provenance, not absolute paths.
5. Commit reviewable knowledge changes.

## Template evolution

Generated repositories are independent. Template improvements are versioned at a milestone, reviewed for applicability, then brought into an actual repository through an explicit branch or PR. There is no automatic sync, submodule, subtree, or template remote.

Machine locations may be useful local examples, but are never canonical identities.

When creating an instance, replace the template name, description, and any example remotes with the instance identity, then create `TEMPLATE_BASELINE.md` from the documented contract. Keep general operating guidance that remains true for the instance; do not retain template branding as a second identity. Details: [specializing this template](docs/SPECIALIZATION.md).

## Validation

Run `python scripts/validate_template.py` before proposing template changes. It uses only the Python standard library and Git to check the public repository shape and documented ignore boundaries; it does not inspect personal data or integrate with external services.
