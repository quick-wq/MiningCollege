from os import path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ke1&cjdo123up2a)e453w-t#%k%54c*nx53b123_r(-0*-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'website.apps.WebsiteConfig',
    'authorization.apps.AuthorizationConfig',
    'personal_area.apps.PersonalAreaConfig',

    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MiningCollege.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'MiningCollege.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Настройка интернациализаций (нам интересен только язык и часовой пояс)
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Yekaterinburg'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Настройка почты
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mr.smitix@gmail.com'
EMAIL_HOST_PASSWORD = 'PASSWORD'
DEFAULT_FROM_EMAIL = 'Марченко Андрей'
DEFAULT_TO_EMAIL = 'mr.smitix@gmail.com'

# Подключаем кастомный бекенд авторизаций (для авторизацй по username и email)
AUTHENTICATION_BACKENDS = ['services.custom_auth_backend.CustomBackend']

# Настройка django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Настраиваем дирректорию для статичных файлов (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'static')

# Настраиваем дирректорию для медиа файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

# Указываем путь для поиска fixtures
FIXTURE_DIRS = (BASE_DIR,)

# Кодировка по умолчанию
DEFAULT_CHARSET = 'utf-8'

# Устанавливает первый день недели (0 - воскресенье, 1 - понедельник и так далее)
FIRST_DAY_OF_WEEK = 1

# Максимальный размер загружаемых файлов в байтах (10Мб)
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# Разрешать ли асинхронно небезопасные операций?
DJANGO_ALLOW_ASYNC_UNSAFE = False

# Настройка формата ввода даты и времени
TIME_INPUT_FORMATS = ('%H:%M',)

DATE_INPUT_FORMATS = ('%d.%m.%Y',)
DATETIME_INPUT_FORMATS = ('%d.%m.%Y %H:%M',)

DATETIME_FORMAT = ('%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S.%f')
