import pandas as pd

# Load cleaned dataset in variable dff 
df = pd.read_csv("data/processed/github_repositories.csv")

# Convert dates now 
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# Repository age in days
df["repository_age_days"] = (
    pd.Timestamp.now(tz="UTC") - df["created_at"]
).dt.days

# Days since last update happend
df["days_since_last_update"] = (
    pd.Timestamp.now(tz="UTC") - df["updated_at"]
).dt.days

# Star/Fork ratio
df["star_fork_ratio"] = (
    df["stars"] / (df["forks"] + 1)
).round(2)

# Is repository active? so small then 365
df["is_active"] = df["days_since_last_update"] <= 365

# Description length
df["description_length"] = (
    df["description"]
    .fillna("")
    .str.len()
)

# license ahe ka 
df["has_license"] = df["license"].notna()

# Save karuya 
df.to_csv(
    "data/processed/github_repositories_featured.csv",
    index=False
)

print(df.head()) #first 5 dataframe
print(df.tail()) #last 5

print("\nDataset Shape:", df.shape)

print("\nFeature Engineering Completed!")