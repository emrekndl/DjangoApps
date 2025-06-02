## Todo App - Django
<br />
<p align="center">
<img src="images/todoAppDjango.png"  height="350" width="650" >
<br />
A simple todo app built with django
</p>
<br />
<br />

## Setup

To get this repository, run the following commands inside your terminal

```bash
$ git clone https://github.com/emrekndl/todoAppDjango.git
```

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

```bash
$ python manage.py createsuperuser
```

```bash
$ python manage.py runserver
```

###### Runing with Dockerfile

```bash
docker build . -t django-app-v1
```

```bash
docker run -p 8001:8000 django-app-v1
```
