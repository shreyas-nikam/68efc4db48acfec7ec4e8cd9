import pytest
from definition_ac5879c967464d27899b789d90b697fd import calculate_systematic_opportunity

@pytest.mark.parametrize("h_base, growth_multiplier, regional_multiplier, expected", [
    (0.8, 1.2, 0.9, 0.864),  # Typical case
    (0.5, 1.0, 1.0, 0.5),    # No growth or regional multiplier effect
    (1.0, 1.5, 0.5, 0.75),   # High growth, low regional
    (0.2, 0.8, 1.2, 0.192),  # Low base, low growth, high regional
    (0, 1.0, 1.0, 0),        # Zero base opportunity
])
def test_calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier, expected):
    assert calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier) == expected