from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['inputed_name']) < 5:
            errors["name"] = "Name has to be at least 5 characters"
        if len(postData['inputed_desc']) < 15:
            errors["desc"] = "Description has to be at least 15 characters"
        return errors;

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {}>".format(self.name) 