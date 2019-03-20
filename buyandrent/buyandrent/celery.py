import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTING_MODULE', 'buyandrent.settings')

#Instance of our app;ication
app = Celery('buyandrent')

app.config_from_object('django.conf:settings')

# Auto discover asynchronous tasks from installed Apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
