from rest_framework import serializers
from article.models import Article, Category, Rating
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'headline', 'body', 'category', 'publishing_time']

class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_current_username')
    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_username(self, obj):
        return obj.get_full_name()

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')

    class Meta:
        model = Rating
        fields = ['id', 'article', 'rating', 'user']
        read_only_fields = ['article', 'user']
        

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        article = Article.objects.get(pk=self.context['article_id'])
        validated_data['article'] = article
        return super().create(validated_data)