import pytest
from definition_8fd9b1bbf80f4a5e8e76075950175359 import calculate_job_growth_projection

@pytest.mark.parametrize("growth_rate_g, expected", [
    (0.10, 100),  # Positive growth rate
    (-0.05, 0), # Negative growth rate
    (0.0, 50), # Zero growth rate
    (0.5, 100), #High growth rate, should be capped at 100.
    (-0.5, 0), #High negative growth rate, should be capped at 0.
])
def test_calculate_job_growth_projection(growth_rate_g, expected):
    assert calculate_job_growth_projection(growth_rate_g) == expected