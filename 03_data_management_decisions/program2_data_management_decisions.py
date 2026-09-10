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
