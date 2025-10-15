import pytest
from definition_27fdf1593cc742b2b086c36b7c027f3e import calculate_critical_ai_judgment


def test_calculate_critical_ai_judgment_no_errors():
    assert calculate_critical_ai_judgment(0, 0, 10, 10) == 0


def test_calculate_critical_ai_judgment_all_errors():
    assert calculate_critical_ai_judgment(0, 10, 0, 10) == 1


def test_calculate_critical_ai_judgment_some_errors():
    assert calculate_critical_ai_judgment(5, 10, 5, 10) == 0.5


def test_calculate_critical_ai_judgment_mixed_scenarios():
    assert calculate_critical_ai_judgment(7, 10, 3, 10) == 0.3


def test_calculate_critical_ai_judgment_perfect_judgment():
    assert calculate_critical_ai_judgment(10, 10, 10, 10) == 0.0