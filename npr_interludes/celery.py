from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings  # noqa


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'npr_interludes.settings.development')

app = Celery('npr_interludes')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)