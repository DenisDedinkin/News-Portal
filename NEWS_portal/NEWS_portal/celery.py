import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEWS_portal.settings')

app = Celery('NEWS_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'inform_news': {
        'task': 'tasks.inform_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}