import sys
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.core.wsgi import get_wsgi_application
#from decouple import config, Csv

BASE_DIR = str('/')

settings.configure(
	DEBUG=True,
	SECRET_KEY='SECRET_KEY',
	ALLOWED_HOSTS=[],
	ROOT_URLCONF='website.urls',
	MIDDLEWARE=[
	    'django.contrib.sessions.middleware.SessionMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	],
	#DATABASES={
	#	'default': {
	#		'ENGINE': 'django.db.backends.sqlite3',
	#		'NAME': ('db.sqlite3'),
	#	}
	#},
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],	
    INSTALLED_APPS = [
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',	
        'website',
    ],
    STATIC_URL = 'static/'
)

#def index(request):
#	return HttpResponse("<h1>Hello, this is a minimal project setup. Configure as you please!</h1>")

#urlpatterns = [
#	path('', index, name='index')
#]

application = get_wsgi_application()

if __name__ == "__main__":
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)