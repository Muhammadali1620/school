# Generated by Django 5.0.6 on 2024-05-28 09:02

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.CharField(max_length=255)),
                ('sender_phone_number', models.CharField(max_length=255)),
                ('sender_fullname', models.CharField(max_length=255)),
                ('recipient_email', models.CharField(max_length=255)),
                ('recipient_phone_number', models.CharField(max_length=255)),
                ('recipient_fullname', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('viewed', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_recipient', related_query_name='messages_recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sender', related_query_name='messages_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.PositiveSmallIntegerField(choices=[(0, 'EXAM_RESULT'), (1, 'ON_ATTENDANCE'), (2, 'STUDENT_PAYMENT'), (3, 'SALARY'), (4, 'ACCOUNT'), (5, 'FINE'), (6, 'WARNING')])),
                ('is_viewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('exam_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.examresult')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
