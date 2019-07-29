from rest_framework import serializers
from hackernews.models import News, Comment


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title', 'link'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'news', 'comment'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = [
            'news', 'comment', 'author'
        ]


        # def create(self, validated_data):
        #     author = self.context.get("id")
        #     comment = Comment.objects.create(author=author, **validated_data)
        #     comment.save()
        #     return comment