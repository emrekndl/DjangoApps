import os
import random
import django

from django.contrib.auth.models import User
from books.api.serializers import BookSerializer

from faker import Faker
import requests

# django settings for project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_app.settings")
django.setup()


def set_user():
    """ create demo users """
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name}_{l_name}'
    email = f'{u_name}@{fake.domain_name()}'

    print('111...:::', f_name, l_name, u_name, email)

    while User.objects.filter(username=u_name).exists():
        u_name = f'{u_name}_{random.randint(1, 100)}'
        email = f'{u_name}@{fake.domain_name()}'

    print('222...:::', f_name, l_name, u_name, email)

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )
    user.set_password('django123.')
    user.save()
    print('User created.', u_name)


def add_book(sub):
    """ create demo books """
    fake = Faker(['en_US'])
    url = 'http://openlibrary.org/search.json'
    payload = {'q': sub}
    res = requests.get(url, params=payload)

    if res.status_code != 200:
        print('request error: ', res.status_code)
        return

    jsn = res.json()
    books = jsn.get('docs')

    for book in books:
        data = dict(
                name=book.get('title'),
                author=book.get('author_name')[0],
                description=book.get('person'),
                pub_date=fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
        )

        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Book Saved: ', book.get('title'))
        else:
            continue


def main():
    set_user()
    add_book('lord of the rings')


if __name__ == '__main__':
    main()
