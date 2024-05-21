import sys

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'some random string, this is only crucial for production server'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# noinspection PyUnresolvedReferences
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # for MySQL option
        'NAME': 'lida',  # corresponds to the database running on local
        'USER': 'root',  # corresponds to the database running on local
        'PASSWORD': 'password',  # corresponds to the database running on local
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

if 'test' in sys.argv:
    # I have experienced that sqlite backend was considerably faster when running
    # unit tests, to whenever `manage.py` is run with 'test' argument, backend
    # changes to sqlite
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': str(Path(__file__).resolve().parent.parent / 'test_db.sqlite'),
    }
