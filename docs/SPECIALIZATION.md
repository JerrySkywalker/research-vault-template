# Specializing an instance

An instance is an independent knowledge repository, not a branded copy that tracks this template automatically.

## Replace

An instance MUST replace the repository title, opening description, example organization or remote references, and any template-specific identity. It MUST create `TEMPLATE_BASELINE.md` at the root, naming the source template, adopted version or commit, adoption date, and instance-specific deviations.

## Keep and adapt

An instance SHOULD retain generic operating guidance that is still true: ownership boundaries, logical asset references, Zotero custody, the promotion workflow, and minimal Obsidian policy. It SHOULD adapt examples, project links, and local governance to its own identity. It MUST NOT retain awkward template branding alongside its actual identity.

Template changes arrive only through an explicit, reviewable branch or PR. `TEMPLATE_BASELINE.md` records provenance; it is not an automatic synchronization mechanism.
