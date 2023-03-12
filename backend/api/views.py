from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import IssueSerializer
from .github_api import GithubAPI


class GithubIssuesCollection(APIView):
    def get(self, request, *args, **kwargs):
        owner = request.query_params.get("owner")
        name = request.query_params.get("name")
        if not name or not owner:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        issues = GithubAPI(owner, name).get_issues_list()
        serializer = IssueSerializer(issues, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )
