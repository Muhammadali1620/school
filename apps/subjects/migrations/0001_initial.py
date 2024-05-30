# Generated by Django 5.0.6 on 2024-05-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('name_uz', models.CharField(max_length=70, null=True)),
                ('name_en', models.CharField(max_length=70, null=True)),
                ('name_ru', models.CharField(max_length=70, null=True)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('desc', models.CharField(max_length=320)),
                ('desc_uz', models.CharField(max_length=320, null=True)),
                ('desc_en', models.CharField(max_length=320, null=True)),
                ('desc_ru', models.CharField(max_length=320, null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Add in UZS', max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
