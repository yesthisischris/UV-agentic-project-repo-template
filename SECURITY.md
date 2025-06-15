# Security Policy

## Supported Versions

We support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 0.9.x   | :white_check_mark: |
| < 0.9   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability, please follow these steps:

1. **Do not** open a public GitHub issue
2. Email us at admin@umbraversa.com with:
   - A clear description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Any suggested fixes (if you have them)

## Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Varies based on severity, typically 14-30 days

## Security Best Practices

When using this template:

1. Keep all dependencies up to date
2. Use environment variables for API keys and secrets
3. Never commit sensitive information to version control
4. Use the provided `.env.example` as a template
5. Follow the principle of least privilege for API access

## Disclosure Policy

Once a vulnerability is fixed, we will:

1. Release a patch version
2. Update the security advisory
3. Credit the reporter (if desired)
4. Document the fix in our changelog
