# Program 1: Data Management & Frequency Distributions

This step looks at each of the two core variables from the proposal
separately, using univariate descriptive analysis — a frequency table
showing counts and valid percentages for each category.

## The Program

```python
"""
Outlook on Life Surveys (2012, ICPSR 35348)
Program 1: Data Management & Frequency Distributions
------------------------------------------------------
Builds valid-percentage frequency tables for the two core variables
in this project: educational attainment (PPEDUCAT) and ideological
self-placement (W1_C2).
"""

import pandas as pd
import numpy as np

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 10)

# ------------------------------------------------------------------
# Step 1: Load the data
# ------------------------------------------------------------------
data = pd.read_csv('1.csv', low_memory=False)

# ------------------------------------------------------------------
# Step 2: List the variables to manage
# ------------------------------------------------------------------
project_vars = ['PPEDUCAT', 'W1_C2']

# ------------------------------------------------------------------
# Step 3: Convert to numeric (anything unreadable becomes NaN)
# ------------------------------------------------------------------
for var in project_vars:
    data[var] = pd.to_numeric(data[var], errors='coerce')

# ------------------------------------------------------------------
# Step 4: Recode codebook missing values (-1, -2) as NaN
# ------------------------------------------------------------------
data['PPEDUCAT'] = data['PPEDUCAT'].replace([-1, -2], np.nan)
data['W1_C2']    = data['W1_C2'].replace([-1], np.nan)

# ------------------------------------------------------------------
# Step 5: Value labels
# ------------------------------------------------------------------
labels = {
    'PPEDUCAT': {
        1: 'Less than high school',
        2: 'High school',
        3: 'Some college',
        4: "Bachelor's degree or higher"
    },
    'W1_C2': {
        1: 'Extremely liberal', 2: 'Liberal', 3: 'Slightly liberal',
        4: 'Moderate; middle of the road', 5: 'Slightly conservative',
        6: 'Conservative', 7: 'Extremely conservative'
    }
}

# ------------------------------------------------------------------
# Step 6: Reusable frequency-table function
# ------------------------------------------------------------------
def print_frequency_table(varname, label_map):
    n_total = len(data)
    n_missing = data[varname].isna().sum()
    n_valid = n_total - n_missing

    # Step 7: counts
    counts = data[varname].value_counts(dropna=True).sort_index()

    # Step 8: valid percentages (denominator = valid cases, not total)
    pct = (counts / n_valid * 100).round(1)

    # Step 9: combine into one table
    table = pd.DataFrame({'Count': counts, 'Valid %': pct})

    # Step 10: replace numeric codes with labels
    table.index = [label_map.get(v, v) for v in table.index]

    print(f'\n=== {varname} ===')
    print(table)
    # Step 11: report missing separately
    print(f'Valid cases: {n_valid} of {n_total} | Missing/refused/NA: {n_missing}')


# ------------------------------------------------------------------
# Step 12: Run the function for each variable
# ------------------------------------------------------------------
for var in project_vars:
    print_frequency_table(var, labels[var])
```

## Why each step matters

- **Step 3 (convert to numeric):** survey CSVs can contain blank spaces
  or stray text where a number is expected. `errors='coerce'` turns
  anything unreadable into `NaN` instead of quietly treating the whole
  column as text.
- **Step 4 (recode missing codes):** the codebook defines `-1` as
  "refused" and `-2` as "not applicable" — real numbers, but not real
  survey answers. Left alone, they'd distort any average or frequency
  count, so they're recoded to `NaN` before anything else happens.
- **Step 8 (valid percentages):** percentages are calculated against
  the number of people who actually answered the question
  (`n_valid`), not the full sample (`n_total`) — so the table
  describes the distribution among respondents who answered, with
  missingness reported separately rather than baked into the
  percentages.
- **Step 6 (reusable function):** rather than writing the same
  count → percentage → label logic twice (once per variable), one
  function handles any variable, which keeps the code shorter and
  easier to check for mistakes.

## Results

```
=== PPEDUCAT ===
                             Count  Valid %
Less than high school          219      9.5
High school                    700     30.5
Some college                   682     29.7
Bachelor's degree or higher    693     30.2
Valid cases: 2294 of 2294 | Missing/refused/NA: 0

=== W1_C2 ===
                              Count  Valid %
Extremely liberal                75      3.4
Liberal                         312     14.0
Slightly liberal                286     12.8
Moderate; middle of the road    874     39.1
Slightly conservative           297     13.3
Conservative                    311     13.9
Extremely conservative           79      3.5
Valid cases: 2234 of 2294 | Missing/refused/NA: 60
```

## Summary

**Educational attainment (PPEDUCAT)** has zero missing data, since it's
a background variable supplied by the survey panel rather than a
question respondents could refuse to answer. The sample is fairly
evenly spread across categories: the largest group (30.5%) has only a
high school diploma, closely followed by those with a bachelor's
degree or higher (30.2%) and those with some college but no degree
(29.7%); less than 10% of the sample did not complete high school.

**Ideological self-placement (W1_C2)** clusters heavily at the
midpoint — 39.1% place themselves as "moderate, middle of the road" —
while the remaining respondents split fairly symmetrically toward the
liberal end (3.4%–14.0% across the three liberal categories) and the
conservative end (3.5%–13.9% across the three conservative
categories). This variable had 60 missing/refused cases (2.6% of the
sample).

Overall, the panel-supplied education variable has no missing data,
while the self-reported ideology variable shows a modest amount of
missingness from survey refusals. Both distributions look plausible
and interpretable — no unexpected out-of-range values turned up after
recoding the -1 and -2 missing-value codes to NaN.

---

*Continued in [`03_data_management_decisions/`](../03_data_management_decisions/) —
a secondary variable is created by binning ideology into three groups.*
