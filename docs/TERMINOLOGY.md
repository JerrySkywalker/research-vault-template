# Canonical terminology

## Authority and form

The Vault owns reviewed cross-project canonical terminology. A project Design Lab owns its local terms. A term can remain local forever. A canonical term is one `terminology/<descriptive-slug>.md` note, with preferred English and Chinese wording in the same front matter. Descriptive path and Git revision are its identity; do not invent a global term ID.

Use the [term form](../templates/term.md). The structured fields are `type: term`, `status: active` or `deprecated`, `preferred_en`, `preferred_zh`, and lists `abbreviations`, `aliases_en`, `aliases_zh`. Keep the technical definition, domain, sources, translation rationale, discouraged wording and optional first-use wording in Markdown. An alias is a recognized alternate form; a discouraged form is named with a reason in wording guidance and should not silently become a preferred form. Abbreviations are explicit, never inferred from initials.

If first-use guidance is present, follow it for publications. Otherwise use the preferred forms and an explicitly listed abbreviation as appropriate; the term does not impose a universal paper format. Terms without a useful abbreviation may leave the list empty.

## Admission and change

Review a candidate for cross-project value, existing equivalent terms, both translations, definition boundaries and source provenance. Use the existing [promotion workflow](PROMOTION_WORKFLOW.md) and a reviewable Git change. Admission creates or updates a canonical note; it never automatically changes a project. Record a promoted term's originating project repository, note path, and review commit or PR in provenance. Retain the original project note and context.

Change a preferred translation or definition in a reviewed Git commit. A Lab or publication needing reproducibility can retain the full Vault commit it used. Current readers may use the current note; historical readers can inspect the earlier commit. Do not copy full canonical definitions into Labs solely for this purpose.

For retirement, retain the note and history, set `status: deprecated`, and explain the successor or reason in the body. A discouraged variant of an otherwise active term does not deprecate the whole term.

## Lab references

A Lab note may record the Vault repository URL or stable identity and `terminology/<slug>.md`, plus the full Git commit used where exact provenance matters. These are ordinary human-readable fields, not a runtime lookup protocol. A Lab remains valid offline when navigation to the Vault is unavailable. Promotion and later reference updates are explicit reviews, with no automatic synchronization.
