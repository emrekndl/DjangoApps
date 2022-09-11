from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment
from books.api.permissions import IsAdminUserOrReadOnly, IsCommenterOrReadOnly
from books.api.pagination import LargePagination, SmallPagination

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin


class BookListCreateAPIView(generics.ListCreateAPIView):
    """ List all books or create a new book """

    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a book """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    """ Create a new comment """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Override the default perform_create method
        'books/<int:book_pk>/comment'
        Save the comment with related book
        """

        book = get_object_or_404(Book, pk=self.kwargs.get('book_pk'))
        if Comment.objects.filter(book=book, commenter=self.request.user).exists():
            raise ValidationError('You have already commented this book')
        serializer.save(book=book, commenter=self.request.user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a comment """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommenterOrReadOnly]
    # permission_classes = [permissions.IsAdminUser]


class CommentListAPIView(generics.ListAPIView):
    """ List all comments """

    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LargePagination
    # permission_classes = [permissions.IsAdminUser]


# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """ Book Create List Generic API View and Mixins """

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         """  Get all books """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """ Create a new book """
#         return self.create(request, *args, **kwargs)
