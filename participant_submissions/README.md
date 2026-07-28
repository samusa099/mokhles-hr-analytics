# Participant Submissions

This directory is reserved for participant solutions to the **Mokhles Group Rajshahi Expansion Crisis** case.

## Submission branch policy

Participant work must **not** be merged directly into `main`.

All participant pull requests must target the dedicated branch:

```text
submissions
```

Pull requests that modify `participant_submissions/**` while targeting `main` are rejected by the repository policy workflow.

## Required folder structure

Create one folder using the following naming convention:

```text
participant_submissions/<github-username>/
```

Example:

```text
participant_submissions/example-user/
├── README.md
├── executive_memo.pdf
├── analytical_report.pdf
├── dashboard/
│   ├── dashboard.pbix
│   └── dashboard_preview.png
├── data_model/
│   └── relationship_diagram.png
├── kpi_dictionary.csv
├── evidence_register.csv
├── notebook/
│   └── analysis.ipynb
└── supporting_files/
```

Do not place submissions at the repository root.

## Required deliverables

Each participant submission must contain:

1. `README.md` — solution summary, decision and navigation;
2. executive decision memo;
3. analytical report;
4. dashboard or dashboard preview;
5. data-model diagram;
6. KPI dictionary;
7. evidence register;
8. analysis notebook or reproducible script, where applicable.

## Data rules

Participants must:

- use only the existing Mokhles Group project datasets;
- preserve the synthetic-data declaration;
- avoid external salary, labour-market or economic data;
- avoid fabricated records and unsupported assumptions;
- state `Insufficient evidence to conclude` where required;
- keep raw source files unchanged;
- avoid committing credentials, tokens, personal data or executable binaries unrelated to the case.

## Pull request title

Use:

```text
submission: <github-username> — Rajshahi expansion case
```

## Review standard

Submissions are reviewed for:

- data quality and grain accuracy;
- KPI correctness;
- controlled Dhaka–Rajshahi comparison;
- root-cause reasoning;
- evidence classification;
- limitation disclosure;
- management recommendation;
- reproducibility and repository hygiene.

## Main-branch restriction

The `main` branch contains the canonical project, datasets, documentation, validation logic and release assets. Participant work is intentionally isolated so that the official project remains clean and stable.
