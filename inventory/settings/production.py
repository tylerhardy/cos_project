# -*- coding: utf-8 -*- 
from .base import * 

SECRET_KEY = '75jele&o5ftncyfx#0p&ttmjcl635r3j1r3oipv##b0q0o7o20'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '137.190.117.94']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

=======
DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
>>>>>>> 8d50c88a78994a4104df87f506c7dc8824f5b5a5
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cos_inv_db',
        'USER': 'tylerhardy',
        'PASSWORD': 'Letmein11',
        'HOST': 'localhost',
        'PORT': '',
    }
<<<<<<< HEAD
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
=======
}
>>>>>>> 8d50c88a78994a4104df87f506c7dc8824f5b5a5
