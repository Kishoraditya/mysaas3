SECRET_KEY = 'key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTAGRAM_APP_ID = 'id'
INSTAGRAM_APP_SECRET = 'secret'
#INSTAGRAM_REDIRECT_URI = 'http://127.0.0.1:8000/socialapp/instagram-callback/'
INSTAGRAM_REDIRECT_URI = 'redirect url'
FACEBOOK_APP_ID = 'id'
FACEBOOK_APP_SECRET = 'secret'

