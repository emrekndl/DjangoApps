from rest_framework import serializers
from books.models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment objects."""

    commenter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ["book"]


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book objects."""

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
