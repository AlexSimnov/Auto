from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from executor.models import Executor


class Task(models.Model):
    create_dt = models.DateTimeField(
        'дата создания',
        auto_now_add=True
    )
    deadline_dt = models.DateTimeField(
        'Дедлайн',
        null=False,
        blank=False
    )
    executor = models.ForeignKey(
        Executor,
        on_delete=models.SET_NULL,
        related_name='tasks',
        null=True,
        blank=True
    )
    priority = models.IntegerField(
        'Приоритет',
        validators=[MinValueValidator(1),
                    MaxValueValidator(3)]
        )
    title = models.CharField(
        'Заголовок',
        max_length=50
    )
    comment = models.TextField(
        'Комментарий',
        max_length=256
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Project(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    task = models.ManyToManyField(
        Task,
        related_name='projects'
    )

    class Meta:
        verbose_name = 'вещь'
        verbose_name_plural = 'вещи'

    def __str__(self) -> str:
        return f'{self.name}'
