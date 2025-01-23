import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset as a dictionary
data = {
    "Product_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Product_Name": ["PainRelief", "ColdCure", "HeadacheFix", "PainRelief", "ColdCure",
                     "HeadacheFix", "PainRelief", "ColdCure", "HeadacheFix", "PainRelief"],
    "Region": ["North America", "Europe", "Asia", "North America", "Europe",
               "Asia", "North America", "Europe", "Asia", "North America"],
    "Marketing_Spend": [50000, 30000, 45000, 52000, 28000, 48000, 51000, 31000, 47000, 53000],
    "Sales": [100000, 60000, 80000, 110000, 55000, 90000, 105000, 65000, 85000, 115000],
    "Effectiveness": [85, 75, 80, 88, 70, 82, 86, 78, 80, 90],
    "Side_Effects": [5, 2, 3, 4, 1, 3, 5, 2, 4, 6],
    "Age_Group": ["20-30", "30-40", "40-50", "50-60", "30-40", "40-50", "20-30", "30-40", "50-60", "20-30"],
    "Trial_Period": ["6 months", "3 months", "6 months", "12 months", "3 months", "6 months", "6 months", "3 months", "12 months", "6 months"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Bar plot of average effectiveness by region and product
sns.barplot(data=df, x="Region", y="Effectiveness", hue="Product_Name")
plt.title("Average Effectiveness Across Regions")
plt.xlabel("Region")
plt.ylabel("Average Effectiveness")
plt.legend(title="Product Name")
plt.show()

# Violin plot for Effectiveness
sns.violinplot(data=df, x="Product_Name", y="Effectiveness", palette="muted")
plt.title("Distribution of Effectiveness by Product")
plt.show()

# Violin plot for Side Effects
sns.violinplot(data=df, x="Product_Name", y="Side_Effects", palette="muted")
plt.title("Distribution of Side Effects by Product")
plt.show()

# Pairplot for Effectiveness, Side Effects, and Marketing Spend
sns.pairplot(df[["Effectiveness", "Side_Effects", "Marketing_Spend"]], diag_kind="kde")
plt.show()

# Boxplot for Effectiveness by Trial Period
sns.boxplot(data=df, x="Trial_Period", y="Effectiveness", hue="Product_Name", palette="pastel")
plt.title("Effectiveness by Trial Period")
plt.xlabel("Trial Period")
plt.ylabel("Effectiveness")
plt.legend(title="Product Name")
plt.show()

# Regression plot for Marketing Spend vs. Effectiveness
sns.regplot(data=df, x="Marketing_Spend", y="Effectiveness", scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Marketing Spend vs. Effectiveness")
plt.xlabel("Marketing Spend")
plt.ylabel("Effectiveness")
plt.show()

# Analysis of Best Product
average_effectiveness = df.groupby("Product_Name")["Effectiveness"].mean()
print("Average Effectiveness by Product:")
print(average_effectiveness)

# Correlation between Effectiveness and Side Effects
correlation = df[["Effectiveness", "Side_Effects"]].corr()
print("\nCorrelation Between Effectiveness and Side Effects:")
print(correlation)
