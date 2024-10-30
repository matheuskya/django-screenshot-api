from django.contrib.auth.models import Group, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields=['url', 'name']

class ScreenshotRequestSerializer(serializers.Serializer):
    url = serializers.URLField()
    viewport_width = serializers.IntegerField(default=1200)
    viewport_height = serializers.IntegerField(default=720)
    full_page = serializers.BooleanField(default=False)
