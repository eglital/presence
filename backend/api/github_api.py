from dataclasses import dataclass
import datetime
from typing import List
import requests


@dataclass
class Issue:
    url: str
    number: int
    title: str
    author_name: str
    author_url: str
    created_at: datetime

    @staticmethod
    def create_from_response(issue):
        return Issue(
            url=issue.get("html_url"),
            number=issue.get("number"),
            title=issue.get("title"),
            author_name=issue.get("user", {}).get("login"),
            author_url=issue.get("user", {}).get("html_url"),
            created_at=issue.get("created_at"),
        )


class GithubAPI:
    def __init__(self, repo_owner: str, repo_name: str):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

    def get_issues_list(self) -> List[Issue]:
        url = f"{self.base_url}/issues"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                f"Failed to get issues from {url}, status code: {response.status_code}"
            )
        issues = response.json()
        return [Issue.create_from_response(issue) for issue in issues]
