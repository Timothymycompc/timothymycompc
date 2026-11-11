"""Keeps the profile README's numbers and latest-reports list in step with GitHub, so they never go stale.

Counted from GitHub search (real data only):
- issues_filed: issues I opened in other people's repos
- fixes: distinct repos where a "version 1" report of mine was closed as completed (fixed)
- merged_PRs: my merged pull requests
- latest list: my 8 newest issues in other people's repos, with their state
Runs in GitHub Actions (.github/workflows/stats.yml) with the built-in GITHUB_TOKEN; stdlib only.
"""
import json, os, re, urllib.parse, urllib.request

ME = "Timothymycompc"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def search(q, per_page=100):
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": q, "per_page": per_page, "sort": "created", "order": "desc"})
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-stats",
                                               **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def repo_of(item):
    return item["repository_url"].split("/repos/", 1)[1]


issues = search(f"author:{ME} type:issue -user:{ME}")
fixed = search(f'author:{ME} type:issue -user:{ME} is:closed reason:completed "version 1"')
merged = search(f"author:{ME} type:pr is:merged")

n_issues = issues["total_count"]
n_fixed = len({repo_of(i) for i in fixed["items"]})
n_merged = merged["total_count"]

rows = []
for i in issues["items"][:8]:
    state = "fixed" if i["state"] == "closed" and i.get("state_reason") == "completed" else (
        "closed" if i["state"] == "closed" else "open")
    title = i["title"].replace("|", "/")
    rows.append(f"| {i['created_at'][:10]} | [{repo_of(i)}#{i['number']}]({i['html_url']}) | {title} | {state} |")
latest = ("<!-- latest:start -->\n| Date | Issue | What it's about | State |\n|---|---|---|---|\n" + "\n".join(rows) +
          f"\n\n<sub>Updated automatically from GitHub: {n_issues} issues filed, {n_fixed} projects fixed a bug I reported, "
          f"{n_merged} merged PRs.</sub>\n<!-- latest:end -->")

p = "README.md"
s = open(p).read()
s = re.sub(r"issues_filed-\d+-", f"issues_filed-{n_issues}-", s)
s = re.sub(r"upstream_fixes_from_my_reports-\d+_projects", f"upstream_fixes_from_my_reports-{n_fixed}_projects", s)
s = re.sub(r"merged_PRs-\d+-", f"merged_PRs-{n_merged}-", s)
s = re.sub(r"<!-- latest:start -->.*?<!-- latest:end -->", lambda _: latest, s, flags=re.S)
open(p, "w").write(s)
print(f"issues={n_issues} fixed={n_fixed} merged={n_merged} latest={len(rows)}")
