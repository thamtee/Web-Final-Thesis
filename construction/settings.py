"""
Django
settings
for'construction project.

Generated
by
'django-admin startproject'
using
Django
1.10
.3.

For
more
information
on
this
file, see
https: // docs.djangoproject.com / en / 1.10 / topics / settings /

For
the
full
list
of
settings and their
values, see
https: // docs.djangoproject.com / en / 1.10 / ref / settings /
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r2o62(wcm(+lseh#a45m5z9w8ht_c4&t83mjs!mo@-7ene!7l3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    # 'django_stormpath',

    'construction',
    'reportConstruction',
]

# Stormpath Setting
# AUTHENTICATION_BACKENDS = (
#     'django_stormpath.backends.StormpathBackend',    
#     'django_stormpath.backends.StormpathIdSiteBackend',
#     'django_stormpath.backends.Stormpath.SocialBackend',
# )

# # AUTH_USER_MODEL = 'django_stormpath.StormpathUser'

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

# STORMPATH_ID = '6GTHPSFNUBSADHYYEECCE3OQX'
# STORMPATH_SECRET = 'qN+it57grKYMnQtNotumvofvnv+pk28VCsR5hUb5rRo'
# STORMPATH_APPLICATION = 'https://api.stormpath.com/v1/applications/3Fs7hhRZf62m6xjFy80K1e'

# STORMPATH_ENABLE_FACEBOOK = True

# STORMPATH_SOCIAL = {
#     'FACEBOOK': {
#         'client_id': os.environ['1346565105353812'],
#         'client_secret': os.environ['222c1b18e8fb79b77d530b7a12b9a95f']
#     },
# }

# END STORMPATH SETTING

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'construction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'construction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'