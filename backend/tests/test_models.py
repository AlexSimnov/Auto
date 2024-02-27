import pytest

from .fixtures.fixtures import create_ex, TaskFactory


class TestExecutor:

    @pytest.mark.django_db
    def test_upd_count(self, create_ex):
        tasks = TaskFactory.create(executor=create_ex)

        assert create_ex.task_delete == 0

        tasks.delete()

        assert create_ex.task_delete == 1
