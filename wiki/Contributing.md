# Contributing

## Contribution paths

### Core project improvements

Use a feature or maintenance branch and open a pull request to `main` for:

- validation and transformation scripts;
- tests and runtime compatibility;
- data dictionaries and metadata;
- BI assets and platform guides;
- documentation and Wiki source;
- corrections to maintained synthetic datasets;
- release and packaging improvements.

### Participant case submissions

Solutions to the Rajshahi Expansion Crisis must:

- be placed under `participant_submissions/**`;
- follow the submission template;
- target the dedicated `submissions` branch;
- not alter core datasets, scripts or governance files.

## Recommended development workflow

```bash
git checkout main
git pull
git checkout -b docs/clear-change-name
python -m pip install -r requirements.txt
python -m pip install -e .
```

Make the smallest coherent change, then run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

Run generated-layer builds when relevant:

```bash
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
python scripts/profile_data.py
```

## Pull-request checklist

- [ ] The purpose and affected files are clear.
- [ ] Source and generated files are not confused.
- [ ] Table grain and KPI definitions remain valid.
- [ ] Tests and repository validation pass.
- [ ] Documentation is updated when behavior changes.
- [ ] No real personal or organisational data is included.
- [ ] No secrets, credentials or private endpoints are committed.
- [ ] Licensing and attribution remain intact.
- [ ] Participant files target the correct branch.

## Documentation conventions

- Use clear, descriptive headings.
- Write paths and commands in code formatting.
- Define every KPI numerator, denominator and period.
- State whether evidence is observed, calculated or inferred.
- Keep synthetic-data notices visible.
- Link detailed source documents instead of duplicating conflicting instructions.

## Data changes

A proposed data correction should include:

1. The affected table and business key.
2. The current and proposed values.
3. Why the current value is inconsistent.
4. The validation rule or source logic supporting the change.
5. Any generated files that must be rebuilt.
6. Before-and-after reconciliation results.

## Wiki maintenance

The maintained Wiki source lives in `wiki/`. Update navigation in `_Sidebar.md` whenever a page is added, renamed or removed.
