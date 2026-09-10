import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Load data
# ------------------------------------------------------------------
data = pd.read_csv('1.csv', low_memory=False)

# ------------------------------------------------------------------
# 2. Clean / recode variables
# ------------------------------------------------------------------
data['PPEDUCAT'] = pd.to_numeric(data['PPEDUCAT'], errors='coerce')
data['W1_C2']    = pd.to_numeric(data['W1_C2'], errors='coerce')

data['PPEDUCAT'] = data['PPEDUCAT'].replace([-1, -2], np.nan)
data['W1_C2']    = data['W1_C2'].replace([-1], np.nan)

educ_labels = {
    1: 'Less than HS',
    2: 'High School',
    3: 'Some College',
    4: "Bachelor's or higher"
}
ideo_labels = {
    1: 'Extremely liberal', 2: 'Liberal', 3: 'Slightly liberal',
    4: 'Moderate', 5: 'Slightly conservative', 6: 'Conservative',
    7: 'Extremely conservative'
}

sub = data[['PPEDUCAT', 'W1_C2']].dropna().copy()
sub['educ_label'] = sub['PPEDUCAT'].map(educ_labels)
sub['ideo_label'] = sub['W1_C2'].map(ideo_labels)

print("Valid cases used for analysis:", len(sub))
print("\nEducation category center/spread:")
print(sub['PPEDUCAT'].describe())
print("\nIdeology scale center/spread:")
print(sub['W1_C2'].describe())

# ------------------------------------------------------------------
# 3. UNIVARIATE GRAPH 1 — Educational Attainment (explanatory variable)
# ------------------------------------------------------------------
educ_order = [1, 2, 3, 4]
educ_counts = sub['PPEDUCAT'].value_counts().reindex(educ_order)

plt.close('all')
plt.figure(figsize=(7, 5))
bars = plt.bar(range(len(educ_order)), educ_counts.values, color='#4C72B0', edgecolor='black')
plt.xticks(range(len(educ_order)), [educ_labels[v] for v in educ_order])
plt.xlabel('Educational Attainment')
plt.ylabel('Number of Respondents')
plt.title('Univariate Distribution: Educational Attainment (PPEDUCAT)')
for bar, val in zip(bars, educ_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, val + 10, str(int(val)),
              ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('univariate_education.png', dpi=150)
plt.show()

# ------------------------------------------------------------------
# 4. UNIVARIATE GRAPH 2 — Ideological Self-Placement (response variable)
# ------------------------------------------------------------------
ideo_order = [1, 2, 3, 4, 5, 6, 7]
ideo_counts = sub['W1_C2'].value_counts().reindex(ideo_order)

plt.close('all')
plt.figure(figsize=(8, 5))
bars = plt.bar(range(len(ideo_order)), ideo_counts.values, color='#C44E52', edgecolor='black')
plt.xticks(range(len(ideo_order)), [ideo_labels[v] for v in ideo_order], fontsize=8, rotation=20, ha='right')
plt.xlabel('Ideological Self-Placement (7-point scale)')
plt.ylabel('Number of Respondents')
plt.title('Univariate Distribution: Ideological Self-Placement (W1_C2)')
for bar, val in zip(bars, ideo_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, val + 10, str(int(val)),
              ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('univariate_ideology.png', dpi=150)
plt.show()

# ------------------------------------------------------------------
# 5. BIVARIATE GRAPH — Ideology by Education level
# ------------------------------------------------------------------
ct = pd.crosstab(sub['PPEDUCAT'], sub['W1_C2'], normalize='index') * 100
ct = ct.reindex(index=educ_order, columns=ideo_order)

plt.close('all')
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(ideo_order))
width = 0.2
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']

for i, educ_val in enumerate(educ_order):
    ax.bar(x + (i - 1.5) * width, ct.loc[educ_val].values, width,
           label=educ_labels[educ_val], color=colors[i], edgecolor='black')

ax.set_xticks(x)
ax.set_xticklabels([ideo_labels[v] for v in ideo_order], fontsize=8, rotation=20, ha='right')
ax.set_xlabel('Ideological Self-Placement')
ax.set_ylabel('Percent within Education Group (%)')
ax.set_title('Bivariate Relationship: Ideology by Educational Attainment')
ax.legend(title='Education Level', fontsize=8)
plt.tight_layout()
plt.savefig('bivariate_education_ideology.png', dpi=150)
plt.show()

# ------------------------------------------------------------------
# 6. Supporting summary statistics for the bivariate relationship
# ------------------------------------------------------------------
print("\nMean ideology score (1=extremely liberal, 7=extremely conservative) by education level:")
print(sub.groupby('educ_label', observed=True)['W1_C2'].mean().reindex(
    [educ_labels[v] for v in educ_order]))
