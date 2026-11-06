# Security Policy

## Scope

This repository is public. Treat every committed file, issue, pull request, workflow log, and asset as public information. AMORDER11 is for content operations only, not trading or research operations.

## Never commit

- Alpaca API keys, secrets, access tokens, passwords, `.env` files, or credential exports.
- Buffer, Hugging Face, or GitHub tokens.
- Trading code, strategy rules, candidate scans, symbol-specific research, or internal source code.
- Raw market or broker payloads, account identifiers, order identifiers, balances, positions, fills, trade-by-trade records, statements, P&L/performance statistics, private journals, or internal logs.
- Personal or sensitive data that is not intentionally approved for public release.

Commit only reviewed public post copy, source links, approved creative assets, and publishing status metadata. Do not put account-level or trade-level results in this repository. Any content describing a paper-trading experiment must clearly label it as simulated activity—not live-money performance, investment advice, or a guarantee of returns.

The existing GitHub Actions workflow is a read-only secret-pattern guard. Do not add publishing credentials or broker credentials to this public repository.

## Reporting a vulnerability

Please do not post credentials or sensitive vulnerability details in a public issue. Use GitHub's private vulnerability reporting / Security Advisories feature when available. If it is not enabled, contact the repository owner privately through GitHub before sharing exploit details.

## Response

The owner will review reports, rotate any exposed credentials, remove affected public content where possible, and document remediation without publishing sensitive details.
