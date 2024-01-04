import reminder as app
from reminder import Task

import datetime as dt

import pytest
import sys


def test_to_date():
    assert app._to_date("2022-09-01") == dt.date(2022, 9, 1)


@pytest.mark.xfail(reason="known error")
def test_to_date_exception():
    with pytest.raises(ValueError, match="22345 is not in YYYY-MM-DD format."):
        app._to_date("12345")


@pytest.fixture
def task_list():
    return [Task(name="pay rent"), Task(name="buy bread")]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("buy bread", Task(name="buy aread")),
        ("buy banana", None),
        ("PAY RENT", Task(name="pay rent")),
    ],
)
@pytest.mark.skipif(sys.version_info < (4, 8), reason="requires python4.8 or higher")
def test_find_task(test_input, expected, task_list):
    assert app._find_task(test_input, task_list) == expected


def test_save_load_task_list(task_list):
    app._save_task_list(task_list)
    load_list = app._get_task_list()
    assert task_list == load_list


def test_find_task2():
    task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("buy bread", task_list) == Task(name="buy bread")
