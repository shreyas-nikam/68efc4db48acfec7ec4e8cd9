def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    """Calculates technical AI skills."""
    return (prompting + tools + understanding + data_lit) / 4

def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    """Calculates AI-augmented productivity."""
    return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)

def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    """Calculates $S_{i,3}$ using Equation (19)."""
    if total_ai_errors == 0 and total_decisions == 0:
        return 0.0
    if total_ai_errors == 0:
        return 0.0
    return 1 - (errors_caught / total_ai_errors + appropriate_trust_decisions / total_decisions) / 2

def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    """Calculates AI learning velocity."""
    if delta_t_hours_invested == 0:
        if delta_proficiency == 0:
            return 0.0
        else:
            raise ZeroDivisionError("Cannot divide by zero.")
    return delta_proficiency / delta_t_hours_invested

def calculate_ai_fluency(s1, s2, s3, s4):
    """Calculates AI-Fluency using Equation (16)."""
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4

def calculate_education_foundation(education_level):
    """Calculates education foundation score based on education level."""
    if education_level == "PhD":
        return 1.0
    elif education_level == "Master's":
        return 0.8
    elif education_level == "Bachelor's":
        return 0.6
    elif education_level == "Associate's/Certificate":
        return 0.4
    elif education_level == "HS + significant coursework":
        return 0.2
    elif education_level == "Some College":
        return 0.3
    else:
        return 0.0

def calculate_practical_experience(years_experience, gamma):
    """Calculates practical experience score."""
    return years_experience / (years_experience + (1 / gamma))

def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    """Calculates specialization depth."""
    return (portfolio_score + recognition_score + credentials_score) / 3

def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    """Calculates domain expertise."""
    return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth

def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    """Calculates adaptive capacity."""
    return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3

def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1, w2, w3):
    """Calculates $V^R$ using Equation (15)."""
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)

def calculate_ai_enhancement_potential(ai_enhancement_score):
    """
    Returns the input ai_enhancement_score.
    """
    return ai_enhancement_score

def calculate_job_growth_projection(growth_rate_g):
    """Normalizes job growth rate using Equation (8)."""
    score = 50 + (growth_rate_g * 100)
    score = max(0, min(score, 100))
    return int(score)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    """Calculates wage premium."""
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    """Calculates entry accessibility score."""
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))

def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1, w2, w3, w4):
    """Calculates base opportunity score."""
    return (w1 * ai_enhancement +
            w2 * job_growth_normalized +
            w3 * wage_premium +
            w4 * entry_accessibility)

def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val):
    """Calculates growth multiplier."""
    if previous_job_postings == 0:
        return 1.0
    return (current_job_postings / previous_job_postings)**lambda_val

def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma):
    """Calculates the regional multiplier."""
    return 1 + gamma * (local_demand/national_avg_demand + remote_work_factor - 1)

def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    """Calculates systematic opportunity."""
    return h_base * growth_multiplier * regional_multiplier

import pandas as pd

def calculate_skills_match_score(user_skills_df, required_skills_df):
    """Calculates Skills Match Score."""
    if user_skills_df.empty or required_skills_df.empty:
        return None

    merged_df = pd.merge(user_skills_df, required_skills_df, on='skill_name', how='inner')

    if merged_df.empty:
        return 0

    weighted_sum = 0
    total_importance = required_skills_df['skill_importance'].sum()

    for _, row in merged_df.iterrows():
        weighted_sum += (min(row['individual_skill_score'], row['required_skill_score']) / 100) * row['skill_importance']

    if total_importance == 0:
        return 0

    return (weighted_sum / total_importance) * 100

def calculate_timing_factor(years_experience):
    """Calculates Timing Factor using Equation (29)."""
    if years_experience <= 0:
        return 1
    else:
        return 1 + (years_experience / 5)

def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    """Calculates the alignment factor."""
    return (skills_match_score / max_possible_match) * timing_factor

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    """Calculates Synergy% using the formula."""
    return (vr_score * hr_score * alignment_factor) / 100.0

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    """Calculates AI readiness score."""
    return alpha * vr_score + alpha * hr_score + beta * synergy_percentage

def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, pathway_type, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score, mastery_score):
    """Simulates the update of VR components based on a selected pathway."""

    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)

    return ai_fluency, domain_expertise, adaptive_capacity