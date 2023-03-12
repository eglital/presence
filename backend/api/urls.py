from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path(
        "github-issues/",
        views.GithubIssuesCollection.as_view(),
        name="github-issues",
    )
]
