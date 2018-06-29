# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title), 'My Latest Blog Post')

# Run the following command in the CLI (or terminal interface within Pycharm): "python manage.py test blog_app"
# This will run all the tests within this file