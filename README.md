# Security Scanning CI Pipeline Demo


[![POC](https://img.shields.io/badge/POC-Success-success)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Learn](https://img.shields.io/badge/Learn-Success-success)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Fun](https://img.shields.io/badge/Fun-100%25-brightgreen)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Code](https://img.shields.io/badge/Code-Quality-blue)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)

A demonstration project showcasing various security scanning tools integrated into GitHub Actions workflows for Python applications.

[![SAST](https://img.shields.io/badge/SAST-YES-red)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-SAST.yml)
[![Secrets](https://img.shields.io/badge/Secrets-YES-yellow)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-Secrets.yml)
[![SCA](https://img.shields.io/badge/SCA-YES-red)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-SCA.yml)
[![Container](https://img.shields.io/badge/Container-YES-orange)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-Container.yml)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)

## 🛡️ Security Scans Included

- **Secrets Detection**
  - Gitleaks
  - TruffleHog
  - GitGuardian

- **SAST (Static Application Security Testing)**
  - Semgrep
  - CodeQL

- **SCA (Software Composition Analysis)**
  - OWASP Dependency Check
  - Trivy
  - Grype

- **Container Security**
  - Trivy
  - Dockle

## 🚀 Quick Start

```bash
# Run all security scans
gh workflow run Scan-All.yml
```

## ⚠️ Important Notes

- This project contains intentionally vulnerable code for testing security tools
- DO NOT use this code in production
- Perfect for learning and testing security scanning tools
- All scans can be run individually or together via composite workflows

## 🔍 Workflow Structure

- `Scan-All.yml` - Runs all security scans
- `Scan-All-SAST.yml` - Runs only SAST tools
- `Scan-All-SCA.yml` - Runs only SCA tools
- `Scan-All-Secrets.yml` - Runs only secret detection
- `Scan-All-Container.yml` - Runs container security scans

## 📝 License

MIT
