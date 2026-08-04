# BI and Platform Guides

## Power BI

Use `data/bi_ready_csv/` with the relationship map and theme under `bi_assets/`.

Recommended report pages:

1. Executive Overview
2. Workforce and Diversity
3. Recruitment
4. Retention and Leave
5. Learning and Performance
6. Compensation and Safety

Model rules:

- one-to-many dimension-to-fact relationships;
- single-direction filters by default;
- one active date relationship per fact;
- mark the date dimension as the date table;
- store relationship keys as text;
- format decimal rates as percentages.

Theme:

```text
bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json
```

Relationship and dashboard assets:

```text
bi_assets/semantic_model/relationship_map.csv
bi_assets/semantic_model/dashboard_blueprint.csv
```

## Excel

Recommended tools:

- Power Query for importing and standardizing files
- Data Model / Power Pivot for relationships
- PivotTables for controlled aggregation
- Measures for headcount, hiring, turnover and payroll
- Slicers for department, location, period and employee segment

Use Employee 360 for quick analysis and BI-ready tables for a relational workbook.

## Python

Use pandas for profiling, validation, joins and reproducible KPI calculation. Start with:

```bash
jupyter lab notebooks/Mokhles_HR_Analytics_EDA.ipynb
```

Recommended pattern:

1. Load the minimum required tables.
2. Assert expected columns and grain.
3. Standardize dates and categorical values.
4. Reconcile row counts and totals.
5. Calculate KPIs in reusable functions.
6. Save derived outputs with explicit names and periods.

## SQL

The BI-ready layer supports:

- dimensional joins;
- grouped KPI calculations;
- common table expressions;
- window functions;
- cohort and ranking analysis;
- reusable departmental or monthly views.

Load IDs as text and inspect source grain before joining tables.

## Tableau, Qlik and Metabase

Use the same dimensional principles as Power BI. Prefer the normalized BI-ready tables, define shared date/employee/department/location relationships and calculate KPIs centrally to prevent report-level inconsistency.

## Looker Studio

For simple portfolio dashboards, use Employee 360 or Department 360. For more complex relational modeling, prepare a consolidated SQL view or governed analytical extract first.

## Dashboard design standard

Every page should have:

- a clear management question;
- a small set of headline KPIs;
- one or two explanatory visuals;
- relevant segmentation controls;
- a concise interpretation or decision cue;
- definitions for rates and denominators.

Avoid decorative charts that do not support a decision.
