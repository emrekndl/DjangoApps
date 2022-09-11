from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Book(models.Model):
    """Book model"""

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.author}'


class Comment(models.Model):
    """Comment model"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    # commenter = models.CharField(max_length=255)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return str(self.rating)
