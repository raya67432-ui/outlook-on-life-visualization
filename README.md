# Outlook on Life — Data Visualization

Univariate and bivariate graphs exploring the relationship between educational
attainment and political ideology, built as part of a data management and
visualization course project.

## Dataset

**Source:** Outlook on Life Surveys, 2012 ([ICPSR 35348](https://www.icpsr.umich.edu/web/ICPSR/studies/35348)), Robnett & Tate (2012)
**Sample size:** 2,294 respondents (2,234 with valid answers on both variables used below)

## Variables

| Role | Variable | Description |
|---|---|---|
| Explanatory | `PPEDUCAT` | Educational attainment, 4 categories (Less than HS → Bachelor's or higher) |
| Response | `W1_C2` | Ideological self-placement, 7-point scale (Extremely liberal → Extremely conservative) |

## Files

- `graphs_program.py` / notebook — the full Python program that cleans the
  data and produces all three graphs
- `univariate_education.png` — distribution of respondents by education level
- `univariate_ideology.png` — distribution of respondents by ideology
- `bivariate_education_ideology.png` — ideology distribution within each
  education group (grouped bar chart, percentages)

## Key Findings

- **Education (univariate):** Fairly evenly split among "High School,"
  "Some College," and "Bachelor's or higher" (~30% each), with "Less than
  HS" as a clear minority (~9%).
- **Ideology (univariate):** Strongly centered on "Moderate" (39%, the
  mode), with roughly symmetric spread toward liberal and conservative
  categories on either side; extremes are rare (~3–4% each).
- **Relationship (bivariate):** "Moderate" is the most common response at
  every education level, but the pattern shifts modestly with education —
  the Bachelor's-or-higher group leans more liberal (mean ideology score
  3.87) than the High School group (mean 4.20), with the other two groups
  falling in between.

## Tools

Python (pandas, numpy, matplotlib), run in Jupyter Notebook.
