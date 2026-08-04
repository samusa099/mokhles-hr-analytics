# Releases and Roadmap

## Current release line

The repository README identifies the current portfolio release as **v2.5.0**.

Key maintained capabilities include:

- fully synthetic Bangladesh-context HR data;
- reproducible Python validation and transformation;
- 15-table BI-ready analytical model;
- Employee 360 and Department 360 outputs;
- data-quality profiles and validation rules;
- Power BI semantic-model assets and theme;
- Excel, SQL, Python and multi-platform learning support;
- Rajshahi Expansion Crisis advanced case;
- participant-submission branch governance;
- security, dependency and required-check workflows.

## Release documentation

- `RELEASE_NOTES_v2.5.0.md` — governance, security and advanced case study
- `RELEASE_NOTES_v2.4.0.md` — runtime compatibility and deployment readiness
- `release/` — release pointer and manifests
- `CITATION.cff` — citation metadata

## Suggested release validation

Before publishing a new version:

1. Run unit tests.
2. Run repository validation.
3. Rebuild BI-ready and analysis-ready layers.
4. Regenerate data-quality profiles.
5. Reconcile row counts and headline KPIs.
6. Validate documentation links and Wiki navigation.
7. Confirm Kaggle package consistency.
8. Review synthetic-data notices and licences.
9. Confirm required GitHub checks pass.
10. Publish release notes describing material changes and migration impact.

## Roadmap priorities

### Data and analytics

- Expand automated KPI reconciliation across Python, SQL, Excel and DAX.
- Add controlled scenario and sensitivity examples.
- Strengthen fairness and cohort-comparison guidance.
- Add data-contract checks for generated tables.

### BI and reporting

- Provide validated dashboard screenshots or portable demo outputs.
- Expand semantic-model documentation and measure catalogues.
- Add platform-specific implementation checks for Tableau, Qlik and Metabase.
- Improve executive storytelling examples using Department 360.

### Learning and community

- Add graded exercises from beginner to advanced.
- Publish model participant submissions after review.
- Add instructor notes and evaluation rubrics.
- Improve Kaggle notebooks and onboarding paths.

### Engineering and governance

- Keep actions and dependencies updated through reviewed maintenance changes.
- Preserve branch protection and participant isolation.
- Automate Wiki-source synchronization when the GitHub Wiki repository is initialized.
- Maintain deterministic builds and documented release manifests.

## Versioning principle

Use semantic versioning:

- **Patch:** documentation, validation or compatibility fixes without changing analytical meaning.
- **Minor:** backward-compatible datasets, metrics, guides or platform capabilities.
- **Major:** breaking schema, KPI-definition or workflow changes requiring migration.
