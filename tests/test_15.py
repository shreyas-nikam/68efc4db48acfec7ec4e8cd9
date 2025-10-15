import pytest
from definition_1799f960e2f84b529a9f737f519074c5 import calculate_base_opportunity_score

@pytest.mark.parametrize("ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1, w2, w3, w4, expected", [
    (0.8, 0.7, 0.9, 0.6, 0.3, 0.3, 0.25, 0.15, 0.75),
    (0.2, 0.3, 0.1, 0.4, 0.3, 0.3, 0.25, 0.15, 0.23),
    (1.0, 1.0, 1.0, 1.0, 0.3, 0.3, 0.25, 0.15, 1.0),
    (0.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.25, 0.15, 0.0),
    (0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0)  # All weights are zero
])
def test_calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1, w2, w3, w4, expected):
    try:
        result = calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1, w2, w3, w4)
        assert isinstance(result, (int, float))
        assert result == expected
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")