# KPI Library

## Workforce

```text
Beginning Headcount = Ending Headcount - Hires + Separations
Average Headcount = (Beginning Headcount + Ending Headcount) / 2
Headcount Growth % = (Ending Headcount - Beginning Headcount) / Beginning Headcount × 100
Hiring Rate % = Hires / Average Headcount × 100
Turnover Rate % = Separations / Average Headcount × 100
Retention Rate % = 100 - Turnover Rate %
```

FY2025 portfolio example:

```text
Beginning headcount = 456 - 96 + 60 = 420
Average headcount = (420 + 456) / 2 = 438
Growth = (456 - 420) / 420 = 8.57%
Hiring rate = 96 / 438 = 21.92%
Turnover rate = 60 / 438 = 13.70%
```

## Recruitment

```text
Time to Fill = Filled Date - Requisition Open Date
Time to Hire = Accepted Date - Application Date
Offer Acceptance % = Accepted Offers / Offers Issued × 100
Cost per Hire = Total Recruitment Cost / Number of Hires
Selection Ratio % = Hires / Applicants × 100
```

## Leave and absence

```text
Leave Utilisation % = Leave Days Used / Leave Days Available × 100
Absence Rate % = Unplanned Absence Days / Available Workdays × 100
Average Leave Duration = Total Leave Days / Leave Transactions
```

## Learning and development

```text
Training Participation % = Employees Trained / Eligible Employees × 100
Average Training Hours = Total Training Hours / Participants
Assessment Improvement = Post-assessment Score - Pre-assessment Score
Training ROI % = (Estimated Benefit - Training Cost) / Training Cost × 100
```

## Compensation

```text
Compa-ratio = Employee Salary / Salary-band Midpoint
Payroll per Employee = Total Payroll / Average Headcount
Benefit Cost Ratio = Benefit Cost / Gross Payroll
Pay Gap % = (Reference-group Pay - Comparison-group Pay) / Reference-group Pay × 100
```

## Performance

```text
Average Performance Score = Sum of Scores / Evaluations
High Performer % = High Performers / Evaluated Employees × 100
Promotion-readiness % = Promotion-ready Employees / Evaluated Employees × 100
Goal Completion % = Completed Goals / Assigned Goals × 100
```

## Health and safety

```text
Incident Rate = Recordable Incidents / Exposure Base
Lost-time Incident Rate = Lost-time Incidents / Exposure Base
Average Lost Days = Lost Workdays / Lost-time Incidents
Corrective-action Closure % = Closed Actions / Actions Raised × 100
```

## KPI controls

For every published KPI, document:

- numerator and denominator;
- population and exclusions;
- reporting period;
- grain and aggregation method;
- whether the value is stored or calculated;
- cross-check result in Python, Excel, SQL or Power BI.

Do not compare rates unless their denominators and time windows are aligned.
