# Outlook on Life — Education & Political Ideology

A course project for the Data Management and Visualization
Specialization, exploring whether educational attainment is associated
with ideological self-placement.

**Dataset:** Outlook on Life Surveys, 2012 ([ICPSR 35348](https://www.icpsr.umich.edu/web/ICPSR/studies/35348)), Robnett & Tate (2012) — 2,294 respondents

## Project Structure

| Folder | Contents |
|---|---|
| [`01_proposal/`](./01_proposal/proposal.md) | Topic, personal codebook, literature review, research question, hypothesis |
| [`02_data_visualization/`](./02_data_visualization/) | Python program and graphs (univariate + bivariate) |

## Variables

| Role | Variable | Description |
|---|---|---|
| Explanatory | `PPEDUCAT` | Educational attainment, 4 categories |
| Response | `W1_C2` | Ideological self-placement, 7-point scale |

## Key Findings (Data Visualization)

- **Education:** Fairly evenly split among High School, Some College,
  and Bachelor's-or-higher (~30% each); Less than HS is the clear
  minority (~9%).
- **Ideology:** Strongly centered on "Moderate" (39%, the mode), with
  roughly symmetric spread toward liberal and conservative; extremes
  are rare (~3–4% each).
- **Relationship:** "Moderate" is the most common response at every
  education level, but the Bachelor's-or-higher group leans more
  liberal (mean ideology score 3.87) than the High School group (mean
  4.20).

## Tools

Python (pandas, numpy, matplotlib), Jupyter Notebook.
