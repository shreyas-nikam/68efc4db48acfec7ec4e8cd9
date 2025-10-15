import pytest
from definition_962cd3333abf49218c1fefe5f533ed1f import calculate_specialization_depth

@pytest.mark.parametrize("portfolio_score, recognition_score, credentials_score, expected", [
    (0.8, 0.9, 0.7, 0.8),  # Typical case
    (0.0, 0.0, 0.0, 0.0),  # All scores are zero
    (1.0, 1.0, 1.0, 1.0),  # All scores are maxed out
    (0.5, 0.5, 0.5, 0.5),  # All scores are average
    (0.2, 0.8, 0.9, 0.6333333333333333) # Uneven scores
])
def test_calculate_specialization_depth(portfolio_score, recognition_score, credentials_score, expected):
    assert calculate_specialization_depth(portfolio_score, recognition_score, credentials_score) == expected