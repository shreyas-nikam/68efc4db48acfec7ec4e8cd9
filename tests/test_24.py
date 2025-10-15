import pytest
from definition_fb96548c80b04a6eabe0daa540c39d12 import simulate_pathway_impact

@pytest.mark.parametrize(
    "current_ai_fluency, current_domain_expertise, current_adaptive_capacity, pathway_type, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score, mastery_score, expected_ai_fluency, expected_domain_expertise, expected_adaptive_capacity",
    [
        (0.5, 0.5, 0.5, "AI-Fluency", 0.1, 0.0, 0.0, 1.0, 1.0, 0.6, 0.5, 0.5),
        (0.5, 0.5, 0.5, "Domain+AI Integration", 0.0, 0.1, 0.0, 1.0, 1.0, 0.5, 0.6, 0.5),
        (0.5, 0.5, 0.5, "Adaptive Capacity", 0.0, 0.0, 0.1, 1.0, 1.0, 0.5, 0.5, 0.6),
        (0.5, 0.5, 0.5, "AI-Fluency", 0.1, 0.0, 0.0, 0.5, 0.5, 0.55, 0.5, 0.5),  # Reduced impact due to scores
        (1.0, 1.0, 1.0, "AI-Fluency", 0.1, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0) # Check that values don't exceed 1.0
    ],
)
def test_simulate_pathway_impact(
    current_ai_fluency,
    current_domain_expertise,
    current_adaptive_capacity,
    pathway_type,
    impact_ai_fluency,
    impact_domain_expertise,
    impact_adaptive_capacity,
    completion_score,
    mastery_score,
    expected_ai_fluency,
    expected_domain_expertise,
    expected_adaptive_capacity
):
    """
    Test that the pathway impact simulation correctly updates the VR components.
    """
    ai_fluency, domain_expertise, adaptive_capacity = simulate_pathway_impact(
        current_ai_fluency,
        current_domain_expertise,
        current_adaptive_capacity,
        pathway_type,
        impact_ai_fluency,
        impact_domain_expertise,
        impact_adaptive_capacity,
        completion_score,
        mastery_score
    )
    assert ai_fluency == expected_ai_fluency
    assert domain_expertise == expected_domain_expertise
    assert adaptive_capacity == expected_adaptive_capacity