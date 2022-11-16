from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Group, Comment

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    #author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(required=False, queryset=Group.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', "image", 'group', 'pub_date')
