## REST API App - Django Rest Framework - Authenticaiton
<br />
<p align="center">

<table>
<tr><td>
<img src="images/drfauthapp.gif" width="650" height="350" alt=""></td><td>
</tr>
</table>
</p>
<br />

###### API Usage
- /api/user-profiles
* User Profiles, list-get
- /api/profile-state
* A User Profile States, list-get
- /api/profile-image/
* Add A User Profile Image
<br/>


### Installing

- To get this repository, run the following commands inside your terminal

```bash
svn export https://github.com/emrekndl/DjangoApps/trunk/DRFAuthentication
```

```bash
cd DRFAuthenticaiton
```

```bash
pip3 install -r requirements.txt
```

```bash
cd core
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

