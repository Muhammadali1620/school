import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

#(?<data>img/[a-zA-Z0-9/._-]+)
#{% static '${data}' %}

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['4f12-5-133-120-251.ngrok-free.app', '127.0.0.1', 'localhost']

CSRF_TRUSTED_ORIGINS = ['https://4f12-5-133-120-251.ngrok-free.app']


INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'django_ckeditor_5',
    'django_filters',
]

INSTALLED_APPS += [
    'apps.additionals.apps.AdditionalsConfig',
    'apps.attendances.apps.AttendancesConfig',
    'apps.general.apps.GeneralConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.exams.apps.ExamsConfig',
    'apps.users.apps.UsersConfig',
    'apps.groups.apps.GroupsConfig',
    'apps.lessons.apps.LessonsConfig',
    'apps.notices.apps.NoticesConfig',
    'apps.subjects.apps.SubjectsConfig'
     
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  

                'apps.general.context_processors.general'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


TIME_ZONE = 'Asia/Tashkent'

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'