# Dataset Catalog

## Portfolio snapshot

| Domain | Volume |
|---|---:|
| Employees represented | 516 |
| FY2025 year-end headcount | 456 |
| Hires | 96 |
| Separations | 60 |
| Recruitment requisitions | 110 |
| Leave transactions | 1,043 |
| Training participation records | 1,011 |
| Performance evaluations | 456 |
| Health and safety records | 120 |

## Choose the right layer

| Analytical need | Recommended asset |
|---|---|
| Understand original HR records | `data/csv/` |
| Create a relational BI model | `data/bi_ready_csv/` |
| Run quick employee-level analysis | `employee_360_fy2025.csv` |
| Compare departments | `department_360_summary_fy2025.csv` |
| Review quality and metadata | `data/data_quality/` |
| Build Excel reports | `data/excel/` |
| Use a structured download package | `packages/kaggle/structured_workspace/` |

## Business-question map

| Question | Primary table or layer |
|---|---|
| How many employees are active? | Employee Master / Employee 360 |
| Which departments are growing? | Monthly HR KPI / Department Annual Summary |
| How many employees were hired? | Monthly HR KPI / Recruitment |
| What is average time-to-fill? | Recruitment fact |
| Why are employees leaving? | Separations fact |
| Which department has high turnover? | Separations + employee/department dimensions |
| Which leave types are most common? | Leave transactions |
| Is workforce representation balanced? | Diversity and inclusion dimension |
| How much training was delivered? | Training and development fact |
| Did learning scores improve? | Training and development fact |
| Are salaries aligned with bands? | Compensation and benefits fact |
| Who may be promotion-ready? | Performance evaluation fact |
| What safety incidents occurred? | Health and safety fact |
| What should leadership review? | Quarterly Board KPI / Department 360 |

## Data-type guidance

| Field class | Recommended type |
|---|---|
| IDs and relationship keys | Text |
| Dates | Date |
| Counts, days and hours | Whole number |
| BDT amounts and costs | Decimal or fixed decimal |
| Rates | Decimal, displayed as percentage |
| Scores and ratings | Decimal number |

## Data dictionary

The repository documents 803 fields. Before calculating a KPI, confirm:

1. The field definition.
2. The table grain.
3. Whether blanks are valid.
4. The unit and reporting period.
5. The primary or relationship key.
6. Whether the field is a stored value or a derived metric.

## Responsible interpretation

This dataset is realistic but synthetic. Analytical findings demonstrate methods and decision logic; they are not claims about an actual employer or employee population.
