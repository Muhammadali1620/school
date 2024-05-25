# Generated by Django 5.0.6 on 2024-05-25 06:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('in_percent', models.BooleanField(default=False)),
                ('slelery', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(limit_choices_to={'status': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_payment', related_query_name='student_payment', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'status': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_payment', related_query_name='teacher_payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('year', 'month', 'student', 'teacher')},
            },
        ),
    ]
