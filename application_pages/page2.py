
import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming the dataframes are already defined (as in page1.py)
# individual_profiles_df, occupational_data_df, learning_pathways_df

# --- Pathway Simulation Function ---
def simulate_pathway_impact(
    current_ai_fluency,
    current_domain_expertise,
    current_adaptive_capacity,
    pathway_type,
    impact_ai_fluency,
    impact_domain_expertise,
    impact_adaptive_capacity,
    completion_score=1.0,
    mastery_score=1.0,
):
    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)

    return ai_fluency, domain_expertise, adaptive_capacity


def run_page2():
    st.header("Pathway Simulation")

    # --- Load Data (assuming already defined) ---
    # For demonstration, let's assume dataframes are available
    # In a real app, ensure they are loaded or passed correctly
    individual_profiles_data = {
        'user_id': [1],
        'prompting_score': [0.75],
        'tools_score': [0.6],
        'understanding_score': [0.8],
        'datalit_score': [0.9],
        'output_quality_with_ai': [90],
        'output_quality_without_ai': [60],
        'time_without_ai': [4],
        'time_with_ai': [1],
        'errors_caught': [15],
        'total_ai_errors': [20],
        'appropriate_trust_decisions': [25],
        'total_decisions': [30],
        'delta_proficiency': [0.3],
        'delta_t_hours_invested': [10],
        'education_level': ["Master's"],
        'years_experience': [5],
        'portfolio_score': [0.85],
        'recognition_score': [0.7],
        'credentials_score': [0.9],
        'cognitive_flexibility': [85],
        'social_emotional_intelligence': [90],
        'strategic_career_management': [75],
    }
    individual_profiles_df = pd.DataFrame(individual_profiles_data)

    occupational_data = {
        'occupation_name': [
            'Data Analyst with AI Skills',
            'AI UX Researcher',
            'AI Prompt Engineer',
            'Data Scientist',
            'Nursing Informatics',
            'Medical Coding',
        ],
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
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    }
    occupational_data_df = pd.DataFrame(occupational_data)

    learning_pathways_data = {
        'pathway_id': [1, 2, 3],
        'pathway_name': [
            'Prompt Engineering Fundamentals',
            'AI for Financial Analysis',
            'Human-AI Collaboration',
        ],
        'pathway_type': [
            'AI-Fluency',
            'Domain+AI Integration',
            'Adaptive Capacity',
        ],
        'impact_ai_fluency': [0.2, 0.1, 0.05],
        'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2],
    }
    learning_pathways_df = pd.DataFrame(learning_pathways_data)

    # --- Input Widgets ---
    st.subheader("Pathway Simulation Inputs")

    # Select Learning Pathway
    selected_pathway = st.selectbox(
        "Select Learning Pathway", learning_pathways_df['pathway_name'], index=0
    )
    pathway = learning_pathways_df[learning_pathways_df['pathway_name'] == selected_pathway].iloc[0]

    # Pathway Completion & Mastery
    completion_score = st.slider(
        "Pathway Completion Score", 0.0, 1.0, 1.0
    )
    mastery_score = st.slider("Pathway Mastery Score", 0.0, 1.0, 1.0)

    # --- Load current VR values from the individual profile ---
    # In a multi-page app, st.session_state might be needed to store
    # and retrieve these values across pages.
    # For this example, let's assume we have initial values.

    # This data should ideally come from a previous page or session state
    initial_ai_fluency = 0.7  # Example value
    initial_domain_expertise = 0.6  # Example value
    initial_adaptive_capacity = 0.8  # Example value

    # Simulate Button
    if st.button("Simulate Pathway Impact"):
        # --- Perform Simulation ---
        (new_ai_fluency, new_domain_expertise, new_adaptive_capacity) = simulate_pathway_impact(
            initial_ai_fluency,
            initial_domain_expertise,
            initial_adaptive_capacity,
            pathway['pathway_type'],
            pathway['impact_ai_fluency'],
            pathway['impact_domain_expertise'],
            pathway['impact_adaptive_capacity'],
            completion_score,
            mastery_score,
        )

        # --- Display Results ---
        st.subheader("Simulation Results")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="AI-Fluency (New)", value=round(new_ai_fluency * 100, 2)
            )
        with col2:
            st.metric(
                label="Domain-Expertise (New)",
                value=round(new_domain_expertise * 100, 2),
            )
        with col3:
            st.metric(
                label="Adaptive-Capacity (New)",
                value=round(new_adaptive_capacity * 100, 2),
            )

        # --- Create a comparison chart ---
        labels = ["AI-Fluency", "Domain-Expertise", "Adaptive-Capacity"]
        initial_values = [
            initial_ai_fluency,
            initial_domain_expertise,
            initial_adaptive_capacity,
        ]
        new_values = [new_ai_fluency, new_domain_expertise, new_adaptive_capacity]

        df = pd.DataFrame(
            {
                "Component": labels,
                "Initial": initial_values,
                "New": new_values,
            }
        )

        fig = px.bar(
            df,
            x="Component",
            y=["Initial", "New"],
            barmode="group",
            title="Comparison of VR Components",
        )
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    run_page2()
