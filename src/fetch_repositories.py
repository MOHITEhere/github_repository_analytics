import os
import json
import requests
from tqdm import tqdm

from config import GITHUB_TOKEN, BASE_URL


headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


url = f"{BASE_URL}/search/repositories"

all_repositories = []

for page in tqdm(range(1, 11), desc="Fetching Pages"):

    params = {
        "q": "stars:>1000",
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
        "page": page
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:

        data = response.json()

        all_repositories.extend(data["items"])

    else:

        print("Error:", response.text)
        break


print(f"\nTotal repositories fetched: {len(all_repositories)}")

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/repositories_raw.json", "w", encoding="utf-8") as file:
    json.dump(all_repositories, file, indent=4)

print("\nRaw JSON saved successfully!")