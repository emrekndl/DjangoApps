from django.urls import path
# from news_app.api import views as api_views
from news_app.api.views import ArticleListCreateAPIView, ArticleDetailAPIView, AuthorListCreateAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
]

# urlpatterns = [
#     path('articles/', api_views.article_list_create_api_view, name='article_list'),
#     path('articles/<int:pk>/', api_views.article_detail_api_view, name='article_detail'),
# ]
