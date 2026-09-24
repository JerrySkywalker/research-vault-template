# Specializing an instance

An instance is an independent knowledge repository, not a branded copy that tracks this template automatically. Specialization establishes instance identity and starts the lifecycle described in [UPGRADE.md](UPGRADE.md).

## Establish instance identity

An instance MUST replace the repository title, opening description, example organization or remote references, and other template-specific identity. It MUST NOT retain template branding as a second identity. It SHOULD keep generic operating guidance that remains true, including ownership boundaries, logical asset references, Zotero custody, promotion workflow, and minimal Obsidian policy, while adapting examples, project links, and local governance.

## Create lifecycle metadata

Create these two concise Markdown files at the instance root during specialization:

`TEMPLATE_BASELINE.md` is a replaceable current-state snapshot:

```markdown
# Template baseline

- Template source: <canonical repository URL or stable identity>
- Generated from: <release> (`<commit>`)
- Generated on: <YYYY-MM-DD>
- Last reviewed: <release> (`<commit>`)
- Reconciled through: <release> (`<commit>`)
- Open delta: <none or link to TEMPLATE_UPGRADES.md>
- Current intentional deviations: <none or concise summary/link>
```

`Generated from` is immutable historical origin. `Last reviewed` is the newest release whose complete delta has been evaluated. `Reconciled through` is the newest release for which every applicable delta has a final disposition, required instance changes are merged, and required validation is complete. It does not mean the instance is byte-identical to the template. On creation, all three release fields normally name the exact release used to generate the instance.

`TEMPLATE_UPGRADES.md` is cumulative and append-oriented. Add one Markdown section for each later review, including the old and reviewed exact releases, review change, result, and a human-readable delta table. Do not turn the baseline into a history log and do not add JSON, YAML, or another machine-readable upgrade manifest.

## Lifecycle ownership rules

Ownership is derived from documented repository, path, and lifecycle semantics. Do not add per-file ownership metadata.

- Reusable note forms in `templates/`, generic workflow documents, and the public validator are `TEMPLATE_OWNED`. Port later improvements through review; a locally changed form is reviewed as an `ADAPT`, never blindly replaced.
- `docs/PROMOTION_WORKFLOW.md`, `docs/UPGRADE.md`, and normally `docs/OBSIDIAN.md` are `TEMPLATE_OWNED` reusable guidance. Preserve stricter local policy when adapting them.
- The root `README.md`, root `AGENTS.md`, `.gitignore`, and `.gitattributes` become `INSTANCE_SPECIALIZED`. README is instance identity after specialization; AGENTS carries local authority; ignore/attribute rules may contain local safety or portability decisions. Review each semantically with all three states.
- The tracked `.obsidian` stable baseline files become `INSTANCE_SPECIALIZED` after use. A template default must not silently overwrite legitimate instance configuration.
- `.gitkeep` files and template onboarding/specialization prose are `BOOTSTRAP_ONLY`. They seed a new vault but must not be restored after a directory is in use or specialization is complete.
- `inbox/`, `concepts/`, `literature/`, `methods/`, `projects/`, `maps/`, and `bibliography/` contain `INSTANCE_OWNED` material once real instance content exists. Preserve it during an upgrade.
- Instance-created notes, including captures, concepts, literature interpretation, methods, portals, maps, and bibliography-facing Markdown, are `INSTANCE_OWNED`. A new template form may be adopted for future notes but never rewrites existing notes.

Template changes arrive only through an explicit, reviewable branch or PR. The metadata records provenance and review state; it is not an automatic synchronization mechanism.
