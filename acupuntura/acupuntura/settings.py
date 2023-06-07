from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8%ql#_^_44wy^fdnc9sk2a@0sdvjesgbmy%)yj)j55kpoy*h0!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "puntos",
    "tema",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'bootstrap4',
    'crispy_forms',
    'ckeditor',
    'rest_framework',    
    'simple_history',
    'fontawesomefree',
    'colorfield',
    'betterforms',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "acupuntura.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "acupuntura.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {        
        "ENGINE": os.environ.get("ACUPUNTURA_SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("ACUPUNTURA_SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("ACUPUNTURA_SQL_USER", "user"),
        "PASSWORD": os.environ.get("ACUPUNTURA_SQL_PASSWORD", "password"),
        "HOST": os.environ.get("ACUPUNTURA_SQL_HOST", "localhost"),
        "PORT": os.environ.get("ACUPUNTURA_SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_URL = "static/"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static') 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

CKEDITOR_BASEPATH =  os.path.join(STATIC_ROOT,"ckeditor/ckeditor/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

