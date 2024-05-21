from apps.group.models import Group, Subject
from django.db import models
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from apps.users.validators import phone_validate


class Relegion(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = None
    objects = CustomUserManager()

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], blank=True)
    address = models.CharField(max_length=300, blank=True)
    gender = models.Choices()
    birth = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT,
                              related_name='users', related_query_name='users')
    religion = models.ForeignKey(Relegion, on_delete=models.SET_NULL, null=True,
                                related_name='users', related_query_name='users')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                related_name='users', related_query_name='users')
    status = models.Choices()
    bio = models.TextField()
    payment = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='user/student')
    zip_code = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-pk']