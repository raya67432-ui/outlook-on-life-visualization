# Outlook on Life — Education & Political Ideology

A course project for the Data Management and Visualization
Specialization, exploring whether educational attainment is associated
with ideological self-placement.

**Dataset:** Outlook on Life Surveys, 2012 ([ICPSR 35348](https://www.icpsr.umich.edu/web/ICPSR/studies/35348)), Robnett & Tate (2012) — 2,294 respondents

## Project Structure

| Folder | Contents |
|---|---|
| [`01_proposal/`](./01_proposal/proposal.md) | Topic, personal codebook, literature review, research question, hypothesis |
| [`02_data_management_frequency/`](./02_data_management_frequency/frequency_distributions.md) | Program 1 — frequency tables and valid percentages for each core variable |
| [`03_data_management_decisions/`](./03_data_management_decisions/data_management_decisions.md) | Program 2 — binning `W1_C2` into a secondary 3-group ideology variable |
| [`04_data_visualization/`](./04_data_visualization/) | Program 3 — Python code and univariate/bivariate graphs |

## Variables

| Role | Variable | Description |
|---|---|---|
| Explanatory | `PPEDUCAT` | Educational attainment, 4 categories |
| Response | `W1_C2` | Ideological self-placement, 7-point scale |
| Secondary | `W1_C2_GROUP3` | `W1_C2` collapsed into Liberal / Moderate / Conservative |

## Key Findings

- **Education:** Fairly evenly split among High School, Some College,
  and Bachelor's-or-higher (~30% each); Less than HS is the clear
  minority (~9.5%). No missing data (panel-supplied variable).
- **Ideology:** Strongly centered on "Moderate" (39.1%, the mode),
  with roughly symmetric spread toward liberal and conservative;
  extremes are rare (~3–4% each). 2.6% missing (survey refusals).
- **Ideology, binned:** Once collapsed into three groups, the sample
  splits almost evenly — 30.1% Liberal, 39.1% Moderate, 30.8%
  Conservative.
- **Relationship:** "Moderate" is the most common response at every
  education level, but the pattern shifts modestly with education —
  the Bachelor's-or-higher group leans more liberal (mean ideology
  score 3.87) than the High School group (mean 4.20).

## Tools

Python (pandas, numpy, matplotlib), Jupyter Notebook.
