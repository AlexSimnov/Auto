from django.db import models


class Executor(models.Model):
    name = models.CharField(
        'имя',
        max_length=50
    )
    task_delete = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )

    def __str__(self) -> str:
        return f'{self.name}'
