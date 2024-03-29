# Generated by Django 4.2.8 on 2024-02-27 14:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('executor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('deadline_dt', models.DateTimeField(verbose_name='Дедлайн')),
                ('priority', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Приоритет')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('comment', models.TextField(max_length=256, verbose_name='Комментарий')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='executor.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('task', models.ManyToManyField(related_name='projects', to='prod.task')),
            ],
            options={
                'verbose_name': 'вещь',
                'verbose_name_plural': 'вещи',
            },
        ),
    ]
