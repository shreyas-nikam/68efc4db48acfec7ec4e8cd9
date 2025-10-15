import pytest
from definition_df82a53c451c4e20971bc7dea257c41b import calculate_practical_experience

@pytest.mark.parametrize("years_experience, gamma, expected", [
    (5, 0.15, 5 / (5 + (1 / 0.15))),
    (0, 0.15, 0),
    (10, 0.15, 10 / (10 + (1 / 0.15))),
    (5, 0.05, 5 / (5 + (1 / 0.05))),
    (5, 0.30, 5 / (5 + (1 / 0.30))),
])
def test_calculate_practical_experience(years_experience, gamma, expected):
    assert calculate_practical_experience(years_experience, gamma) == expected