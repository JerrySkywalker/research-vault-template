# Safe instance upgrade

## Purpose and boundary

A specialized vault reviews an upgrade as a semantic three-way comparison:

```text
previous exact template release + new exact template release + current specialized vault
```

Use ordinary Git diffs, a review branch or PR, and human/agent semantic review. Git ancestry between template and instance is not required. This document does not create an updater, synchronization link, custom merge engine, manifest, or migration service.

An explicit admitted Goal is required before changing an instance. A newly released template is information, not authority to mutate an instance.

## Shared lifecycle vocabulary

Use only these ownership roles:

| Role | Meaning and default review behavior |
| --- | --- |
| `TEMPLATE_OWNED` | Reusable guidance, blank form, or generic validator. Normally propose `PORT`; use `ADAPT` if local intent diverged. |
| `INSTANCE_OWNED` | Real instance knowledge or state. Preserve it; a template delta never replaces it. |
| `INSTANCE_SPECIALIZED` | Template-derived identity, governance, or configuration intentionally adapted locally. Use semantic three-way review, normally `ADAPT`. |
| `BOOTSTRAP_ONLY` | Seed/onboarding material whose original lifecycle ends at or after specialization. Do not reintroduce or refresh it automatically. |

Do not add per-file ownership metadata. Apply documented repository/path/lifecycle semantics to the smallest stable semantic unit. A populated directory or note is instance-owned even when a blank form at another path remains template-owned.

Use only these final delta dispositions:

| Final disposition | Meaning |
| --- | --- |
| `PORT` | Apply the template intent substantially as released. |
| `ADAPT` | Apply the new intent while preserving instance identity, governance, configuration, or knowledge. |
| `SKIP` | Explicitly decide not to adopt the reviewed template change. This is final and must have a rationale. |
| `ALREADY_PRESENT` | Equivalent intent already exists in the instance; cite evidence. |

An unresolved row is not a fifth disposition: leave its disposition blank or mark it pending review in a separate issue/gate field. It keeps the review open. `SKIP` is final; once all rows are final and required work/validation is complete, it may coexist with reconciliation.

## Metadata

Instances create `TEMPLATE_BASELINE.md` and `TEMPLATE_UPGRADES.md` at specialization; see [SPECIALIZATION.md](SPECIALIZATION.md) for the baseline shape.

- **Generated from** is the immutable release and exact commit from which the instance was created. It never advances.
- **Last reviewed** is the newest exact template release against which the complete delta has been evaluated. It may advance while work remains open.
- **Reconciled through** is the newest exact template release for which every applicable delta since the previous reconciliation point has a final disposition, all required instance changes are merged, and required validation is complete. It means accounted for, not identical.

For example, an instance may truthfully state `Generated from: v0.2.0`, `Last reviewed: v0.4.0`, and `Reconciled through: v0.3.0` while the v0.4 review has unresolved or unmerged work. A final documented `SKIP` can still allow the reconciliation point to advance.

Keep `TEMPLATE_BASELINE.md` small. Put review history in cumulative `TEMPLATE_UPGRADES.md`, with one section per review:

```markdown
## Review <old release> -> <new release> — <YYYY-MM-DD>

- Previous reconciliation point: <release> (`<commit>`)
- Reviewed release: <release> (`<commit>`)
- Review result: OPEN | CLOSED | CLOSED_WITH_DEVIATIONS
- Resulting reconciliation point: <release and commit, or unchanged>
- Review change: <PR and/or merge commit>

| Template change | Ownership | Disposition | Instance action | Issue / Owner gate | Rationale / evidence |
| --- | --- | --- | --- | --- | --- |
```

`OPEN`, `CLOSED`, and `CLOSED_WITH_DEVIATIONS` describe the whole review, not a delta disposition. A closed review with one or more `SKIP` rows is `CLOSED_WITH_DEVIATIONS`; no JSON/YAML companion manifest is needed or permitted by this contract.

## Vault review rules

- `templates/` blank note forms, generic docs, and `scripts/validate_template.py` are reusable template contract. Port additions or adapt local extensions without treating an instance validator as a migration tool.
- Existing notes in `inbox/`, `concepts/`, `literature/`, `methods/`, `projects/`, `maps/`, and `bibliography/` are instance-owned. Never overwrite, delete, or normalize them just because a form or template convention changed.
- Existing `terminology/` term notes are instance-owned. The blank term form and generic terminology guidance are template-owned review candidates; do not overwrite populated terms or silently change their preferred wording.
- Root README and AGENTS require specialization-aware review. Preserve instance identity and local authority; do not restore template title, quick-start, or broaden governance implicitly.
- `.obsidian/app.json`, `.obsidian/appearance.json`, and `.obsidian/core-plugins.json` are specialized configuration after use. Review a changed default as a suggestion; do not silently replace a legitimate local choice.
- `.gitignore` and `.gitattributes` are specialized safety/portability rules. Merge new generic intent semantically while preserving local exclusions and attributes.
- `.gitkeep` files, template identity, and consumed onboarding material are bootstrap-only. Do not re-add them where they no longer serve a purpose.

## Review sequence and stop conditions

1. Verify the admitted instance, known-clean state, current metadata, local governance, and exact old/new template commits.
2. Inventory the complete old-to-new template delta, including additions, deletions, renames, mode changes, validator changes, and documentation semantics.
3. Classify each coherent delta by its current lifecycle role and record it in the cumulative table.
4. Implement only finalizable `PORT` and `ADAPT` changes on a review branch. Preserve instance-owned state and document every `SKIP` or `ALREADY_PRESENT` claim with evidence.
5. Run instance-appropriate validation and preservation assertions. A generic template validator is not proof that an instance upgrade is complete.
6. Advance `Reconciled through` only after every applicable row is final, required changes are merged, and required validation is complete. If any row is unresolved, keep the review open and leave reconciliation unchanged.

Stop and leave the review open when exact releases cannot be proven, the full delta is not inventoried, instance state is unexplained, a required Owner decision is unresolved, preservation checks fail, or a proposed change requires data migration, a custom merge engine, or automation outside this contract.

Owner review is required for changes to instance identity, legal posture, local AGENTS authority, safety/storage/provenance boundaries, explicit Owner-adopted state, or a normative-policy `SKIP`.
