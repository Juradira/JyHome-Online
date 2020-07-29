from django.db import models

# Create your models here.
class User(models.Model):
    user_name       = models.CharField(max_length=50)
    proverb         = models.CharField(max_length=200)
    email_link      = models.EmailField(max_length=200)
    github_link     = models.URLField(max_length=200)
    facebook_link   = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
