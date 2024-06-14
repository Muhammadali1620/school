from django.db import models
from apps.general.models import AbstractModel
from apps.groups.services import normalize_text
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from apps.users.validators import phone_validate
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# class Religion(models.Model):
#     name = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name


class CustomUser(AbstractUser, AbstractModel):

    class GenderChoices(models.TextChoices):
        man = 'MAN'
        woman = 'WOMAN'

    class StatusChoices(models.IntegerChoices):
        admin = 1, 'admin'
        teacher = 2, 'teacher'
        student = 3, 'student'
        parent = 4, 'parent'
    
    username = None
    objects = CustomUserManager()

    is_spam = models.BooleanField(default=False)

    status = models.PositiveSmallIntegerField(choices=StatusChoices.choices)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70)
    mother_name = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    date_of_birth = models.DateField()
    bio = models.TextField(max_length=1200)
    student_group = models.ForeignKey('groups.StudentGroup', on_delete=models.PROTECT, blank=True, null=True, related_name='user')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, blank=True, null=True, related_name='teacher')
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    salary = models.DecimalField(default=0, max_digits=20, decimal_places=2, help_text='add in UZS',
                                 validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='user/student', blank=True, null=True)
    zip_code = models.PositiveSmallIntegerField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        super().clean()
        if self.status == self.StatusChoices.teacher.value and self.salary <= 0:
            raise ValidationError({'salary':'A teacher should have a salary'})
        if self.status == self.StatusChoices.student.value and self.student_group is None:
            raise ValidationError('StudentGroup must be provided for student')
        if self.status == self.StatusChoices.parent.value and self.child is None:
            raise ValidationError('Child must be provided for Pare nt')  
        if self.status == self.StatusChoices.teacher.value and not self.subject:
            raise  ValidationError({'subject':'Subject must be provided for teacher'})
    
    class Meta:
        ordering = ['-pk']

    @classmethod
    def get_normalize_fields(cls):
        return ['first_name', 'last_name', 'father_name', 'mother_name', 'address', 'bio']
    
    def __str__(self):
        return f'{self.get_status_display()}: {self.first_name} {self.last_name}'