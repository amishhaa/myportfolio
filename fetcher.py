import requests
import json

GITHUB_USER = "amishhaa"

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

# ---------- Git (kernel.org) patches ----------
def fetch_git_kernel():
    data.append({
        "title": "My Git project patches",
        "source": "git-kernel",
        "status": "mailing list",
        "link": "https://lore.kernel.org/git/?q=amishhhaaaa",
        "date": ""
    })

fetch_github()
fetch_git_kernel()

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated data.json")

