import pytest
from definition_7548872ac847402791d3eee6bd8b7d30 import calculate_wage_premium

@pytest.mark.parametrize("ai_skilled_wage, median_wage, expected", [
    (50000, 40000, 0.25),
    (100000, 50000, 1.0),
    (60000, 60000, 0.0),
    (30000, 50000, -0.4),
    (120000, 40000, 2.0)
])
def test_calculate_wage_premium(ai_skilled_wage, median_wage, expected):
    assert calculate_wage_premium(ai_skilled_wage, median_wage) == expected
