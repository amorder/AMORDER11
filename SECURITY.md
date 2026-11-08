# Security Policy

## Public repository scope

AMORDER11 is a public content-publishing repository. Treat every committed file, asset, storyboard, issue, pull request, branch, commit, Git history entry and workflow log as public information. Anyone can clone or download public content. Deleting a file in a later commit does not remove it from earlier Git history, forks, backups or caches.

The trading application, trading strategy, private research and operational data belong in the separate private repository amorder/AMORDER. The renderer scripts currently present under tools/ and the workflows under .github/workflows/ are public and may be copied. Do not place proprietary implementation here.

## Never commit

- API keys, private keys, passwords, access tokens, session cookies, OAuth credentials or credential exports.
- Buffer, Alpaca, Hugging Face, GitHub or personal credentials.
- Trading engine code, strategy rules/parameters, candidate scans, symbol-specific research or private renderer implementation.
- Raw market or broker payloads, account/order identifiers, balances, positions, fills, trade-by-trade records, statements, P&L/performance statistics, private journals or internal logs.
- Unpublished videos, raw footage, personal information or any data not explicitly approved for public release.
- Local environment files, database files, model credentials, logs, caches or temporary exports.

Commit only reviewed public post copy, public source links, approved final creative assets and public-safe publishing status. Never put secrets in Markdown, JSON, workflow logs, commit messages or issue comments.

Any content describing a paper-trading experiment must clearly label it as simulated activity—not live-money performance, investment advice or a guarantee of returns. Do not publish confidential strategy thresholds or internal system outputs.

## Workflow security

- Workflows must use the minimum permissions required. The render workflows need contents: write only to commit generated media to this repository; do not add broker, Buffer or personal credentials to them.
- The secret-guard workflow is read-only and scans the full Git history as well as current tracked files.
- Do not add pull_request_target or workflow_run jobs that execute untrusted pull-request code with write permissions or secrets.
- Do not print environment variables, credentials, request headers or full broker/API responses in logs.
- Keep Actions default token permissions read-only. Grant write permissions only in a workflow that must commit a reviewed public asset.
- Keep third-party actions current and review Dependabot updates before merging.

## Required owner-side GitHub settings

The repository files cannot enforce these controls on their own. In GitHub repository Settings, configure:

1. Branch protection for main: require a pull request, at least one approving review, code-owner review, dismissal of stale approvals, and the secret-guard status check. Require conversations to be resolved. Disable force pushes and branch deletion.
2. Code security and analysis: enable secret scanning and push protection when available for this account/repository.
3. Actions: set the default GITHUB_TOKEN permission to read-only and restrict which Actions are allowed.
4. Security: enable private vulnerability reporting if the setting is available.
5. Account access: use two-factor authentication or a passkey for the owner account, and remove unneeded collaborators or tokens.

The .github/CODEOWNERS file assigns ownership to @amorder, but it does not force approvals unless the main branch protection rule enables required code-owner review.

## If a secret is exposed

1. Revoke or rotate the credential immediately. Assume it was copied.
2. Identify every service and workflow that used it; review activity and access logs.
3. Remove the value from the current files and, where appropriate, rewrite Git history and invalidate related caches/artifacts. A normal delete commit is not sufficient.
4. Re-run the full-history secret scan and verify the credential no longer works.
5. Record the remediation without publishing the secret or sensitive incident details.

## Reporting a vulnerability

Please do not post credentials or sensitive vulnerability details in a public issue. Use GitHub's private vulnerability reporting / Security Advisories feature when available. If it is not enabled, contact the repository owner privately through GitHub before sharing exploit details.

The owner will review reports, rotate exposed credentials, remove affected public content where possible, and document remediation without publishing sensitive details.
