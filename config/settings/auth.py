AUTHENTICATION_BACKENDS = [
    'apps.users.backends.CustomBackend',
]

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'users:login'