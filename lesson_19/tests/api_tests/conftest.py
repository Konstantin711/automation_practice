import pytest
from lesson_19.data_objects.person_data import PersonData


@pytest.fixture
def person_data():
    return PersonData()
