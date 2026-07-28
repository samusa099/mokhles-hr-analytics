# Main Branch Protection and Submission Governance

## Policy objective

The `main` branch is the canonical, release-ready version of the Mokhles Group HR Analytics project. It must not receive direct participant submissions or unreviewed changes.

Participant solutions belong on the dedicated `submissions` branch and inside:

```text
participant_submissions/<github-username>/
```

## Repository-enforced policy

The workflow `.github/workflows/submission-target-policy.yml` fails any pull request that changes `participant_submissions/**` while targeting `main`.

This workflow is a policy check. To make it an actual merge barrier, configure the GitHub ruleset below and require the check.

## Required GitHub ruleset

Open:

```text
Repository → Settings → Rules → Rulesets → New ruleset → New branch ruleset
```

Use these settings:

### General

| Setting | Value |
|---|---|
| Ruleset name | `Protect main` |
| Enforcement status | `Active` |
| Target branches | Include default branch or pattern `main` |

### Branch rules

Enable:

- Restrict deletions;
- Block force pushes;
- Require a pull request before merging;
- Require at least 1 approval;
- Dismiss stale approvals when new commits are pushed;
- Require conversation resolution before merging;
- Require status checks to pass;
- Require branches to be up to date before merging;
- Require linear history;
- Do not allow bypassing the above settings, unless an emergency administrator bypass is deliberately retained.

### Required status checks

Add the checks currently used by the repository:

- `Repository Data Quality and Security`;
- `CodeQL Security Scan`;
- `Python Dependency Security Audit` when triggered;
- `Secret Exposure Scan`;
- `Python Runtime Compatibility` when triggered;
- `Require submissions branch` for participant-submission paths.

GitHub displays the exact check names after each workflow has run at least once.

## Submission branch

Create or retain a permanent branch named:

```text
submissions
```

Participant pull requests must use:

```text
base: submissions
head: participant feature branch
```

They must not use `main` as the base branch.

## Maintainer workflow

Canonical project changes:

```text
feature branch → pull request → required checks → review → main
```

Participant work:

```text
participant branch → pull request → required checks → submissions
```

## Important limitation

A workflow file alone cannot fully prevent a repository administrator from bypassing a failed check or pushing directly. The GitHub branch ruleset must be activated in repository settings for enforceable protection.

## Emergency changes

Emergency changes to `main` should still use a pull request. Any administrator bypass must be documented in the pull request with:

- reason for bypass;
- affected files;
- risk assessment;
- validation performed;
- follow-up remediation.
