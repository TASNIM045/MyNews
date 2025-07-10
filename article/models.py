from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    publishing_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
    
class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Enter a rating between 1 and 5"
    )