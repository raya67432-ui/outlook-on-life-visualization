[data_management_decisions.md](https://github.com/user-attachments/files/32052712/data_management_decisions.md)
# Program 2: Data Management Decisions

This step adds a real data management decision beyond just cleaning
missing values: a new secondary variable, `W1_C2_GROUP3`, created by
binning the original 7-point ideology scale (`W1_C2`) into three
groups (Liberal / Moderate / Conservative). This is now a third
featured frequency table, alongside education (`PPEDUCAT`) and the
original 7-point ideology scale (`W1_C2`).

## The Program

```python
"""
Outlook on Life Surveys (2012, ICPSR 35348)
Program 2: Data Management Decisions
------------------------------------------------------
Beyond basic missing-value cleaning, this program adds one real data
management decision: binning the 7-point ideology scale (W1_C2) into
a secondary 3-category variable, W1_C2_GROUP3 (Liberal / Moderate /
Conservative), which is then featured as a third frequency table
alongside the original two variables.
"""

import pandas as pd
import numpy as np

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 10)

# ------------------------------------------------------------------
# Step 1: Load and clean (same as Program 1)
# ------------------------------------------------------------------
data = pd.read_csv('1.csv', low_memory=False)

project_vars = ['PPEDUCAT', 'W1_C2']

for var in project_vars:
    data[var] = pd.to_numeric(data[var], errors='coerce')

data['PPEDUCAT'] = data['PPEDUCAT'].replace([-1, -2], np.nan)
data['W1_C2']    = data['W1_C2'].replace([-1], np.nan)

# ------------------------------------------------------------------
# Step 1d: Bin W1_C2 (7-point scale) into a secondary 3-group variable
# ------------------------------------------------------------------
# 1,2,3 (Extremely/Liberal/Slightly liberal)      -> 1 = Liberal
# 4     (Moderate)                                 -> 2 = Moderate
# 5,6,7 (Slightly/Conservative/Extremely conserv.) -> 3 = Conservative
def bin_ideology(val):
    if pd.isna(val):
        return np.nan
    elif val in [1, 2, 3]:
        return 1
    elif val == 4:
        return 2
    elif val in [5, 6, 7]:
        return 3
    return np.nan

data['W1_C2_GROUP3'] = data['W1_C2'].apply(bin_ideology)

all_vars = ['PPEDUCAT', 'W1_C2', 'W1_C2_GROUP3']

# ------------------------------------------------------------------
# Value labels, including the new binned codes
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
    },
    'W1_C2_GROUP3': {
        1: 'Liberal', 2: 'Moderate', 3: 'Conservative'
    }
}

# ------------------------------------------------------------------
# Reusable frequency-table function (same as Program 1)
# ------------------------------------------------------------------
def print_frequency_table(varname, label_map):
    n_total = len(data)
    n_missing = data[varname].isna().sum()
    n_valid = n_total - n_missing

    counts = data[varname].value_counts(dropna=True).sort_index()
    pct = (counts / n_valid * 100).round(1)
    table = pd.DataFrame({'Count': counts, 'Valid %': pct})
    table.index = [label_map.get(v, v) for v in table.index]

    print(f'\n=== {varname} ===')
    print(table)
    print(f'Valid cases: {n_valid} of {n_total} | Missing/refused/NA: {n_missing}')


# ------------------------------------------------------------------
# Run for all three variables, including the new secondary one
# ------------------------------------------------------------------
for var in all_vars:
    print_frequency_table(var, labels[var])
```

## The data management decision, explained

**Binning `W1_C2` into `W1_C2_GROUP3` (Step 1d)** is the main decision
in this program, beyond simply cleaning missing values. The original
7-point ideology scale is a bit noisy to summarize at a glance — seven
categories, several of them small. Collapsing "Extremely liberal /
Liberal / Slightly liberal" into one "Liberal" group, keeping
"Moderate" as its own group, and collapsing the three conservative
categories into "Conservative" produces a secondary variable that's
easier to interpret and more directly comparable to how ideology is
often reported in political science research, while still preserving
the substantive left/center/right structure of the original item.

**Building a labels dictionary instead of printing raw numeric
codes** keeps the output self-explanatory — a table of "1, 2, 3" with
no explanation isn't interpretable without cross-referencing the
codebook. Mapping each code, including the new binned codes 1/2/3, to
a readable label removes that step for the reader.

**Reusing the `print_frequency_table()` function from Program 1**
rather than repeating the logic keeps the program shorter and easier
to check for errors — the new variable only needed a definition and a
label dictionary, not a rewritten calculation.

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

=== W1_C2_GROUP3 ===
              Count  Valid %
Liberal         673     30.1
Moderate        874     39.1
Conservative    687     30.8
Valid cases: 2234 of 2294 | Missing/refused/NA: 60
```

## Summary

The three frequency tables above use descriptive variable names,
labeled value categories, counts, and valid percentages, so they're
interpretable without needing to consult the codebook alongside them.
The panel-supplied education variable (`PPEDUCAT`) has no missing
data, while the self-reported ideology variable (`W1_C2`) shows a
modest amount of missingness from survey refusals (2.6%).

The binning decision made the underlying pattern easier to summarize
without distorting it: once collapsed into three groups, ideology
splits almost evenly — 30.1% Liberal, 39.1% Moderate, 30.8%
Conservative — confirming that the "bulge" in the middle of the
7-point scale isn't an artifact of how the categories were split, and
that liberal- and conservative-leaning respondents are close to
equally represented once the finer distinctions are set aside.

---

*Continued in [`04_data_visualization/`](../04_data_visualization/) —
univariate and bivariate graphs built from these same variables.*
