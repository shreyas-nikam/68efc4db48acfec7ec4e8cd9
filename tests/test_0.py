import pytest
from definition_2281f67ecdc7468f83ded607e63e2669 import calculate_technical_ai_skills

@pytest.mark.parametrize("prompting, tools, understanding, data_lit, expected", [
    (0.8, 0.7, 0.9, 0.6, 0.75),  # Typical case
    (1.0, 1.0, 1.0, 1.0, 1.0),  # All skills at max
    (0.0, 0.0, 0.0, 0.0, 0.0),  # All skills at min
    (0.5, 0.5, 0.5, 0.5, 0.5),  # All skills equal
    (0.2, 0.9, 0.3, 0.8, 0.55),  # Varying skills
])
def test_calculate_technical_ai_skills(prompting, tools, understanding, data_lit, expected):
    assert calculate_technical_ai_skills(prompting, tools, understanding, data_lit) == expected