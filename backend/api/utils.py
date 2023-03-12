import json

from .github_api import Issue


class IssueEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Issue):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
