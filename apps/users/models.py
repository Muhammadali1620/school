from django.db import models
from apps.groups.services import normalize_text
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from apps.users.validators import phone_validate


# class Religion(models.Model):
#     name = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name


class CustomUser(AbstractUser):

    class GenderChoices(models.TextChoices):
        man = 'MAN'
        woman = 'WOMAN'

    class StatusChoices(models.TextChoices):
        admin = 'admin'
        teacher = 'teacher'
        student = 'student'
        perent = 'perent'
    
    username = None
    objects = CustomUserManager()

    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70)
    mother_name = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    date_of_birth = models.DateField()
    student_group = models.ForeignKey('groups.StudentGroup', on_delete=models.PROTECT, blank=True, null=True,
                              related_name='group_users', related_query_name='group_users')
    # subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
    #                             related_name='sbject_users', related_query_name='sbject_users')
    bio = models.TextField(max_length=1500)
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    payment = models.DecimalField(max_digits=20, decimal_places=2)
    selary = models.DecimalField(default=0, max_digits=20, decimal_places=2)
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

    @classmethod
    def get_normalize_fields(cls):
        return ['first_name', 'last_name', 'father_name', 'mother_name', 'address', 'bio']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)