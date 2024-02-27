import pytest
import factory

from executor.models import Executor

from prod.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    create_dt = factory.Faker('date_time')
    deadline_dt = factory.Faker('date_time')
    priority = factory.Faker('random_int', min=1, max=3)
    title = factory.Faker('sentence', nb_words=4)
    comment = factory.Faker('text')


@pytest.fixture()
def create_ex(db):
    one_ex = Executor.objects.create(
        name='Alex'
    )
    return one_ex
