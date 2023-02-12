from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .resources import CATEGORY, TYPE_OF_POST, news


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0)

    def update_rating(self):
        self.rating = 0
        for post in Post.objects.filter(author_id=self.id):
            self.rating += post.rating * 3
            for comment in Comment.objects.filter(post_id=post.id):
                self.rating += comment.rating
        for comment in Comment.objects.filter(user_id=self.user):
            self.rating += comment.rating
        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    category_name = models.CharField(max_length=100, choices=CATEGORY, default='news', unique=True)


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=TYPE_OF_POST, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating = self.rating + 1
        self.save()

    def dislike(self):
        self.rating = self.rating - 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.title}: {self.text[:124] + "..."}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_data_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0)

    def like(self):
        self.comment_rating = self.comment_rating + 1
        self.save()

    def dislike(self):
        self.comment_rating = self.comment_rating - 1
        self.save()

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py shell
# venv\scripts\activate
# from news_models.models import *
