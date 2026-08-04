# Analytics Workflows

## Standard analytical workflow

1. Define the business decision.
2. Select the correct population and reporting period.
3. Confirm each source table's grain.
4. Review definitions and validation rules.
5. Run repository validation.
6. Build the required analytical layer.
7. Calculate KPIs and cross-check material results.
8. Segment findings by department, location, role or time.
9. Separate confirmed findings from inference and hypothesis.
10. Produce a decision-focused report with limitations and next actions.

## Reproducible command sequence

```bash
python scripts/validate_repository.py
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
python scripts/profile_data.py
python -m unittest discover -s tests -v
```

## Data-quality workflow

Review:

```text
data/data_quality/table_quality_summary.csv
data/data_quality/column_profile.csv
data/data_quality/validation_rules.csv
```

Check for:

- required-field completeness;
- duplicate business keys;
- invalid dates or reporting periods;
- inconsistent category labels;
- impossible negative counts or amounts;
- rates outside their valid range;
- broken employee, department, location or date relationships;
- unexpected row-count changes after transformations.

## Evidence classification

Use four evidence levels in analytical reports:

| Level | Meaning |
|---|---|
| Confirmed finding | Directly demonstrated by valid project data |
| Supported inference | Reasonable interpretation supported by several observations |
| Unproven hypothesis | Plausible explanation requiring additional evidence |
| Unsupported claim | Not demonstrated by available project data |

## Decision-focused reporting

A useful HR report should answer:

- **What happened?** State the result and magnitude.
- **Where did it happen?** Identify affected location, department, cohort or period.
- **What may explain it?** Present drivers with evidence strength.
- **Why does it matter?** Connect the finding to workforce or business risk.
- **What should happen next?** Recommend a bounded action or monitoring point.

## Recommended portfolio analyses

- Workforce composition and headcount movement
- Hiring funnel and recruitment-source efficiency
- Voluntary versus involuntary turnover
- Leave usage and absence concentration
- Diversity representation by level and department
- Training participation, assessment improvement and cost
- Compensation positioning and compa-ratio distribution
- Performance distribution and promotion readiness
- Workplace safety trends and corrective-action closure
- Department-level operating model comparison

## Analytical safeguards

- Never infer causation from a simple correlation.
- Avoid joining two transaction tables directly without a bridge or aggregated layer.
- Reconcile totals before and after every major transformation.
- Preserve zero values where they are meaningful.
- Explain missing data rather than silently dropping records.
- Use human-readable business labels in reports, while preserving technical field names in metadata.
