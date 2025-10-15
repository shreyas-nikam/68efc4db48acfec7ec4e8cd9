import pytest
from definition_e3a5f3537280451f8d2ede1349d2a818 import calculate_regional_multiplier

@pytest.mark.parametrize("local_demand, national_avg_demand, remote_work_factor, gamma, expected", [
    (100, 50, 0.5, 0.2, 1 + 0.2 * (100/50 + 0.5 - 1)),  # Basic test case
    (50, 100, 0.5, 0.2, 1 + 0.2 * (50/100 + 0.5 - 1)),  # local_demand < national_avg_demand
    (100, 50, 1.0, 0.2, 1 + 0.2 * (100/50 + 1.0 - 1)),  # remote_work_factor = 1.0
    (100, 50, 0.0, 0.2, 1 + 0.2 * (100/50 + 0.0 - 1)),  # remote_work_factor = 0.0
    (0, 50, 0.5, 0.2, 1 + 0.2 * (0/50 + 0.5 - 1)),  # local_demand = 0
])
def test_calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma, expected):
    assert calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma) == expected