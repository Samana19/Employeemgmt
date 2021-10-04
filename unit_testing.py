import pytest


@pytest.fixture
def tester():
    employee_id = "210246"
    employee_name = "Hello Shrestha"
    employee_email = "hello@gmail.com"
    return (employee_id, employee_name, employee_email)


def test_1(tester):
    employee_id_check = "210246"
    assert tester[0] == employee_id_check


def test_2(tester):
    employee_name_check = "Hello Shrestha"
    assert tester[1] == employee_name_check


def test_3(tester):
    employee_email_check = "bye@gmail.com"
    assert tester[2] == employee_email_check
