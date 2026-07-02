import json
import pandas as pd

# Loading the raw JSON ( je apan raw data  madhe store kela ahe tyala hite load kartoy)
with open("data/raw/repositories_raw.json", "r", encoding="utf-8") as file:
    repositories = json.load(file)

cleaned_data = []

for repo in repositories:

    cleaned_data.append({

        "repository_name": repo["name"],
        "full_name": repo["full_name"],
        "owner": repo["owner"]["login"],
        "description": repo["description"],
        "language": repo["language"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "watchers": repo["watchers_count"],
        "open_issues": repo["open_issues_count"],
        "size_kb": repo["size"],
        "default_branch": repo["default_branch"],
        "created_at": repo["created_at"],
        "updated_at": repo["updated_at"],
        "license": repo["license"]["name"] if repo["license"] else None,
        "topics": ", ".join(repo["topics"]),
        "visibility": repo["visibility"],
        "has_issues": repo["has_issues"],
        "has_projects": repo["has_projects"],
        "has_wiki": repo["has_wiki"],
        "has_pages": repo["has_pages"],
        "archived": repo["archived"],
        "disabled": repo["disabled"]
    })

df = pd.DataFrame(cleaned_data)

print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values:\n")
print(df.isnull().sum())

# processed folder banawla ani magh tyat save karnar
import os
os.makedirs("data/processed", exist_ok=True)

# to_csv pandas cha function use karun tyala csv madhe convert kela
df.to_csv(
    "data/processed/github_repositories.csv",
    index=False
)

# parquet save kela data-> folder cha processed file madhe
df.to_parquet(
    "data/processed/github_repositories.parquet",
    index=False
)

print("\nDataset saved successfully!")