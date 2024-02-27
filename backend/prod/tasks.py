from config.celery import app
from .models import Task

from datetime import datetime


@app.task
def check_run_out_of_time():
    taks = Task.objects.filter(
        deadline_dt__lte=datetime.now())

    for i in taks:
        i.delete()
