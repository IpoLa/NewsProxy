from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from news_proxy_app.management.commands.update_news import Command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProxy.settings')

app = Celery('NewsProxy')

# celeryconfig.py

# Set the broker connection retry behavior (prior to Celery 6.0)
broker_connection_retry = True

# Set the broker connection retry on startup (for Celery 6.0 and above)
broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Define schedule for the periodic task (run twice a day)
# app.conf.beat_schedule = {
#     'run-task-twice-daily': {
#         'task': 'news_proxy_app.management.commands.update_news.Command',
#         'schedule': crontab(minute=1),
#         #   'schedule': crontab(hour='*/12'),  # Run every 12 hours
#     },
# }


# from celery import Celery
# from celery.schedules import crontab
# import os
# from news_proxy_app.management.commands.update_news import Command

# app = Celery('NewsProxy')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProxy.settings')
# # Configure Celery
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# # Define the Celery Beat schedule
# app.conf.beat_schedule = {
#     'run-task-twice-daily': {
#         'task': Command,
#         'schedule': crontab(hour='*/12'),  # Run every 12 hours
#     },
# }