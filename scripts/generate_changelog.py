"""Fetch the 3 most recent GitHub Releases and generate docs/changelog.md."""

import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = "alperensert/capmonster_python"
API_URL = f"https://api.github.com/repos/{REPO}/releases?per_page=3"
OUTPUT = Path(__file__).resolve().parent.parent / "docs" / "changelog.md"

FRONTMATTER = """\
---
icon: history
label: Changelog
order: 50
---
"""


def fetch_releases():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(API_URL, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def format_date(iso_str: str) -> str:
    return datetime.fromisoformat(iso_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")


def build_markdown(releases: list[dict]) -> str:
    lines = [FRONTMATTER, "# Changelog\n"]

    for i, release in enumerate(releases):
        tag = release["tag_name"]
        date = format_date(release["published_at"])
        heading = f"## {tag} ({date})"
        if i == 0:
            heading += ' [!badge text="Latest"]'
        lines.append(heading)
        lines.append("")
        body = (release.get("body") or "").strip()
        # Remove the auto-generated heading (e.g. "## [4.0.0](...) (2025-04-30)")
        # that duplicates our own heading
        body = re.sub(r"^##\s+\[?\d+\.\d+\.\d+\]?[^\n]*\n*", "", body).strip()
        if body:
            lines.append(body)
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(
        "You can find other version changelogs "
        f"[here](https://github.com/{REPO}/releases).\n"
    )
    return "\n".join(lines)


def main():
    releases = fetch_releases()
    md = build_markdown(releases)
    OUTPUT.write_text(md)
    print(f"Wrote {len(releases)} releases to {OUTPUT}")


if __name__ == "__main__":
    main()
