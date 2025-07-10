from django.urls import path, include
from rest_framework_nested import routers
from article.views import ArticleViewSet, CategoryViewSet, RatingViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('users', UserViewSet, basename='users')


articles_router = routers.NestedDefaultRouter(router, 'articles', lookup='article')
articles_router.register('ratings', RatingViewSet, basename='article-ratings')

urlpatterns = [
    path('', include(router.urls)),           
    path('', include(articles_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
