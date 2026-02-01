import requests
import json

GITHUB_USER = "amishhaa"
data = []

def fetch_github():
    url = f"https://api.github.com/search/issues?q=author:{GITHUB_USER}+type:pr"
    r = requests.get(url).json()
    for item in r.get("items", []):
        repo_url = item["repository_url"]
        repo = requests.get(repo_url).json()

        data.append({
            "title": item["title"],
            "source": "github",
            "status": item["state"],
            "link": item["html_url"],
            "date": item["created_at"][:10],
            "org": repo["owner"]["login"],
            "logo": repo["owner"]["avatar_url"]
        })

def fetch_git_kernel():
    data.append({
        "title": "My Git Project Patches",
        "source": "git-kernel",
        "status": "mailing list",
        "link": "https://lore.kernel.org/git/?q=amishhhaaaa",
        "date": "",
        "org": "git",
        "logo": "https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png"
    })

fetch_github()
fetch_git_kernel()

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

