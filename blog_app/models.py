# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings  # new addition

# Create your models here.
class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # Author is linked to a registered
    # user, via the User model in the auth app.
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # new addition
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen (for counter)
    tag = models.CharField(max_length=30, blank=True, null=True)  # Code for categorising posts using tags
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title