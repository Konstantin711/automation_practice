import pytest
from human import Human


@pytest.fixture
def valid_person_instance():
    return Human('Homer', 32, 'male')


@pytest.fixture
def very_old_person():
    return Human('Homer', 100, 'male')
