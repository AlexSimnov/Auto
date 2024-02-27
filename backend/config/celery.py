import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-24-hours': {
        'task': 'prod.tasks.check_run_out_of_time',
        'schedule': crontab(hour=0, minute=0),
    },
}
