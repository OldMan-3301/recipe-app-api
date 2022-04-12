from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
                            

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=_db)

        return user