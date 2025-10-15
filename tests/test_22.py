import pytest
from definition_281ce9afeb1745489d601a0b4721dede import calculate_synergy_percentage

@pytest.mark.parametrize("vr_score, hr_score, alignment_factor, expected", [
    (75, 80, 0.9, 60.0),
    (50, 50, 0.5, 25.0),
    (90, 20, 0.1, 1.8),
    (0, 100, 1.0, 0.0),
    (100, 0, 1.0, 0.0)
])
def test_calculate_synergy_percentage(vr_score, hr_score, alignment_factor, expected):
    assert calculate_synergy_percentage(vr_score, hr_score, alignment_factor) == expected