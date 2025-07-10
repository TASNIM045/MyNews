from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article.views import ArticleViewSet, CategoryViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('users', UserViewSet, basename='users')



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
