# Contributing to the template

Open an issue or pull request for reusable template defects and documentation improvements. Keep research content, credentials, private paths, Zotero attachments, and generated output out of the public template. Actual research repositories are outside this template's review scope.

State the proposed change, the released baseline, any contract it affects, and how you validated it. Run `python scripts/validate_template.py`; for pair changes, also check the Design Lab contract at exact heads. Attach only synthetic or cleared evidence. A passing validator does not establish scientific validity or admit a research interpretation.

The source repository's CI checks this public template on Windows and Linux. It runs only in `JerrySkywalker/research-vault-template`; a repository created from the template should replace or remove the inherited source-template workflow when it defines its own checks. For versioned pair releases, follow [the maintainer release procedure](docs/RELEASING.md).
