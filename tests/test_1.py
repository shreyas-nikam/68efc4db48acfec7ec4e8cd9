import pytest
from definition_7b9cad6f9776475084c909b86bb3014a import calculate_ai_augmented_productivity

@pytest.mark.parametrize("output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai, expected", [
    (100, 50, 60, 30, 2.0),  # Standard case: AI improves quality and time
    (50, 50, 60, 60, 1.0),  # AI maintains quality, no time change
    (25, 50, 60, 30, 0.25),  # AI decreases quality but improves time
    (100, 50, 30, 60, 4.0),  # AI improves quality and time, time_with_ai > time_without_ai
    (0, 50, 60, 30, 0.0), # output_quality_with_ai is zero
])
def test_calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai, expected):
    assert calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai) == expected