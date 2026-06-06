import pandas as pd

df = pd.read_csv("../Dataset/BankChurners.csv")

# Remove unnecessary columns
df = df.drop(columns=[
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
])

# Attrition Rate
attrition_rate = (
    (df['Attrition_Flag'] == 'Attrited Customer').mean()
) * 100

print(f"\nAttrition Rate: {attrition_rate:.2f}%")
print("\nAttrition by Card Category:")
print(
    pd.crosstab(
        df['Card_Category'],
        df['Attrition_Flag']
    )
)
print("\nAttrition Rate by Card Category:")

card_attrition = (
    pd.crosstab(
        df['Card_Category'],
        df['Attrition_Flag'],
        normalize='index'
    ) * 100
)

print(card_attrition)
print("\nAttrition Rate by Income Category:")

income_attrition = (
    pd.crosstab(
        df['Income_Category'],
        df['Attrition_Flag'],
        normalize='index'
    ) * 100
)

print(income_attrition.sort_values(
    by='Attrited Customer',
    ascending=False
))
df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[20,30,40,50,60,70],
    labels=[
        '20-30',
        '30-40',
        '40-50',
        '50-60',
        '60-70'
    ]
)

print("\nAttrition Rate by Age Group:")

age_attrition = (
    pd.crosstab(
        df['Age_Group'],
        df['Attrition_Flag'],
        normalize='index'
    ) * 100
)

print(
    age_attrition.sort_values(
        by='Attrited Customer',
        ascending=False
    )
)
# Risk Score

df["Risk_Score"] = (
    df["Months_Inactive_12_mon"] * 10
    + df["Contacts_Count_12_mon"] * 5
    - (df["Total_Trans_Ct"] / 10)
)

print("\nRisk Score Summary:")
print(df["Risk_Score"].describe())
# Risk Segmentation

df["Risk_Level"] = pd.cut(
    df["Risk_Score"],
    bins=[-100, 25, 40, 100],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

print("\nRisk Level Distribution:")
print(df["Risk_Level"].value_counts())
print("\nHigh Risk Customers:")

high_risk = df[df["Risk_Level"] == "High Risk"]

print("Total High Risk Customers:")
print(len(high_risk))

print("\nHigh Risk Customers by Card Category:")
print(high_risk["Card_Category"].value_counts())

print("\nHigh Risk Customers by Income Category:")
print(high_risk["Income_Category"].value_counts())
# Export Final Dataset

df.to_csv(
    "../Dataset/Customer_Risk_Analytics.csv",
    index=False
)

print("\nFinal dataset exported successfully!")