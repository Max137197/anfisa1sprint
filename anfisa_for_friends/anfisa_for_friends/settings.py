import os
from pathlib import Path

# Путь к корню проекта (где лежит manage.py: ANFISA1SPRINT)
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (для учебного проекта можно оставить так,
# в продакшене нужно выносить в переменные окружения)
SECRET_KEY = 'django-insecure-oy%f52n92s=%3&b3dh&h)f(b4ag^_z*&3w+ooo!sy-g=449bwn'

# Режим отладки
DEBUG = True

ALLOWED_HOSTS = []

# Приложения проекта
INSTALLED_APPS = [
    'anfisa_for_friends.homepage.apps.HomepageConfig',
    'anfisa_for_friends.ice_cream.apps.IceCreamConfig',
    'anfisa_for_friends.about.apps.AboutConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой urls
ROOT_URLCONF = 'anfisa_for_friends.urls'

# Папка с шаблонами: ANFISA1SPRINT/templates
TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # ищем шаблоны в папке templates на уровне manage.py
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'anfisa_for_friends.wsgi.application'

# База данных (SQLite по умолчанию)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статика: папка static_dev рядом с manage.py
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

# Куда собирать статику при деплое
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Медиа (если будут)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Тип поля авто‑id
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
