from rest_framework import serializers
from .models import Article


# 전체 게시글 데이터를직렬화 하는 클래스
# 게시글의 일부 필드를 직렬화
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = ('id', 'title', 'content',)

# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
