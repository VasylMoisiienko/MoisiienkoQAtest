import pytest
from modules.api.clients.github import GitHub


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def creat(self):
        self.name = 'Vasyl'
        self.second_name = 'Moisiienko'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.creat()

    yield user

    user.remove()


def test_change_name(user):
    assert user.name == 'Vasyl'


def test_change_second_name(user):
    assert user.second_name == 'Moisiienko'


@pytest.fixture
def github_api():
    api = GitHub()

    yield api
