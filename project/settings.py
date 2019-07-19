import os

import environs


env = environs.Env()
env.read_env()

DATABASES = {
    'default': env.dj_db_url('DATABASE_URL'),
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG_MODE', default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = env.str('DJANGO_TIME_ZONE', default='Europe/Moscow')

USE_TZ = True
