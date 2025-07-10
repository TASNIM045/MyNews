from article.models import Article, Category
from article.serializers import ArticleSerializer, CategorySerializer
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