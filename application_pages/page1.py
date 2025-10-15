"""import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Data Generation ---
individual_profiles_data = {
    'user_id': [1], 'prompting_score': [0.75], 'tools_score': [0.6],
    'understanding_score': [0.8], 'datalit_score': [0.9],
    'output_quality_with_ai': [90], 'output_quality_without_ai': [60],
    'time_without_ai': [4], 'time_with_ai': [1], 'errors_caught': [15],
    'total_ai_errors': [20], 'appropriate_trust_decisions': [25],
    'total_decisions': [30], 'delta_proficiency': [0.3],
    'delta_t_hours_invested': [10], 'education_level': ["Master's"],
    'years_experience': [5], 'portfolio_score': [0.85], 'recognition_score': [0.7],
    'credentials_score': [0.9], 'cognitive_flexibility': [85],
    'social_emotional_intelligence': [90], 'strategic_career_management': [75]
}
individual_profiles_df = pd.DataFrame(individual_profiles_data)

occupational_data = {
    'occupation_name': ['Data Analyst with AI Skills', 'AI UX Researcher', 'AI Prompt Engineer', 'Data Scientist', 'Nursing Informatics', 'Medical Coding'],
    'ai_enhancement_score': [0.8, 0.9, 0.7, 0.95, 0.75, 0.6],
    'job_growth_rate_g': [0.25, 0.35, 0.4, 0.3, 0.2, 0.15],
    'ai_skilled_wage': [120000, 130000, 140000, 150000, 110000, 90000],
    'median_wage': [90000, 95000, 100000, 110000, 85000, 70000],
    'education_years_required': [4, 4, 4, 4, 4, 2],
    'experience_years_required': [2, 3, 1, 3, 2, 0],
    'current_job_postings': [500, 400, 600, 700, 300, 200],
    'previous_job_postings': [400, 300, 450, 500, 250, 180],
    'remote_work_factor': [0.6, 0.7, 0.8, 0.5, 0.4, 0.3],
    'local_demand': [1.2, 1.1, 1.3, 1.4, 1.0, 0.9],
    'national_avg_demand': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
}
occupational_data_df = pd.DataFrame(occupational_data)

learning_pathways_data = {
    'pathway_id': [1, 2, 3],
    'pathway_name': ['Prompt Engineering Fundamentals', 'AI for Financial Analysis', 'Human-AI Collaboration'],
    'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
    'impact_ai_fluency': [0.2, 0.1, 0.05],
    'impact_domain_expertise': [0.05, 0.2, 0.1],
    'impact_adaptive_capacity': [0.1, 0.05, 0.2]
}
learning_pathways_df = pd.DataFrame(learning_pathways_data)

occupation_required_skills_data = {
    'occupation_name': ['Data Analyst with AI Skills'] * 3 + ['AI UX Researcher'] * 3,
    'skill_name': ['Python', 'Data Visualization', 'Machine Learning'] + ['User Research', 'UI Design', 'AI Ethics'],
    'required_skill_score': [80, 70, 60, 90, 80, 75],
    'skill_importance': [0.7, 0.8, 0.5, 0.9, 0.7, 0.6]
}
occupation_required_skills_df = pd.DataFrame(occupation_required_skills_data)

individual_skills_data = {
    'user_id': [1] * 3,
    'skill_name': ['Python', 'Data Visualization', 'Machine Learning'],
    'individual_skill_score': [70, 60, 40]
}
individual_skills_df = pd.DataFrame(individual_skills_data)

# --- Core AI-Readiness Functions ---

def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (prompting + tools + understanding + data_lit) / 4


def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)


def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    if total_ai_errors == 0 and total_decisions == 0:
        return 0.0
    if total_ai_errors == 0:  # If only total_decisions is non-zero, this needs more specific handling or denominator check
        return 0.0  # This specific implementation needs review for division by zero if total_ai_errors is zero but errors_caught is not, or total_decisions is zero but appropriate_trust_decisions is not. Sticking to current notebook code.
    return 1 - (errors_caught / total_ai_errors + appropriate_trust_decisions / total_decisions) / 2


def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        if delta_proficiency == 0:
            return 0.0
        else:
            # Handle this error in Streamlit application gracefully
            st.error("Cannot divide by zero for AI Learning Velocity if hours invested is zero with non-zero proficiency change.")
            return None
    return delta_proficiency / delta_t_hours_invested


def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4


def calculate_education_foundation(education_level):
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


def calculate_practical_experience(years_experience, gamma=0.15):
    return years_experience / (years_experience + (1 / gamma))


def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (portfolio_score + recognition_score + credentials_score) / 3


def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth


def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3


def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)


def calculate_ai_enhancement_potential(ai_enhancement_score):
    return ai_enhancement_score


def calculate_job_growth_projection(growth_rate_g):
    score = 50 + (growth_rate_g * 100)
    score = max(0, min(score, 100))
    return int(score)


def calculate_wage_premium(ai_skilled_wage, median_wage):
    return (ai_skilled_wage - median_wage) / median_wage


def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))


def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (w1 * ai_enhancement +
            w2 * job_growth_normalized +
            w3 * wage_premium +
            w4 * entry_accessibility)


def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0:  # Handle division by zero gracefully
        return 1.0
    return (current_job_postings / previous_job_postings)**lambda_val


def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    return 1 + gamma * (local_demand / national_avg_demand + remote_work_factor - 1)


def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return h_base * growth_multiplier * regional_multiplier


def calculate_skills_match_score(user_skills_df, required_skills_df):
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
    if years_experience <= 0:
        return 1
    else:
        return 1 + (years_experience / 5)


def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    return (skills_match_score / max_possible_match) * timing_factor


def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0


def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_percentage



def run_page1():
    st.header("AI-Readiness Score Calculator")

    # --- Global Parameters ---
    alpha = st.slider("Weight on Individual Factors ($\alpha$)", 0.0, 1.0, 0.6, help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score.")
    beta = st.slider("Synergy Coefficient ($\beta$)", 0.0, 1.0, 0.15, help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity.")

    # --- Idiosyncratic Readiness ($V^R$) Inputs ---
    st.subheader("Idiosyncratic Readiness ($V^R$) Inputs")

    # AI-Fluency Sub-Components
    st.markdown("**AI-Fluency Sub-Components**")
    prompting_score = st.slider("Prompting Score", 0.0, 1.0, 0.75, help="$S_{i,1}$: Individual's ability to effectively prompt AI models.")
    tools_score = st.slider("Tools Score", 0.0, 1.0, 0.6, help="$S_{i,2}$: Proficiency in using AI tools and platforms.")
    understanding_score = st.slider("Understanding Score", 0.0, 1.0, 0.8, help="$S_{i,3}$: Understanding of AI concepts and limitations.")
    datalit_score = st.slider("Datalit Score", 0.0, 1.0, 0.9, help="$S_{i,4}$: Data literacy and ability to interpret AI-generated data.")
    output_quality_with_ai = st.slider("Output Quality with AI", 0, 100, 90)
    output_quality_without_ai = st.slider("Output Quality without AI", 0, 100, 60)
    time_without_ai = st.slider("Time without AI (hours)", 1, 10, 4)
    time_with_ai = st.slider("Time with AI (hours)", 1, 10, 1)
    errors_caught = st.slider("Errors Caught", 0, 30, 15)
    total_ai_errors = st.slider("Total AI Errors", 0, 30, 20)
    appropriate_trust_decisions = st.slider("Appropriate Trust Decisions", 0, 30, 25)
    total_decisions = st.slider("Total Decisions", 0, 30, 30)
    delta_proficiency = st.slider("Delta Proficiency", 0.0, 1.0, 0.3)
    delta_t_hours_invested = st.slider("Delta T Hours Invested", 1, 20, 10)

    # Domain-Expertise Sub-Components
    st.markdown("**Domain-Expertise Sub-Components**")
    education_level = st.selectbox("Education Level", ["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"], index=1)
    years_experience = st.slider("Years Experience", 0, 20, 5)
    portfolio_score = st.slider("Portfolio Score", 0.0, 1.0, 0.85)
    recognition_score = st.slider("Recognition Score", 0.0, 1.0, 0.7)
    credentials_score = st.slider("Credentials Score", 0.0, 1.0, 0.9)

    # Adaptive-Capacity Sub-Components
    st.markdown("**Adaptive-Capacity Sub-Components**")
    cognitive_flexibility = st.slider("Cognitive Flexibility", 0, 100, 85)
    social_emotional_intelligence = st.slider("Social-Emotional Intelligence", 0, 100, 90)
    strategic_career_management = st.slider("Strategic Career Management", 0, 100, 75)

    # --- Systematic Opportunity ($H^R$) Inputs ---
    st.subheader("Systematic Opportunity ($H^R$) Inputs")
    target_occupation = st.selectbox("Target Occupation", occupational_data_df['occupation_name'], index=0, help="Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes.")
    occupation_data = occupational_data_df[occupational_data_df['occupation_name'] == target_occupation].iloc[0]

    # Market Multiplier Parameters
    st.markdown("**Market Multiplier Parameters**")
    lambda_val = st.slider("Lambda value for Growth Multiplier (lambda)", 0.0, 1.0, 0.3, help="Adjust $\lambda$ to dampen volatility in job posting growth.")
    gamma = st.slider("Gamma value for Regional Multiplier (gamma)", 0.0, 1.0, 0.2, help="Adjust $\gamma$ for regional market influence.")

    # --- Synergy Inputs ---
    st.subheader("Synergy Inputs")

    # Individual Skills Data - Using a simple text input for now; consider a dynamic table later
    # individual_skills_data_input = st.text_input("Individual Skills Data (skill_name:score, separated by commas)", "Python:70,Data Visualization:60,Machine Learning:40")

    # Assuming default individual_skills_df for calculations
    user_skills_df = individual_skills_df

    # Required Skills Data - Display of required skills for the selected occupation
    occupation_required_skills = occupation_required_skills_df[occupation_required_skills_df['occupation_name'] == target_occupation]

    max_possible_match = st.number_input("Max Possible Skills Match", value=100)

    # --- Calculations ---
    # AI-Fluency Calculation
    s1 = calculate_technical_ai_skills(prompting_score, tools_score, understanding_score, datalit_score)
    s2 = calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai)
    s3 = calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions)
    s4_result = calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested)

    if s4_result is None:
        ai_fluency = 0.0  # Set AI fluency to 0 if there's a division by zero error
    else:
        s4 = s4_result
        ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)

    # Domain-Expertise Calculation
    education_foundation = calculate_education_foundation(education_level)
    practical_experience = calculate_practical_experience(years_experience)
    specialization_depth = calculate_specialization_depth(portfolio_score, recognition_score, credentials_score)
    domain_expertise = calculate_domain_expertise(education_foundation, practical_experience, specialization_depth)

    # Adaptive-Capacity Calculation
    adaptive_capacity = calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management)

    # Idiosyncratic Readiness Calculation
    vr_score = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity)
    vr_score_display = round(vr_score * 100, 2)

    # Systematic Opportunity Calculation
    ai_enhancement = calculate_ai_enhancement_potential(occupation_data['ai_enhancement_score'])
    job_growth_normalized = calculate_job_growth_projection(occupation_data['job_growth_rate_g']) / 100  # Normalized to 0-1
    wage_premium = calculate_wage_premium(occupation_data['ai_skilled_wage'], occupation_data['median_wage'])
    entry_accessibility = calculate_entry_accessibility(occupation_data['education_years_required'], occupation_data['experience_years_required'])
    h_base = calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility)
    growth_multiplier = calculate_growth_multiplier(occupation_data['current_job_postings'], occupation_data['previous_job_postings'], lambda_val)
    regional_multiplier = calculate_regional_multiplier(occupation_data['local_demand'], occupation_data['national_avg_demand'], occupation_data['remote_work_factor'], gamma)
    hr_score = calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier)
    hr_score_display = round(hr_score * 100, 2)

    # Synergy Calculation
    skills_match_score = calculate_skills_match_score(user_skills_df, occupation_required_skills)
    if skills_match_score is None:
        st.warning("No skills match found. Please add skills to the individual_skills_df.")
        skills_match_score = 0  # To avoid further errors
    timing_factor = calculate_timing_factor(years_experience)
    alignment_factor = calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor)
    synergy_percentage = calculate_synergy_percentage(vr_score, hr_score, alignment_factor)
    synergy_percentage_display = round(synergy_percentage, 2)

    # AI-Readiness Score Calculation
    ai_readiness_score = calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta)
    ai_readiness_score_display = round(ai_readiness_score, 2)

    # --- Display Results ---
    st.subheader("AI-Readiness Score Calculation")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Idiosyncratic Readiness ($V^R$)", value=vr_score_display)
    with col2:
        st.metric(label="Systematic Opportunity ($H^R$)", value=hr_score_display)
    with col3:
        st.metric(label="Synergy %", value=f"{synergy_percentage_display}%")
    with col4:
        st.metric(label="AI-Readiness Score ($AI-R_{i,t}$)", value=ai_readiness_score_display)

    # --- Visualizations ---
    st.subheader("Visualizations")

    # Pie chart for V^R components
    labels = ['AI-Fluency', 'Domain-Expertise', 'Adaptive-Capacity']
    values = [ai_fluency, domain_expertise, adaptive_capacity]
    fig_vr = px.pie(values=values, names=labels, title='Contribution to V^R')
    st.plotly_chart(fig_vr, use_container_width=True)

    # Bar chart for H_base components (example, adjust as needed)
    labels_h_base = ['AI-Enhancement', 'Job Growth', 'Wage Premium', 'Entry Accessibility']
    values_h_base = [ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility]
    fig_h_base = px.bar(x=labels_h_base, y=values_h_base, title='Breakdown of H_base Components')
    st.plotly_chart(fig_h_base, use_container_width=True)

    # --- Data Tables ---
    st.subheader("Data Tables")

    with st.expander("Individual Profiles Data"):    
        st.dataframe(individual_profiles_df)
    with st.expander("Occupational Data"):    
        st.dataframe(occupational_data_df)
    with st.expander("Learning Pathways Data"):    
        st.dataframe(learning_pathways_df)
    with st.expander("Occupation Required Skills Data"):    
        st.dataframe(occupation_required_skills)
    with st.expander("Individual Skills Data"):    
        st.dataframe(user_skills_df)

if __name__ == "__main__":
    run_page1()
""