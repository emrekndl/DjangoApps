from django.db import models


class Author(models.Model):
    """ Author model """

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=120)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    """ Model for articles """

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_articles')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    text = models.TextField()
    city = models.CharField(max_length=100)
    pub_date = models.DateField()
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
