

"""
LEARNING HOW TO CREATE MODELLEARNING HOW TO CREATE MODELSS
"""



import email
from socket import fromshare
from attr import fields
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from jmespath import search

class User(AbstractBaseUser):
    """
    Here we are setting the database table attributes
    as variables.
    """
    email           =   models.EmailField(
                        verbose_name    =   'email address',
                        max_length      =   255,
                        unique          =   True,
    )
    is_active       =   models.BooleanField(default = True)
    staff           =   models.BooleanField(default = False)
    admin           =   models.BooleanField(default = False)

    """
    Here we specify the values that should be enter on login.
    Or values to identify the user.
    """
    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   []

    """
    Methods for getting identificators of users.
    In this case the user is identified.

    Here you can add whatever methods you want
    """
    def     get_full_name(self):
        return self.email
    
    def     get_short_name(self):
        return self.email
    
    def     _str_(self):
        return self.email

    """
    Method for checking if user has some kind of permission
    """
    def     has_permission(self, perm, obj=None):
        return True
    
    """
    Method for checking if the user has permission to view
    the app 'app_label'
    """
    def     has_module_permission(self, app_label):
        return True
    
    """
    Definition of User properties
    """
    """
    Checks wether the user is part of the staff or not
    """
    @property
    def     is_staff(self):
        return self.staff
    
    """
    Method that ckecks wether the current user is an admin or not
    """
    @property
    def     is_admin(self):
        return self.admin


"""
Now we must create the user model manager.
"""
class UserManager(BaseUserManager):
    def     create_user(self, email, password=None):
        """
        Creates and saves a User with given email and password
        """
        if not email:
            raise ValueError('Users must have an email address') 
        
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def     create_staffuser(self, email, password):
        """
        Creates and saves a staff user with given email password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Create and saves a superuser with the given email and passowrd
        """
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

"""
python manage.py makemigrations
python manage.py migrate
"""

"""
On settings.py:
    AUTH_USER_MODEL = 'accounts.User

This means that we can use many third party packages that leverage
the Django user model; packages like Django rest frameword, django AllAuth,
python social auth.

And run migrations


Create a superuser
"""

from django.contrib.auth import get_user_model
User = get_user_model()





"""
Create the forms for register, change, and admin leve create

Since it was updated the AUTH_USER_MODEL, we can actually use the built-in user creation
form since its a model form based on our user model, but lets lear how to implement our
own ways
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password    = forms.CharField(widget=forms.PasswordInput)
    password_2  = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        """
        Verify Email is available
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email u taken")
        return email
    
    def clean(self):
        """
        Verify both passwords match
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passowrds must match")
    
class UserAdminCreationForm(forms.ModelForm):
    """
    Form for updating users. Inclides all the fields on the user,
    but replaces the password field with admins passsword hash
    display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'admin']

    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value.
        this is done here, rather than on the field, because the field
        does not have access to the initial value.
        """
        return self.initial["password"]





"""
UPDATE THE DJANGO ADMIN
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

"""
Removing group model from admin
"""
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    """
    The forms to add and change user instances
    """
    form = UserAdminChangeForm
    add_form = UserAdminChangeForm

    """
    Fields to be usedd in displaying user model
    these overrides the definitions on the base UaserAdmin
    That referece specific field on the auth.User
    """
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields':('admin',)}),
    )

    """
    add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    overrides get_fieldsets to use this attribute when creating a user
    """
    add_fieldsets = {
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1', 'password2')}
        ),
    }
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
