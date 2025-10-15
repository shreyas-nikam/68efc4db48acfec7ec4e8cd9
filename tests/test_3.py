import pytest
from definition_29d2ba899f7143ac9225e4516bae0dce import calculate_ai_learning_velocity

@pytest.mark.parametrize("delta_proficiency, delta_t_hours_invested, expected", [
    (10, 5, 2.0),
    (0, 10, 0.0),
    (5, 0, float('inf')),
    (-10, 5, -2.0),
    (10, -5, -2.0),
])
def test_calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested, expected):
    if delta_t_hours_invested == 0:
        if delta_proficiency == 0:
             assert calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested) == 0.0
        else:
            with pytest.raises(ZeroDivisionError):
                calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested)
    else:
        assert calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested) == delta_proficiency / delta_t_hours_invested