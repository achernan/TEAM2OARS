import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TEAM2OARS.settings")

application = get_wsgi_application()
