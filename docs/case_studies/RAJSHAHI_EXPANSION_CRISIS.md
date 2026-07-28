# Mokhles Group Rajshahi Expansion Crisis

## A High-Difficulty People Analytics and Workforce Transformation Case

<p align="center">
  <strong>Difficulty: 80% · Decision period: Q4 FY2025 · Forward horizon: Q1 FY2026</strong><br>
  <em>Use only the existing Mokhles Group datasets. External data and fabricated evidence are prohibited.</em>
</p>

---

## 1. Executive case summary

Mokhles Group is a fictional Bangladesh-based organisation whose established operation is centred in Dhaka. Over time, the Dhaka office developed a mature HR operating model supported by experienced managers, familiar recruitment channels, standard salary structures, recurring training practices, established reporting routines and relatively stable workforce processes.

To support business expansion, senior management established a new operational office in Rajshahi. The original assumption was simple: the Dhaka model could be copied into Rajshahi with only minor adjustments.

By Q4 FY2025, the expansion was producing contradictory signals. Rajshahi was hiring and building capacity, but management could not determine whether the workforce was becoming stronger or merely larger. Recruitment activity was high, some vacancies appeared difficult to fill, employee exits were occurring, training coverage was uneven, performance results varied, leave pressure appeared to be increasing and safety records raised questions about operational readiness.

Management initially blamed the location. The HR team blamed recruitment. Some managers blamed compensation. Others argued that Rajshahi was only experiencing the normal instability of a new office.

The organisation had no trusted analytical model capable of separating these explanations.

The central challenge is therefore not simply to compare Dhaka and Rajshahi. The real challenge is to determine whether Rajshahi is genuinely underperforming after controlling for workforce size, department mix, job level, employee tenure, hiring intensity and organisational maturity.

---

## 2. Strategic decision

Before Q1 FY2026, management must choose one of three options:

1. **Continue expansion** — maintain the current operating model and continue scaling.
2. **Pause expansion** — temporarily stop major hiring and growth until workforce instability is addressed.
3. **Redesign expansion** — continue the Rajshahi operation but change its recruitment, management, training, compensation or workforce structure.

The organisation cannot fund every possible intervention. The analyst must identify exactly **three priority actions** supported by the available data.

---

## 3. Musa's role

Musa is assigned as the **People Analytics and Workforce Transformation Analyst**.

His responsibility is not to defend management's original decision. His responsibility is to test it.

Musa must:

- validate the existing HR data;
- define the correct grain of each dataset;
- prevent duplicate counting across one-to-many tables;
- integrate workforce, hiring, exit, compensation, leave, training, performance and safety evidence;
- compare Dhaka and Rajshahi fairly;
- separate symptoms from root causes;
- challenge unsupported assumptions;
- rank intervention priorities;
- document limitations;
- deliver a decision-ready recommendation.

The analyst solving this case takes Musa's role.

---

## 4. Core analytical question

> Is Rajshahi a failing location, or is Mokhles Group using the wrong workforce operating model for a new location?

The analyst must determine whether the problem is primarily:

- structural;
- managerial;
- recruitment-related;
- compensation-related;
- training-related;
- performance-related;
- workload-related;
- safety-related;
- or a normal consequence of rapid expansion.

More than one factor may be present, but the final recommendation must identify the three most important and evidence-supported priorities.

---

## 5. Available data

Only the existing project data may be used:

- Employee Master;
- Monthly HR KPI;
- Department Annual Summary;
- Quarterly Board KPI;
- Recruitment Master;
- Employee Separations;
- Leave Transactions;
- Diversity and Inclusion;
- Training and Development;
- Compensation and Benefits;
- Performance Evaluation;
- Health and Safety;
- Employee 360;
- Department 360;
- BI-ready dimensions and facts;
- project metadata and data dictionaries.

### Prohibited inputs

The analyst may not use:

- external salary surveys;
- labour-market statistics;
- cost-of-living data;
- job portal information;
- regional economic indicators;
- external employee surveys;
- fabricated interviews;
- invented records;
- assumed values for missing fields.

Where evidence is insufficient, the required conclusion is:

> **Insufficient evidence to conclude.**

---

## 6. Evidence classification

Every material conclusion must be classified as one of the following:

| Classification | Meaning |
|---|---|
| **Confirmed finding** | Directly supported by the available data |
| **Supported inference** | Reasonably supported by multiple internal indicators |
| **Unproven hypothesis** | Plausible, but the data is insufficient |
| **Unsupported claim** | Not permitted because the evidence does not support it |

---

## 7. Required analytical stages

### Stage 1 — Data audit and trust assessment

The analyst must test:

- duplicate and missing employee IDs;
- inconsistent department and location names;
- conflicting employment status;
- separated employees still marked active;
- duplicate recruitment, leave or training records;
- missing or impossible dates;
- join dates after exit dates;
- missing compensation values;
- inconsistent job levels;
- unmatched employees, departments or managers;
- inconsistent Q4 totals.

The output must state which findings are reliable, partially reliable or unreliable.

### Stage 2 — Data model design

The analyst must define the grain of every table and explain how joins will avoid inflated counts.

| Dataset | Expected grain |
|---|---|
| Employee Master | One row per employee |
| Recruitment Master | One row per requisition or candidate event |
| Employee Separations | One row per separated employee |
| Leave Transactions | One row per leave transaction |
| Training and Development | One row per employee-training event |
| Performance Evaluation | One row per employee evaluation |
| Health and Safety | One row per incident or safety record |
| Monthly HR KPI | One row per month or month-location combination |

Directly joining multiple one-to-many tables without aggregation is prohibited.

### Stage 3 — Descriptive comparison

Compare Dhaka and Rajshahi across:

- workforce size and growth;
- department and job-level composition;
- employment type;
- hiring and separation;
- compensation;
- training;
- performance;
- leave;
- diversity;
- health and safety.

Raw totals alone are not acceptable. Rates, ratios and denominators are mandatory.

### Stage 4 — Controlled comparison

Test whether location differences remain after controlling for:

- department;
- job level;
- employee tenure;
- employment type;
- manager;
- hiring period;
- workforce size;
- employee status.

### Stage 5 — Root-cause analysis

Test the following competing hypotheses:

1. Rajshahi underperformance is caused by lower compensation.
2. Rajshahi underperformance is caused by weak recruitment quality.
3. Rajshahi underperformance is caused by insufficient onboarding or training.
4. Rajshahi underperformance is caused by management and supervision gaps.
5. Rajshahi underperformance is caused by rapid expansion and workforce instability.
6. Rajshahi only appears weaker because its department and job-level mix differs from Dhaka.
7. Rajshahi is not materially weaker after proper adjustment.

Each hypothesis must be labelled **supported**, **partially supported**, **rejected** or **inconclusive**.

### Stage 6 — Decision recommendation

Choose **Continue**, **Pause** or **Redesign** and provide:

- exactly three priority interventions;
- the expected workforce effect;
- target population;
- relevant KPI;
- implementation sequence;
- risk of inaction;
- analytical limitations.

---

## 8. Mandatory metrics

### Workforce

- opening, closing and average headcount;
- headcount growth;
- net workforce movement;
- workforce share by location and department;
- new-hire concentration;
- workforce stability ratio.

### Recruitment

- requisition count and fulfilment rate;
- average and median time-to-fill;
- cost per hire;
- hiring rate;
- joining conversion rate;
- vacancy ageing;
- repeated requisition rate.

### Turnover

- total, voluntary and involuntary separation rates;
- retention rate;
- early-tenure exit rate;
- department, location and manager-level turnover;
- high-performer turnover where supported.

### Compensation

- total payroll;
- payroll per employee;
- average and median gross salary;
- compensation by department and job level;
- location pay difference;
- department-adjusted and job-level-adjusted pay difference;
- compensation-performance alignment.

### Training and performance

- training participation and completion rates;
- training hours and cost per employee;
- new-hire training coverage;
- average and median rating;
- rating distribution;
- low-performance rate;
- high-performance share;
- manager and location rating variation.

### Leave and safety

- leave transactions and leave days per employee;
- leave utilisation;
- monthly and department leave concentration;
- incident rate per employee;
- incident severity and category distribution;
- location and department incident concentration.

### Diversity

- gender representation;
- location and department representation;
- leadership representation;
- hiring, performance and separation distribution by demographic group where valid.

---

## 9. Hidden analytical traps

1. **Denominator failure** — fewer Rajshahi exits may still represent a higher turnover rate.
2. **Department-mix distortion** — overall pay or performance comparisons may be invalid.
3. **New-office maturity effect** — lower tenure may explain part of the instability.
4. **Simpson's paradox** — Rajshahi may look weaker overall but not within comparable departments.
5. **One-to-many join inflation** — leave and training joins may multiply headcount and payroll.
6. **Survivorship bias** — analysing only active employees excludes separated employees.
7. **Training selection bias** — better outcomes among trained employees do not prove causation.
8. **Small-group volatility** — a few events may create extreme percentages in small teams.
9. **Manager effect versus location effect** — one manager may drive a location-level pattern.
10. **Internal versus external pay evidence** — internal pay gaps do not establish market competitiveness.

---

## 10. Mandatory case questions

### Data and model

1. Are employee, recruitment, separation and compensation records internally consistent?
2. What is the grain of each table?
3. Which joins create duplicate-counting risk?
4. Which datasets require aggregation before joining?
5. Which variables are dimensions and which are facts?
6. Which fields are missing or unreliable?
7. Which business questions cannot be answered?

### Workforce diagnosis

8. Is Rajshahi genuinely underperforming?
9. Does the result remain after department and job-level adjustment?
10. Does tenure explain part of the difference?
11. Is instability concentrated in particular departments or under particular managers?
12. Is the problem driven by hiring, exits or both?
13. Are Rajshahi employees leaving earlier than Dhaka employees?

### Recruitment and compensation

14. Which location has the longer time-to-fill?
15. Which departments have the oldest or repeated vacancies?
16. Is Rajshahi hiring growth sustainable?
17. Are high-hiring departments also high-turnover departments?
18. Are Rajshahi employees paid less within comparable roles?
19. Are pay differences explained by department composition?
20. Is lower compensation associated with higher turnover?
21. Which compensation conclusions require external data?

### Capability, leave and safety

22. Does Rajshahi have lower training coverage?
23. Are new employees receiving adequate training?
24. Are low-performance teams also under-trained?
25. Is performance variation explained by location, manager, tenure or department?
26. Does Rajshahi have a higher leave burden per employee?
27. Are safety incidents higher after normalising for headcount?
28. Is safety associated with training coverage, without claiming causation?

### Strategic decision

29. Should the expansion continue, pause or be redesigned?
30. Which Dhaka practices should be retained?
31. Which practices should not be copied?
32. Which policies require localisation?
33. What are the three most urgent interventions?
34. What is the implementation sequence?
35. What is the risk of taking no action?
36. Which KPIs should be monitored weekly and monthly?
37. What evidence is still missing?

---

## 11. Required submissions

### 1. Executive dashboard

Maximum five pages:

1. Executive status and recommendation;
2. Workforce stability;
3. Recruitment and compensation;
4. Capability, leave and safety;
5. Q1 FY2026 action plan.

### 2. Analytical report

Recommended length: **2,500–4,000 words**.

Required sections:

- executive summary;
- business context;
- data architecture;
- data-quality findings;
- analytical method;
- Dhaka–Rajshahi comparison;
- root-cause assessment;
- alternative explanations;
- management recommendation;
- implementation plan;
- limitations;
- monitoring framework.

### 3. Executive decision memo

Maximum two pages. It must clearly state:

- Continue, Pause or Redesign;
- three priority interventions;
- evidence;
- expected effect;
- implementation risk;
- monitoring plan.

### 4. Data model

Include:

- fact and dimension map;
- table grain;
- primary and foreign keys;
- relationship cardinality;
- duplicate prevention logic;
- aggregation rules.

### 5. KPI dictionary

| KPI | Formula | Source table | Grain | Interpretation | Limitation |
|---|---|---|---|---|---|

### 6. Evidence register

| Claim | Evidence | Classification | Confidence | Limitation |
|---|---|---|---:|---|

---

## 12. Evaluation rubric

| Area | Weight |
|---|---:|
| Data-quality assessment | 10% |
| Data model and grain accuracy | 15% |
| KPI calculation accuracy | 15% |
| Controlled Dhaka–Rajshahi comparison | 15% |
| Root-cause reasoning | 15% |
| Management recommendation | 10% |
| Evidence discipline | 10% |
| Limitation disclosure | 5% |
| Dashboard communication | 5% |
| **Total** | **100%** |

---

## 13. Strong-solution standard

A strong solution will:

- challenge management assumptions;
- distinguish totals from rates;
- control for department, job level and tenure;
- prevent duplicate counting;
- separate fact from inference;
- reject unsupported market claims;
- evaluate alternative explanations;
- quantify operational risk;
- prioritise exactly three interventions;
- provide a clear decision;
- disclose limitations honestly.

A weak solution will compare only totals, assume Dhaka is automatically better, treat correlation as causation, ignore grain, fabricate evidence or produce charts without a management decision.

---

## 14. Final storyline

Mokhles Group built a stable Dhaka-centred HR operating model over several years. When it expanded into Rajshahi, management assumed that the same recruitment, management, compensation and training rules could be transferred with limited modification.

By Q4 FY2025, Rajshahi was adding employees but management could not determine whether the workforce was becoming stronger or merely larger. The available data was fragmented across workforce, hiring, exits, payroll, leave, training, performance and safety records. Raw comparisons produced conflicting conclusions.

Musa was assigned to convert those records into a governed analytical model, test competing explanations and determine whether Rajshahi was a failing location or whether Mokhles Group was using the wrong operating model for a new location.

The final decision cannot be based on one chart or one KPI. It must integrate workforce stability, recruitment efficiency, compensation, capability, leave and safety evidence while respecting strict data limitations.

> **The portfolio narrative is a transformation from fragmented HR records, to governed analytics, to controlled workforce diagnosis, and finally to an evidence-based regional expansion decision.**
