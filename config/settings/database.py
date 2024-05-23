from .base import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'school_db',
        'USER': 'muhammadali',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}