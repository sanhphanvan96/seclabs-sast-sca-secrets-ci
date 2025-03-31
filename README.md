# Security Scanning CI Pipeline Labs: SAST, SCA, Secrets, and Container Security


[![POC](https://img.shields.io/badge/POC-Success-success)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Learn](https://img.shields.io/badge/Learn-Success-success)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Fun](https://img.shields.io/badge/Fun-100%25-brightgreen)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)
[![Code](https://img.shields.io/badge/Code-Quality-blue)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions)

[![SAST](https://img.shields.io/badge/SAST-YES-red)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-SAST.yml)
[![Secrets](https://img.shields.io/badge/Secrets-YES-yellow)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-Secrets.yml)
[![SCA](https://img.shields.io/badge/SCA-YES-red)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-SCA.yml)
[![Container](https://img.shields.io/badge/Container-YES-orange)](https://github.com/sanhphanvan96/seclabs-sast-sca-secrets-ci/actions/workflows/Scan-All-Container.yml)

Welcome to **Security Scanning CI Pipeline Labs**!


This project demonstrates how to integrate **free and open-source security scanning tools** (SAST, SCA, secrets detection, and container security) into your **CI/CD pipelines** using **GitHub Actions**. Ideal for learning **DevSecOps best practices**, testing tools, and building secure workflows.

## 🛡️ Security Scans Included

### Secrets Detection
- [Gitleaks](https://github.com/gitleaks/gitleaks) - Scan Git history for leaked credentials.
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) - High-accuracy secrets detection.
- [GitGuardian](https://github.com/GitGuardian) - Real-time secrets monitoring.

### SAST (Static Application Security Testing)
- [Semgrep](https://github.com/semgrep/semgrep) - Lightweight, fast static analysis.
- [CodeQL](https://codeql.github.com/) - Deep code analysis by GitHub.

### SCA (Software Composition Analysis)
- [OWASP Dependency Check](https://github.com/dependency-check/DependencyCheck) - Detect vulnerable libraries.
- [Trivy](https://github.com/aquasecurity/trivy) - Comprehensive dependency scanning.
- [Grype](https://github.com/anchore/grype) - Fast vulnerability scanning.

### Container Security
- [Trivy](https://github.com/aquasecurity/trivy) - Scan container images for vulnerabilities.
- [Dockle](https://github.com/goodwithtech/dockle) - Best practices for Docker images.

## 🚀 Quick Start

Run all security scans with a single command:

```bash
# Run all security scans
gh workflow run Scan-All.yml
```

## ⚠️ Important Notes

- This repository contains **intentionally vulnerable code** for testing purposes.
- **DO NOT deploy this code in production environments.**
- Ideal for learning, testing, and demonstrating **security scanning tools**.
- All scans can be executed individually or as part of composite workflows.

## 🔍 Workflow Structure

- `Scan-All.yml` - Runs all security scans
- `Scan-All-SAST.yml` - Runs only SAST tools
- `Scan-All-SCA.yml` - Runs only SCA tools
- `Scan-All-Secrets.yml` - Runs only secret detection
- `Scan-All-Container.yml` - Runs container security scans

## 🌟 Why Use This Project?

- Learn how to integrate **security scanning tools** into your **CI/CD pipelines**.
- Explore best practices for **DevSecOps**.
- Test and evaluate the effectiveness of various **security tools**.

## 📋 TODO
- Add more popular free tools.
- Optimize workflows for faster execution and reduced resource usage.
- Integrate SonarQube Community Edition for static code analysis.

## 📝 License

MIT
