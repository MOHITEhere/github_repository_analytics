# GitHub Repository Analytics & Dataset Pipeline

An end-to-end Data Engineering project that collects GitHub repository metadata using the GitHub REST API, transforms raw JSON into a structured dataset, performs feature engineering and exploratory data analysis (EDA), and exports the final dataset in CSV and Parquet formats.

---

## Project Overview

GitHub hosts millions of open-source repositories across multiple programming languages and technology domains. This project automates the process of collecting repository metadata, transforming the raw API response into a structured dataset, engineering meaningful features, and performing exploratory data analysis.

The project follows a modular ETL (Extract → Transform → Load) pipeline and demonstrates practical Data Engineering concepts including API integration, data cleaning, feature engineering, and dataset preparation.

---

## Project Architecture


```
GitHub REST API
        │
        ▼
Data Collection
        │
        ▼
Raw JSON Storage
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
CSV & Parquet Export
        │
        ▼
Kaggle Dataset
```

---

## Objectives

- Collect repository metadata using the GitHub REST API
- Store raw API responses for reproducibility
- Transform nested JSON into a structured dataset
- Engineer additional analytical features
- Perform exploratory data analysis
- Export the dataset in CSV and Parquet formats
- Publish the dataset on Kaggle

---

## Project Structure

```text
github-repository-analytics/
│
├── data/
│   ├── raw/
│   │   └── repositories_raw.json
│   │
│   └── processed/
│       ├── github_repositories.csv
│       ├── github_repositories.parquet
│       └── github_repositories_featured.csv
│
├── images/
│   ├── project_architecture.png
│   ├── dataset_overview.png
│   ├── top_10_programming_languages.png
│   ├── top_10_starred_repositories.png
│   ├── repository_age_distribution.png
│   ├── active_vs_inactive_repositories.png
│   ├── license_distribution.png
│   ├── stars_vs_forks_relationship.png
│   └── top_repository_owners.png
│
├── notebooks/
│   └── github_repository_eda.ipynb
│
├── src/
│   ├── config.py
│   ├── fetch_repositories.py
│   ├── clean_data.py
│   └── feature_engineering.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| API | GitHub REST API |
| Data Processing | Pandas |
| HTTP Requests | Requests |
| Progress Tracking | tqdm |
| Environment Variables | python-dotenv |
| Data Storage | CSV, Parquet |
| Visualization | Matplotlib |
| Notebook | Jupyter Notebook |

---

## ETL Pipeline

### Extract

- Authenticated using GitHub Personal Access Token
- Retrieved repository metadata from the GitHub REST API
- Implemented API pagination
- Stored raw responses as JSON

### Transform

- Parsed nested JSON responses
- Selected relevant repository attributes
- Cleaned missing values
- Standardized the dataset structure

### Feature Engineering

Additional features created:

- Repository Age (Days)
- Days Since Last Update
- Star-to-Fork Ratio
- Repository Activity Status
- Description Length
- License Availability

### Load

Generated outputs:

- CSV Dataset
- Parquet Dataset
- Feature Engineered Dataset

---

## Dataset Schema

| Feature | Description |
|----------|-------------|
| repository_name | Repository name |
| full_name | Owner/Repository |
| owner | Repository owner |
| description | Repository description |
| language | Primary programming language |
| stars | Stargazer count |
| forks | Fork count |
| watchers | Watcher count |
| open_issues | Open issues |
| license | Repository license |
| created_at | Creation timestamp |
| updated_at | Last update timestamp |
| repository_age_days | Repository age |
| days_since_last_update | Days since last update |
| star_fork_ratio | Star to fork ratio |
| is_active | Active repository indicator |
| description_length | Description length |
| has_license | License availability |

---

# Exploratory Data Analysis

## Dataset Overview


## Top 10 Programming Languages

<p align="center">
  <img src="images/top_10_programming_languages.png" width="900">
</p>

---

## Top 10 Starred Repositories

<p align="center">
  <img src="images/top_10_starred_repositories.png" width="900">
</p>

---

## Repository Age Distribution

<p align="center">
  <img src="images/repository_age_distribution.png" width="900">
</p>

---

## Active vs Inactive Repositories

<p align="center">
  <img src="images/active_vs_inactive_repositories.png" width="700">
</p>

---

## License Distribution

<p align="center">
  <img src="images/license_distribution.png" width="900">
</p>

---

## Stars vs Forks Relationship

<p align="center">
  <img src="images/stars_vs_forks_relationship.png" width="900">
</p>

---

## Top Repository Owners

<p align="center">
  <img src="images/top_repository_owners.png" width="900">
</p>

---

## Key Insights

- Repository metadata was collected directly from the GitHub REST API.
- The dataset includes both raw and processed versions for reproducibility.
- Feature engineering added analytical attributes that improve downstream analysis.
- Programming language distribution highlights dominant technologies.
- Repository popularity shows a strong relationship between stars and forks.
- Repository activity metrics help distinguish actively maintained projects.

---

## How to Run

Clone the repository

```bash
git clone https://github.com/your-username/github-repository-analytics.git

cd github-repository-analytics
```

Create a virtual environment

```bash
python -m venv venv

venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GITHUB_TOKEN=your_personal_access_token
```

Execute the pipeline

```bash
python src/fetch_repositories.py

python src/clean_data.py

python src/feature_engineering.py
```

Launch the notebook

```bash
jupyter notebook
```

---

## Future Improvements

- Support multiple GitHub search queries
- Automated scheduled data collection
- Docker containerization
- Logging and monitoring
- Data validation framework
- GitHub Actions CI/CD
- Automated Kaggle dataset updates
- Machine Learning models for repository popularity prediction

---

## License

This project is licensed under the MIT License.
