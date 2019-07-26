from rest_framework import serializers
from hackernews.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title', 'link'
        ] 