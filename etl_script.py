import pandas as pd

# Load the CSV file
df = pd.read_csv("input_data.csv")

# Preview the first few rows
print("Initial Data:")
print(df.head())

# Drop rows with any missing values
df_clean = df.dropna()

# Standardize column names (lowercase, underscores)
df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(" ", "_")

# Add a new column to flag delinquent loans
df_clean["loan_status"] = df_clean["current_loan_delinquency_status"].apply(
    lambda x: "Delinquent" if x > 0 else "Current"
)

# Save the cleaned data to a new CSV file
df_clean.to_csv("output_data.csv", index=False)

print("ETL process completed. Cleaned data saved to 'output_data.csv'.")
