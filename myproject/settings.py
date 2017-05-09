"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-q@x+fbn4vl-+qs!*a=+(u%j1w76z_(7re-1*b+yb&a+rj=-&+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


CAS_SERVER_URL = 'https://fed.princeton.edu/cas/'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'django_cas_ng.backends.CASBackend',)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myproject.myapp',
    'django_cas_ng',
    'star_ratings',
    's3direct',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_cas_ng.middleware.CASMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'myproject', 'myapp', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # Haochen's settings
         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
         # 'NAME': 'test1',
         # 'USER': 'iamauser',
         # 'PASSWORD': 'md5b616d86bca63a780a9f5561c0a40ca10',
         # 'HOST': 'localhost',
         # 'PORT': '5432',

        # Yuyan's settings
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
}
}


S3DIRECT_DESTINATIONS = {
    # Allow anybody to upload any MIME type
    'videos': {
        'key': '/',
        'allowed': ['video/mp4','video/quicktime']
    },
}



import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

AWS_ACCESS_KEY_ID = 'AKIAJRO56I6N42GTRMFQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'princetonuniversityfilmsharing'
S3DIRECT_REGION = 'us-east-2'
    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.

  # This is used by the `static` template tag from `static`, if you're using that. Or if anything else

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'myproject.custom_storages.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATIC_URL = '/static/'
    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_S3_CUSTOM_DOMAIN = "s3.%s.amazonaws.comus-east-2.amazonaws.com/%s" % (S3DIRECT_REGION, AWS_STORAGE_BUCKET_NAME)

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# DEFAULT_FILE_STORAGE = 'myproject.s3util.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'myproject.s3util.StaticRootS3BotoStorage'

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.8/howto/static-files/
# # STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.8/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# # Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
   os.path.join(PROJECT_ROOT, 'myapp','static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/" % (AWS_S3_CUSTOM_DOMAIN)
DEFAULT_FILE_STORAGE = 'myproject.custom_storages.MediaStorage'
