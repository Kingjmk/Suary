import os
import django.db.models.options

django.db.models.options.DEFAULT_NAMES = django.db.models.options.DEFAULT_NAMES + ('db',)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'y#(a2(nm=98!xe48ozi-81o7r7#&8s68x6j0@323ciq&3yq%^#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
APPEND_SLASH = False

ADMINS = [('Jameel Hamdan', 'jameelhamdan99@yahoo.com')]

# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'auth',
    'media',
    'users',
    'main',
]

MIDDLEWARE = [
    'auth.backend.middleware.AuthMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_settings.urls'

WSGI_APPLICATION = '_settings.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}

# Authentication settings
REFRESH_TOKEN_EXPIRATION_PERIOD = os.getenv('REFRESH_TOKEN_EXPIRATION_PERIOD', 60 * 24 * 14)
AUTH_TOKEN_EXPIRATION_PERIOD = os.getenv('REFRESH_TOKEN_EXPIRATION_PERIOD', 60 * 24)

# Databases

DEFAULT_DATABASE = 'default'
MONGO_DATABASE = 'mongo'
MEDIA_DATABASE = 'media'

DATABASES = {
    DEFAULT_DATABASE: {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DEFAULT_DATABASE_NAME', 'main'),
        'USER': os.getenv('DEFAULT_DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DEFAULT_DATABASE_PASS', '1234'),
        'HOST': os.getenv('DEFAULT_DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DEFAULT_DATABASE_PORT', ''),
    },
    MONGO_DATABASE: {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,
                    'handlers': ['console']
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG'
                }
            }
        },
        'NAME': 'default',
        'CONN_MAX_AGE': 600,
        'CLIENT': {
            'host': os.getenv('MONGO_DATABASE_URL', 'mongodb://localhost:27017'),
            'minPoolSize': 1,
            'maxPoolSize': 100,
        }
    },
    MEDIA_DATABASE: {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,
                    'handlers': ['console']
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG'
                }
            }
        },
        'NAME': 'media',
        'CONN_MAX_AGE': 600,
        'CLIENT': {
            'host': os.getenv('MEDIA_DATABASE_URL', 'mongodb://localhost:27017'),
            'minPoolSize': 1,
            'maxPoolSize': 100,
        }
    }
}

DATABASE_ROUTERS = ['_settings.db_routers.Router', ]

# Custom
MEDIA_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'mp4', 'm4a', 'm4v', 'webm']
AVATAR_FORMATS = ['png', 'jpeg', 'jpg']
