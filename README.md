# Security Scanning CI Pipeline Demo

A demonstration project showcasing various security scanning tools integrated into GitHub Actions workflows for Python applications.

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
