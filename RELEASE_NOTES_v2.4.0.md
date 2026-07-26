# Mokhles Group HR Analytics v2.4.0

## Release theme

**Runtime Compatibility, Dependency Modernisation and Deployment Readiness**

This release closes the most important deployment-readiness gap identified during the principal engineering review: the repository now tests the installed Python package and data-processing workflow across supported Python versions instead of relying only on static security and repository-integrity scans.

## Highlights

### Python runtime compatibility gate

A new GitHub Actions workflow validates the project on:

- Python 3.11
- Python 3.12
- Python 3.13

Each matrix job:

- installs the repository as an editable package;
- runs `pip check`;
- imports pandas, matplotlib, openpyxl and nbformat;
- executes package-level CSV and Excel loader tests;
- verifies CSV path-traversal rejection;
- runs repository security and integrity validation;
- rebuilds the BI-ready layer;
- confirms that all 15 generated BI-ready CSV files are present and non-empty;
- treats dependency `FutureWarning` signals as test failures.

### Dependency upgrades

The release includes the reviewed Dependabot upgrades:

- pandas `>=3.0.5`
- matplotlib `>=3.11.1`
- openpyxl `>=3.1.5`
- nbformat `>=5.10.4`
- setuptools `>=83.0.0`
- `actions/setup-python` v7 pinned to an immutable commit SHA
- `gitleaks/gitleaks-action` v3 pinned to an immutable commit SHA

### Security posture

The repository continues to enforce:

- read-only GitHub Actions permissions;
- immutable action references;
- CodeQL analysis;
- dependency vulnerability auditing;
- full-history secret scanning;
- CSV formula-injection checks;
- passive notebook validation;
- bounded and passive XLSX archive validation;
- path-containment checks for repository resources.

## Engineering impact

Before v2.4.0, dependency upgrades could pass the repository validator without proving that the installed package, pandas loaders, Excel reader or BI transformation still worked. v2.4.0 adds that missing execution-level evidence.

## Included pull requests

- #3 — Gitleaks Action v3
- #4 — setup-python v7
- #5 — nbformat 5.10.4
- #6 — matplotlib 3.11.1
- #7 — openpyxl 3.1.5
- #8 — pandas 3.0.5
- #9 — setuptools 83.0.0
- #10 — Python runtime compatibility matrix

## Validation

The runtime matrix completed successfully for Python 3.11, 3.12 and 3.13. Package installation, dependency validation, loader tests, security validation and BI transformation smoke tests passed in each matrix job.

## Upgrade

```bash
git pull origin main
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

## Data and licensing

All HR records remain synthetic and suitable for learning, demonstration and portfolio use. Dataset and documentation licensing remain CC BY 4.0; Python code remains MIT licensed.

## Maintainer

**Musa**
