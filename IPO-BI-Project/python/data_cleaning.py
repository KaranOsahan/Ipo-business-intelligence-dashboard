import pandas as pd

pd.set_option('display.max_columns', None)

# Load raw IPO data
df = pd.read_csv("../data/ipo_master.csv")

# Calculate derived metrics
df["listing_gain_pct"] = ((df["Listing Price"] - df["Issue Price"]) / df["Issue Price"]) * 100
df["day30_return_pct"] = ((df["Day 30 Price"] - df["Issue Price"]) / df["Issue Price"]) * 100

# Decision logic
df["decision_flag"] = df.apply(
    lambda row: "HOLD" if row["day30_return_pct"] > row["listing_gain_pct"] else "SELL",
    axis=1
)

# Round for readability
df["listing_gain_pct"] = df["listing_gain_pct"].round(2)
df["day30_return_pct"] = df["day30_return_pct"].round(2)

# Show final dataset
print(df)

# Save cleaned dataset
df.to_csv("../data/ipo_cleaned.csv", index=False)

print("\nCleaned dataset saved as ipo_cleaned.csv")

# Sanity checks
print("\n--- Sanity Checks ---")

# Negative prices (should never happen)
print("Negative Issue Prices:", (df["Issue Price"] <= 0).sum())
print("Negative Listing Prices:", (df["Listing Price"] <= 0).sum())
print("Negative Day 30 Prices:", (df["Day 30 Price"] <= 0).sum())

print("\nDecision distribution:")
print(df["decision_flag"].value_counts())


print("\nSample calculation check:")
print(df[[
    "Company Name",
    "Issue Price",
    "Listing Price",
    "listing_gain_pct",
    "Day 30 Price",
    "day30_return_pct",
    "decision_flag"
]])

print("\n--- Sector-wise Performance Analysis ---")

sector_summary = df.groupby("Sector").agg(
    avg_listing_gain_pct=("listing_gain_pct", "mean"),
    avg_day30_return_pct=("day30_return_pct", "mean"),
    avg_retail_sub=("Retail Sub Ratio", "mean"),
    avg_qib_sub=("QIB Sub Ratio", "mean"),
    ipo_count=("IPO ID", "count")
).round(2)

print(sector_summary)


print("\n--- Correlation Analysis ---")

correlation_columns = [
    "Retail Sub Ratio",
    "QIB Sub Ratio",
    "HNI Sub ratio",
    "listing_gain_pct",
    "day30_return_pct"
]

correlation_matrix = df[correlation_columns].corr().round(2)

print(correlation_matrix)

