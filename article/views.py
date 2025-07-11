from article.models import Article, Category, Rating
from article.serializers import ArticleSerializer, CategorySerializer, RatingSerializer
from rest_framework.viewsets import ModelViewSet
from article.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from article.permissions import IsReviewAuthorOrReadOnly


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
    serializer_class = RatingSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Rating.objects.filter(article_id=self.kwargs.get('article_pk'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['article_id'] = self.kwargs.get('article_pk')
        return context
