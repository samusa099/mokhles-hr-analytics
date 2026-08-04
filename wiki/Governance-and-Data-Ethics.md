# Governance and Data Ethics

## Synthetic-data declaration

Mokhles Group is fictional. All records are synthetic and must not be represented as real organisational, applicant, employee, payroll, medical or performance information.

## Responsible-use rules

- Use the project for learning, portfolio work, testing and demonstration.
- Do not attach real names, phone numbers, email addresses, national IDs or confidential employer data.
- Do not use synthetic risk scores as a basis for real employment decisions.
- Do not imply that fictional findings describe a real employer, location or workforce.
- Explain assumptions, exclusions and analytical limitations.
- Review fairness when comparing gender, age, disability, location or other protected or sensitive groups.

## Branch governance

The default branch contains the maintained project source and generated assets. Participant case solutions are isolated from the main project.

| Change type | Target |
|---|---|
| Core scripts, data model, documentation and maintained assets | `main` through an approved pull request |
| Participant challenge solutions | `submissions` branch |
| Files under `participant_submissions/**` | Must not target `main` |

## Quality controls

Changes should preserve:

- repository validation;
- runtime tests;
- data lineage;
- deterministic generated outputs;
- consistent table and field definitions;
- valid relationship keys;
- licensing and attribution;
- explicit synthetic-data notices.

## Automated repository controls

The repository uses GitHub workflows and branch policies for areas such as:

- required branch checks;
- CodeQL and security gates;
- dependency maintenance;
- participant-submission governance;
- validation of protected repository structure.

Automated checks complement review; they do not replace analytical validation.

## Licensing

- Dataset and documentation: **CC BY 4.0** — see `LICENSE`
- Python code and notebook utilities: **MIT** — see `LICENSE-CODE`
- Citation metadata: `CITATION.cff`

## Reporting limitations

A responsible analysis should distinguish:

- observed values from calculated KPIs;
- correlation from causation;
- missing evidence from zero activity;
- business interpretation from technical validation;
- synthetic portfolio conclusions from real-world recommendations.

## Security and privacy

Never commit secrets, credentials, private tokens, connection strings or real personal data. Use environment variables or platform-managed secrets for any future integrations.
