from django.shortcuts import render
from .models import Category, Movie


def home(request):
    data = {
        'categories': Category.objects.all(),
        'movies': Movie.objects.filter(homepage=True),
        }
    return render(request, 'index.html', context=data)


def movies(request):
    data = {
        'categories': Category.objects.all(),
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies.html', context=data)


def movie_details(request, id):
    data = {
        'movie': Movie.objects.get(id=id),
        }
    return render(request, 'movie_details.html', context=data)

# category_list = ['Action', 'Drama', 'Thriller']

# movie_list = [
#     {
#         'id': 1,
#         'title': 'The Shawshank Redemption',
#         'category': 'Drama',
#         'year': '1994',
#         'poster': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
#         'homepage': True
#     },
#     {
#         'id': 2,
#         'title': 'The Prestige',
#         'category': 'Drama',
#         'year': '2006',
#         'poster': 'thePrestige.jpg',
#         'homepage': True,
#     },
#     {
#         'id': 3,
#         'title': 'Shutter Island',
#         'category': 'Thriller',
#         'year': '2010',
#         'poster': 'https://m.media-amazon.com/images/M/MV5BYjhmMDE4ZjktNDAxZC00MDgwLWI2YjQtNzIzNWY1MjU4OWJkXkEyXkFqcGdeQXVyOTU2NDAzNDE@._V1_.jpg',
#         'homepage': False,
#     },
#     {
#         'id': 4,
#         'title': 'The Purge',
#         'category': 'Thriller',
#         'year': '2013',
#         'poster': 'https://m.media-amazon.com/images/M/MV5BMTQzNTcwODEyM15BMl5BanBnXkFtZTcwMjM1MDI0OQ@@._V1_.jpg',
#         'homepage': False,
#     },
#     {
#         'id': 5,
#         'title': 'Sicario',
#         'category': 'Action',
#         'year': '2015',
#         'poster': 'https://m.media-amazon.com/images/M/MV5BMjA5NjM3NTk1M15BMl5BanBnXkFtZTgwMzg1MzU2NjE@._V1_.jpg',
#         'homepage': True,
#     }
# ]