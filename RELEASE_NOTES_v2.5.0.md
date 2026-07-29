# Mokhles Group HR Analytics v2.5.0

## Release theme

**Governance, Security Hardening and Advanced Case-Study Readiness**

v2.5.0 promotes the repository from a validated analytics portfolio into a more complete learning and contribution environment. It adds a high-difficulty workforce-transformation case, an isolated participant-submission workflow, stronger repository security controls, updated analysis dependencies and a corrected Git structure.

## Highlights

### Advanced Rajshahi expansion case

A new high-difficulty case study asks participants to determine whether the Rajshahi operation is failing or whether Mokhles Group is applying the wrong workforce operating model to a new location.

The case requires participants to:

- use only the existing synthetic project data;
- control for workforce size, department mix, job level, tenure and hiring intensity;
- prevent duplicate counting across one-to-many HR tables;
- classify findings as confirmed, inferred, unproven or unsupported;
- choose Continue, Pause or Redesign;
- recommend exactly three evidence-supported interventions.

### Participant submission governance

The repository now includes:

- a dedicated `participant_submissions/` workspace;
- a participant submission guide and template;
- a pull-request template for case submissions;
- a target-policy workflow that prevents participant solution folders from being merged directly into `main`;
- documented main-branch and submissions-branch governance.

Participant solutions must target the permanent `submissions` branch.

### Portfolio security hardening

A consolidated Portfolio Security workflow now performs:

- blocked-file and path-containment checks;
- symlink safety validation;
- bounded XLSX archive inspection;
- notebook command-policy checks;
- CSV formula-injection detection;
- immutable GitHub Action reference validation;
- checksum-verified Gitleaks scanning;
- dependency auditing;
- pull-request dependency review;
- Python CodeQL analysis with extended security queries.

### Repository integrity correction

The malformed nested Git gitlink was removed. It had no matching `.gitmodules` entry and caused `actions/checkout` to fail during submodule cleanup. Removing it restored normal CI checkout without changing the project datasets or analytical assets.

### Dependency modernisation

The supported analysis environment now requires:

- NumPy `>=2.4.6`
- JupyterLab `>=4.6.2`
- pandas `>=3.0.5`
- matplotlib `>=3.11.1`
- openpyxl `>=3.1.5`
- nbformat `>=5.10.4`

## Included pull requests

- #12 — NumPy requirement update
- #13 — JupyterLab requirement update
- #17 — Rajshahi expansion case and participant workflow
- #18 — corrected portfolio security hardening
- #19 — accidental nested Git submodule correction

## Validation evidence

The final structural correction was validated by successful:

- Portfolio Security;
- CodeQL Security Scan;
- Secret Exposure Scan;
- Repository Data Quality and Security;
- Participant Submission Target Policy.

The Python runtime compatibility gate from v2.4.0 remains active for Python 3.11, 3.12 and 3.13.

## Upgrade

```bash
git pull origin main
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/validate_repository.py
python scripts/build_bi_ready_layer.py
```

## Data and licensing

No real employee, applicant, payroll or organisational records are included. The project remains a fully synthetic Bangladesh HR analytics portfolio.

- Dataset and documentation: CC BY 4.0
- Python code and notebook utilities: MIT

## Maintainer

**Musa**
