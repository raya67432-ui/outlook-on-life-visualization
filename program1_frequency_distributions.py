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
