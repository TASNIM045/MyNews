from article.models import Article, Category, Rating
from article.serializers import ArticleSerializer, CategorySerializer, RatingSerializer
from rest_framework.viewsets import ModelViewSet
from article.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def __str__(self):
        return f"Rating by {self.user.first_name}."