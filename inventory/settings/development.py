# -*- coding: utf-8 -*- 
from .base import * 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['localhost','127.0.0.1','137.190.116.87']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

=======
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
>>>>>>> 8d50c88a78994a4104df87f506c7dc8824f5b5a5
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
<<<<<<< HEAD
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
=======
}
>>>>>>> 8d50c88a78994a4104df87f506c7dc8824f5b5a5
