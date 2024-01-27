from django.db import models
from .auth import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='imgs')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField()


class Friend(models.Model):
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='follower')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    is_confirmed = models.BooleanField(default=False)


class AddExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Company = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    year = models.DateTimeField(auto_now=True)
    month = models.DateTimeField(auto_now=True)
    year_t0 = models.DateTimeField(auto_now=True)
    month_to = models.DateTimeField(auto_now=True)
    locitions = models.CharField(max_length=256)
    desc = models.TextField()


class PostImgs(models.Model):
    img = models.FileField(upload_to='imgs')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
