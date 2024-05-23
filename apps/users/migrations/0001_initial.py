# Generated by Django 5.0.6 on 2024-05-23 10:53

import apps.users.managers
import apps.users.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('status', models.CharField(choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student'), ('perent', 'Perent')], max_length=20)),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[apps.users.validators.phone_validate])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('father_name', models.CharField(max_length=70)),
                ('mother_name', models.CharField(blank=True, max_length=70)),
                ('address', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman')], max_length=20)),
                ('date_of_birth', models.DateField()),
                ('bio', models.TextField(max_length=1500)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('selary', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('image', models.ImageField(upload_to='user/student')),
                ('zip_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('student_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='group_users', related_query_name='group_users', to='groups.studentgroup')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-pk'],
            },
            managers=[
                ('objects', apps.users.managers.CustomUserManager()),
            ],
        ),
    ]
