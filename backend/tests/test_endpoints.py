from rest_framework.test import APIClient
import pytest

from .fixtures.fixtures import TaskFactory

from http import HTTPStatus


class TestTask:

    url = '/api/v1/task/'

    @pytest.mark.django_db
    def test_task(self,):
        TaskFactory.create_batch(11)

        client = APIClient()
        res = client.get(self.url)

        assert res.status_code == HTTPStatus.OK
        assert res.json()

    @pytest.mark.django_db
    def test_endp(self):
        body = {
            "deadline_dt": "2024-10-12T10:30:00",
            "priority": 2,
            "title": "title",
            "comment": "comment"
        }

        client = APIClient()
        res = client.post(self.url, data=body, format='json')

        assert res.status_code == HTTPStatus.CREATED

        res = client.patch(self.url+'1/', body=body, format='json')

        assert res.status_code == HTTPStatus.OK

        res = client.delete(self.url+'1/')

        assert res.status_code == HTTPStatus.NO_CONTENT
