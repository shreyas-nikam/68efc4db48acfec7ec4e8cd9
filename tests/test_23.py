import pytest
from definition_545b397201d54c89899ee57b044b0749 import calculate_ai_readiness_score

@pytest.mark.parametrize("vr_score, hr_score, synergy_percentage, alpha, beta, expected", [
    (70, 80, 60, 0.5, 0.2, 73.0),  # Basic test case
    (0, 0, 0, 0.5, 0.2, 0.0),      # All scores zero
    (100, 100, 100, 0.5, 0.2, 100.0), # All scores maximum
    (50, 50, 50, 0, 0, 50.0),      # alpha and beta are zero
    (50, 50, 50, 1, 1, 100.0),       # alpha and beta are one
])
def test_calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta, expected):
    assert calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta) == expected
