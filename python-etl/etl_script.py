
import pandas as pd

# Load data
df = pd.read_csv("input_data.csv")

# Preview
print("Initial Data:")
print(df.head())

# Drop rows with missing values
df_clean = df.dropna()

# Standardize column names
df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(" ", "_")

# Create new column: loan_status (simple logic)
df_clean["loan_status"] = df_clean["current_loan_delinquency_status"].apply(
    lambda x: "Delinquent" if x > 0 else "Current"
)

# Save to new file
df_clean.to_csv("output_data.csv", index=False)

print("ETL process completed. Cleaned data saved to output_data.csv.")
