import pytest
from definition_9a2c469083db4ef48da594a2a1c66716 import calculate_idiosyncratic_readiness

@pytest.mark.parametrize(
    "ai_fluency, domain_expertise, adaptive_capacity, w1, w2, w3, expected",
    [
        (0.8, 0.7, 0.9, 0.45, 0.35, 0.20, 0.785),
        (0.0, 0.0, 0.0, 0.45, 0.35, 0.20, 0.0),
        (1.0, 1.0, 1.0, 0.45, 0.35, 0.20, 1.0),
        (0.5, 0.5, 0.5, 0.45, 0.35, 0.20, 0.5),
        (0.8, 0.7, 0.9, 0.0, 0.0, 0.0, 0.0),
    ],
)
def test_calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1, w2, w3, expected):
    assert calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1, w2, w3) == expected

