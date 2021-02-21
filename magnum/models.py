from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
  email = models.EmailField()
  username = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'username'

  class Meta:
    abstract = False

  def __str__(self):
    return str(self.username)
