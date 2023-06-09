"""
Django settings for proyecto_veterinaria project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2^6&3g(t4hae%*&#2+o0_y^rn$26^tj8xa-i=9s!s#u!ha!u4z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#if DEBUG:
 #   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




# Aca se agregan todas las aplicaciones que utiliza el sistema
# las "django." son propias de django y la mayoria se crearon con la estructura del proyecto
# el resto son las paginas que fueron siendo creadas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',
    'django_filters',
    'accounts',
    'dogs',
    'shifts',
    'adoptions',
    'perdidos',
    'found',

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

ROOT_URLCONF = 'proyecto_veterinaria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        'DIRS': [str(BASE_DIR.joinpath('templates'))], #le dice a Django la locacion de templates
    },
]

WSGI_APPLICATION = 'proyecto_veterinaria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))] #dice a django donde buscar archivos static en las apps

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

        
# LOGIN_REDIRECT_URL = 'home' #redirecciona al usuario en pagina 'login' a la pag ppal a traves del template "home"
# LOGOUT_REDIRECT_URL = 'login' #redirecciona al usuario en pag ppal a la pantalla login 
            #
            # LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL son constantes que emplea django.contrib.auth 
            # que funcionan bien, pero para hacer mas legible el programa decidi hacer las redirecciones de otra manera
            # 


AUTH_USER_MODEL = 'accounts.CustomUser' #customUser es el usuario personalizado base definido en accounts/models.py



"""EMAIL CREDENTIALS"""



EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'bdaee6e9ccc2b0'
EMAIL_HOST_PASSWORD = '4f92dcd51cdcfc'
EMAIL_PORT = '2525'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'megat01e28@gmail.com'

