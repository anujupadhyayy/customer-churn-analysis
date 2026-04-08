import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Customer-Churn-Records.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.head(3))




df = pd.read_csv("Customer-Churn-Records.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# ── 1. Overall churn rate
churn_rate = df['exited'].mean() * 100
print(f"Overall Churn Rate: {churn_rate:.1f}%")

# ── 2. Churn by Geography
geo_churn = df.groupby('geography')['exited'].mean().sort_values(ascending=False) * 100
print("\nChurn Rate by Geography:\n", geo_churn.round(1))

# ── 3. Churn by Gender
gender_churn = df.groupby('gender')['exited'].mean() * 100
print("\nChurn Rate by Gender:\n", gender_churn.round(1))

# ── 4. Churn by Age Group
df['age_group'] = pd.cut(df['age'], bins=[0,30,45,60,100],
                          labels=['<30','30-45','45-60','60+'])
age_churn = df.groupby('age_group', observed=True)['exited'].mean() * 100
print("\nChurn Rate by Age Group:\n", age_churn.round(1))

# ── 5. Churn by Number of Products
prod_churn = df.groupby('numofproducts')['exited'].mean() * 100
print("\nChurn Rate by No. of Products:\n", prod_churn.round(1))

# ── 6. Churn by Active Member status
active_churn = df.groupby('isactivemember')['exited'].mean() * 100
print("\nChurn Rate - Inactive(0) vs Active(1):\n", active_churn.round(1))

# ── 7. Churn by Satisfaction Score
sat_churn = df.groupby('satisfaction_score')['exited'].mean() * 100
print("\nChurn Rate by Satisfaction Score:\n", sat_churn.round(1))

# ── 8. Churn by Card Type
card_churn = df.groupby('card_type')['exited'].mean() * 100
print("\nChurn Rate by Card Type:\n", card_churn.round(1))

# ── 9. Avg Balance: churned vs retained
bal = df.groupby('exited')['balance'].mean()
print("\nAvg Balance - Retained(0) vs Churned(1):\n", bal.round(2))

# ── 10. Complaint impact on churn
comp_churn = df.groupby('complain')['exited'].mean() * 100
print("\nChurn Rate - No Complaint(0) vs Complaint(1):\n", comp_churn.round(1))

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Customer Churn Analysis — Key Drivers', fontsize=16, fontweight='bold')

# 1. Churn by Age Group
age_churn.plot(kind='bar', ax=axes[0,0], color=['#2ecc71','#f39c12','#e74c3c','#c0392b'])
axes[0,0].set_title('Churn Rate by Age Group')
axes[0,0].set_ylabel('Churn Rate (%)')
axes[0,0].set_xlabel('')
axes[0,0].tick_params(axis='x', rotation=0)

# 2. Churn by No. of Products
prod_churn.plot(kind='bar', ax=axes[0,1], color=['#3498db','#2ecc71','#e74c3c','#c0392b'])
axes[0,1].set_title('Churn Rate by No. of Products')
axes[0,1].set_ylabel('Churn Rate (%)')
axes[0,1].set_xlabel('')
axes[0,1].tick_params(axis='x', rotation=0)

# 3. Churn by Geography
geo_churn.plot(kind='bar', ax=axes[0,2], color=['#e74c3c','#f39c12','#2ecc71'])
axes[0,2].set_title('Churn Rate by Geography')
axes[0,2].set_ylabel('Churn Rate (%)')
axes[0,2].set_xlabel('')
axes[0,2].tick_params(axis='x', rotation=0)

# 4. Complaint vs Churn
comp_churn.plot(kind='bar', ax=axes[1,0], color=['#2ecc71','#e74c3c'])
axes[1,0].set_title('Churn Rate: Complaint vs No Complaint')
axes[1,0].set_ylabel('Churn Rate (%)')
axes[1,0].set_xticklabels(['No Complaint','Complained'], rotation=0)

# 5. Avg Balance: Churned vs Retained
bal.plot(kind='bar', ax=axes[1,1], color=['#3498db','#e74c3c'])
axes[1,1].set_title('Avg Balance: Retained vs Churned')
axes[1,1].set_ylabel('Average Balance (₹)')
axes[1,1].set_xticklabels(['Retained','Churned'], rotation=0)

# 6. Active vs Inactive churn
active_churn.plot(kind='bar', ax=axes[1,2], color=['#e74c3c','#2ecc71'])
axes[1,2].set_title('Churn Rate: Inactive vs Active Members')
axes[1,2].set_ylabel('Churn Rate (%)')
axes[1,2].set_xticklabels(['Inactive','Active'], rotation=0)

plt.tight_layout()
plt.savefig('churn_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart saved as churn_analysis.png")