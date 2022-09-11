## Sample Bookstore REST API App - Django Rest Framework - GenericAPIView
<br />
<p align="center">

<table>
<tr><td>
<img src="images/Book-List-Create-Api.png" width="650" height="350" alt=""></td><td>
<img src="images/Book-Detail-Api.png" width="650" height="350" alt=""></td></tr><tr><td>
<img src="images/Comment-Detail-Api-without-login.png" width="650" height="350" alt=""></td><td>
<img src="images/Comment-Detail-Api.png" width="650" height="350" alt=""></td>
</tr><tr>
<td colspan="2">
<img src="images/Comment-Create-Api.png" width="650" height="350" alt=""></td></tr>
</table>
</p>
<br />

###### API Usage
- /api/books/
* Book create-post, list-get
- /api/books/id/
* A book update-put, delete-delete
- /api/books/book_pk/comment/
* Create a comment to related book
- /api/comments/
* Commeent list-get
- /api/comments/id/
* A comments update-put, delete-delete
<br/>


### Installing

- To get this repository, run the following commands inside your terminal

```bash
svn export https://github.com/emrekndl/DjangoApps/trunk/RestGenericApiBooksApp
```

```bash
cd RestGenericApiBooksApp
```

```bash
pip3 install -r requirements.txt
```

```bash
cd bookstore_app
```

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

```bash
python3 manage.py createsuperuser
```

```bash
python3 manage.py runserver
```

###### Tools
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
<br>
[Django Rest Framework](https://www.django-rest-framework.org/)

