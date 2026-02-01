import requests
from bs4 import BeautifulSoup
import json

GITHUB_USER = "amishhaa"
EMAIL = "amishhhaaaa@gmail.com"

data = []

# ---------- GitHub PRs ----------
def fetch_github():
    url = f"https://api.github.com/search/issues?q=author:{GITHUB_USER}+type:pr"
    r = requests.get(url).json()
    for item in r.get("items", []):
        data.append({
            "title": item["title"],
            "source": "github",
            "status": item["state"],
            "link": item["html_url"],
            "date": item["created_at"]
        })

# ---------- Kernel patches ----------
def fetch_kernel():
    url = f"https://lore.kernel.org/all/?q=from:{EMAIL}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) >= 3:
            title = cols[1].text.strip()
            date = cols[0].text.strip()
            link = "https://lore.kernel.org" + cols[1].find("a")["href"]

            data.append({
                "title": title,
                "source": "kernel",
                "status": "submitted",
                "link": link,
                "date": date
            })

fetch_github()
fetch_kernel()

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated data.json")
