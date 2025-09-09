import pytest

from main import nth_lucky_number


def test_first():
    assert nth_lucky_number(1) == 4444444444


def test_second():
    assert nth_lucky_number(2) == 4444444447


def test_third():
    assert nth_lucky_number(3) == 4444444474


def test_last():
    assert nth_lucky_number(1024) == 7777777777
