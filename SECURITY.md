# Security Policy

## Scope

This repository contains reusable analysis instructions and a report template. It must not contain product credentials, browser state, cookies, tokens, passwords, private keys, authorization headers, private customer evidence, or personally identifying source material.

## Safe use

- Keep product inspection read-only unless the product owner explicitly authorizes a specific mutation.
- Do not commit screenshots, chat exports, private workspace URLs, account identifiers, or generated evidence ledgers without reviewing their access level and redacting sensitive information.
- Store credentials in the operating system credential manager or an approved secret manager, never in this repository.
- Treat output reports as potentially sensitive because they may contain private product behavior, project assets, model settings, billing information, or user content.
- Before publishing a derived report, scan both the working tree and Git history for secrets and private identifiers.

## Reporting a security issue

Do not disclose secrets or private evidence in a public issue. Use GitHub private vulnerability reporting when it is available for this repository. For non-sensitive documentation issues, open a regular GitHub issue without including private product data.
