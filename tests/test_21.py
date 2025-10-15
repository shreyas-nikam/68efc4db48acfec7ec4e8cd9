import pytest
from definition_16434fedb2be42c886397f90d7f12c30 import calculate_alignment_factor

@pytest.mark.parametrize("skills_match_score, max_possible_match, timing_factor, expected", [
    (75, 100, 0.8, 0.6),
    (50, 100, 0.5, 0.25),
    (100, 100, 1.0, 1.0),
    (0, 100, 0.7, 0.0),
    (75, 50, 0.8, 1.2)
])
def test_calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor, expected):
    assert calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor) == expected