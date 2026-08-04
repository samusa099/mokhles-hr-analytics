# Getting Started

## Prerequisites

- Git
- Python 3.11 or newer
- A virtual environment
- JupyterLab for notebook exploration
- Optional: Power BI Desktop, Excel, Tableau, Qlik, Metabase or a SQL database

## Clone and install

```bash
git clone https://github.com/samusa099/mokhles-hr-analytics.git
cd mokhles-hr-analytics
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m pip install -e .
```

### macOS or Linux

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Validate the repository

Run the automated checks before analysis:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

## Build generated analytical layers

```bash
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
python scripts/profile_data.py
```

Expected outputs include:

- `data/bi_ready_csv/` — normalized dimensions and fact tables
- `data/analysis_ready/` — Employee 360 and Department 360 files
- `data/data_quality/` — table profiles, field profiles and validation rules

## Open the exploratory notebook

```bash
jupyter lab notebooks/Mokhles_HR_Analytics_EDA.ipynb
```

## Fastest routes by objective

| Objective | Start with |
|---|---|
| Quick employee analysis | `data/analysis_ready/employee_360_fy2025.csv` |
| Department comparison | `data/analysis_ready/department_360_summary_fy2025.csv` |
| Power BI star schema | `data/bi_ready_csv/` |
| Original operational-style records | `data/csv/` |
| Excel analysis | `data/excel/` |
| Data-quality review | `data/data_quality/` |
| Advanced business case | `docs/case_studies/RAJSHAHI_EXPANSION_CRISIS.md` |

## Refresh sequence

Whenever authoritative source files change, use this order:

1. Validate source files.
2. Rebuild the BI-ready layer.
3. Rebuild analysis-ready files.
4. Regenerate quality profiles.
5. Run tests again.
6. Refresh connected dashboards.

```bash
python scripts/validate_repository.py
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
python scripts/profile_data.py
python -m unittest discover -s tests -v
```

## Common safeguards

- Never combine tables without confirming their grain.
- Treat `data/csv/` as the authoritative analytical source.
- Do not edit generated BI files manually when they can be rebuilt.
- Keep employee IDs and relationship keys as text.
- Format stored decimal rates as percentages only in the reporting layer.
- State clearly that the project contains synthetic data.
