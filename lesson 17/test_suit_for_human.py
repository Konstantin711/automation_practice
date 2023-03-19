import pytest


def test_check_var_types_valid_case(valid_person_instance):
    human = valid_person_instance

    assert isinstance(human._Human__name, str), 'Name has wrong type'
    assert isinstance(human.age, int), 'Age has wrong type'
    assert isinstance(human.gender, str), 'Gender has wrong type'
    assert isinstance(human._Human__status, str), 'Status has wrong type'
    assert isinstance(human._Human__age_limit, int), 'Age limit has wrong type'


def test_name_can_be_changed(valid_person_instance):
    human = valid_person_instance
    name = human._Human__name
    human.name = 'New Name'

    assert human._Human__name == name, 'Name can`t be set'


def test_age_cant_be_set(valid_person_instance):
    human = valid_person_instance
    with pytest.raises(AttributeError):
        human.age = 35


def test_gender_cant_be_set(valid_person_instance):
    human = valid_person_instance
    with pytest.raises(AttributeError):
        human.gender = 'gender'


def test_status_cant_be_set(valid_person_instance):
    human = valid_person_instance
    human.status = 'forever alive'

    assert human._Human__status == 'alive', 'Status was changed'


def test_age_limit_cant_be_set(valid_person_instance):
    human = valid_person_instance
    human.age_limit = 120

    assert human._Human__age_limit == 100, 'Age limit was changed'


def test_age_can_be_increased_by_grow(valid_person_instance):
    human = valid_person_instance
    expected = human.age

    human.grow()

    assert human.age == expected + 1, 'Age was changed'


def test_status_can_be_changed_by_grow(very_old_person):
    human = very_old_person
    human.grow()

    assert human._Human__status == 'dead', 'Status wasn`t changed'


def test_true_returned_by_is_alive(valid_person_instance):
    human = valid_person_instance
    expected = human._Human__is_alive()

    assert expected, 'True wasn`t set'


def test_exception_returned_by_is_alive(very_old_person):
    human = very_old_person
    human.grow()

    with pytest.raises(Exception) as error:
        human._Human__is_alive()

    assert str(error.value) == f'{human._Human__name} is already dead...', \
        'Error message is incorrect'


def test_gender_can_be_changed_by_change_gender(valid_person_instance):
    human = valid_person_instance
    new_gender = 'female' if human.gender == 'male' else 'male'
    human.change_gender(new_gender)

    assert human.gender == new_gender, 'Gender wasn`t changed'


def test_proper_error_raised_by_change_gender(valid_person_instance):
    human = valid_person_instance
    new_gender = 'female' if human.gender == 'female' else 'male'

    with pytest.raises(Exception) as error:
        human.change_gender(new_gender)

    assert str(error.value) == f"{human._Human__name} already has gender '{new_gender}'", \
        'Error message is incorrect'


@pytest.mark.parametrize('gender', ['female', 'male'])
def test_check_gender_validated(valid_person_instance, gender):
    human = valid_person_instance
    human._Human__validate_gender(gender)


def test_error_raised_by_validate_gender(valid_person_instance):
    human = valid_person_instance
    gender = 'new_gender'

    with pytest.raises(Exception) as error:
        human._Human__validate_gender(gender)

    assert str(error.value) == f"Not correct name of gender", 'Error message is incorrect'
