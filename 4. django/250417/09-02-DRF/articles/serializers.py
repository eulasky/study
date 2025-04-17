from rest_framework import serializers 
from .models import Article, Comment


# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set에 활용할 댓글 데이터를 가공하는 도구
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # 기존에 있던 역참조 매니저인 comment_set의 값을 덮어쓰기
    comment_set = CommentDetailSerializer(many=True, read_only=True)


    # 새로운 필드 생성 (댓글 개수를 담기 위한 새로운 필드)
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    # SerializerMethodField의 값을 채울 함수
    def get_num_of_comments(self, obj):
        # 여기서 obj는 특정 게시글 인스턴스 (3번 게시글이면 3번 객체, ...)
        # view 함수에서 annotate 해서 생긴 새로운 속성 결과를 사용할 수 있게 됨
        return obj.num_of_comments

# 댓글의 전체 필드를 직렬화 하는 클래스
class CommentSerializer(serializers.ModelSerializer):

    # 외래키 필드 article의 데이터를 재구성하기 위한 도구
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
