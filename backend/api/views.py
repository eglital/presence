from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class GithubIssuesCollection(GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={"data": "sample"})
