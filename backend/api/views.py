import json

from .utils import IssueEncoder
from .github_api import GithubAPI
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class GithubIssuesCollection(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        owner = request.query_params.get("owner", "Microsoft")
        name = request.query_params.get("name", "vscode")
        issues = GithubAPI(owner, name).get_issues_list()
        return Response(
            status=status.HTTP_200_OK,
            data={"issues": json.dumps(issues, cls=IssueEncoder)},
        )
