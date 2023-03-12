from rest_framework import serializers


class IssueSerializer(serializers.Serializer):
    url = serializers.URLField()
    number = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    author_name = serializers.CharField(max_length=255)
    author_url = serializers.URLField()
    created_at = serializers.DateTimeField()
