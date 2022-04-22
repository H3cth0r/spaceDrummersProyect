
from pyexpat import model
from statistics import mode
# from django.db import models

# Create your models here.

# """
#     Creating custom Model for user

#     First we import the auth models:
#         - BaseUserMananager : for the user manager class
#         - AbstractBaseUser  : for the user class
# """
# from django.contrib.auth.models import (
#     BaseUserManager,
#     AbstractBaseUser
# )




# """


# class User(models.Model):
#     name = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=60)
#     age = models.IntegerField(max_length=3)
#     email = models.CharField(max_length=60)
#     hashedPwd = models.CharField()
#     country = models.CharField(max_length=20)
#     gender = models.CharField(max_length=10)
#     admim = models.CharField()
#     last_Login = models.CharField()

# class Gameprofile(models.Model):
#     username = models.CharField()
#     currentLevel = models.IntegerField()

# """

# class MyUserManager(BaseUserManager):
#     def                 create_user(self, t_name, t_lastName, t_age, t_email, t_password, t_country):
#         if not  t_name:
#             raise   ValueError("Users must have an email.")
#         if not  t_lastName:
#             raise   ValueError("User must have a last name.")
#         if not  t_age:
#             raise   ValueError("User must have an age.")
#         if not  t_email:
#             raise   ValueError("User must have an email.")
#         if not  t_password:
#             raise   ValueError("User must have a password.")
#         if not  t_country:
#             raise   ValueError("User must have a country")
        
#         user = self.model(
#             name        =   t_name,
#             lastName    =   t_lastName,
#             age         =   t_age,
#             email       =   self.normalize_email(t_email),
#             password    =   t_password,
#             country     =   t_country,
#             is_admin    =   False,
#         )

#         user.set_password(t_password)
#         user.save(using=self._db)
#         return user
    
#     def                 create_superuser(self, t_name, t_lastName, t_age, t_email, t_password, t_country):  
#         user = self.create_user(
#             t_name        =   t_name,
#             t_lastName    =   t_lastName,
#             t_age         =   t_age,
#             t_email       =   self.normalize_email(t_email),
#             t_password    =   t_password,
#             t_country     =   t_country,
#             t_is_admin    =   True
#         )

#         user.save(using=self._db)
#         return user


# """
# AbstractUser
# provides full implementation of the default User as an abstract model,
# whicj means you'll get the compelte fields which come with User model 
# plus the fields that you define.
# Has the authentication functionality only, it has no actual fields, you
# will supply the fields to use when you subclass.
# You also have to tell it what field will represents the username, the
# fields that are required, and how tthose users will be managed.
# Lets say you wan to use email in yout authentication, Django normally
# uses username in authentication, so how do you change it to use email?
# """
# class MyUser(AbstractBaseUser):
#     """
#     Declaring User Atributes
#     """
#     name                =   models.CharField(max_length=30,                                             db_column='name')
#     lastName            =   models.CharField(max_length=30,                                             db_column='lastName')
#     age                 =   models.IntegerField(                                                        db_column='age')                # is unique
#     email               =   models.EmailField(verbose_name='email address', max_length=255, unique=True,db_column='email')
#     password            =   models.CharField(max_length=100,                                            db_column='hashedPwd')
#     # date_of_birth     =   models.DateField()
#     country             =   models.CharField(max_length=30,                                             db_column='country')
#     gender              =   models.CharField(max_length=20,                                             db_column='gender')
#     admin               =   models.BooleanField(default=False,                                          db_column='admin')

#     objects             =   MyUserManager()

#     USERNAME_FIELD      =   'email'
#     REQUIRED_FIELDS     =   []

#     class               Meta(AbstractBaseUser.Meta):
#         db_table        =   'User'

#     """
#     Methods
#     """
#     def                 __str__(self):
#         return              self.email

#     def                 has_perm(self, perm, obj=None):
#         return              self.admin