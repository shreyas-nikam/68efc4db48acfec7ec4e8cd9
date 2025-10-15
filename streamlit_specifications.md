
# Streamlit Application Requirements Specification: AI Career Navigator & Pathway Planner

This document outlines the requirements for developing a Streamlit application based on the provided Jupyter Notebook content and user requirements. It details the interactive components, layout, and relevant code stubs from the notebook to serve as a blueprint for development.

## 1. Application Overview

The AI Career Navigator & Pathway Planner is an interactive Streamlit application that enables users to understand, calculate, and simulate their career readiness in AI-driven labor markets using the AI-Readiness Score (AI-R) framework.

### Learning Goals
-   Understand the key insights contained in the uploaded document and supporting data.
-   Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
-   Evaluate the potential impact of various learning pathways on individual skill development and career readiness.
-   Analyze different career paths based on market demand and personal capabilities through "what-if" scenarios.

## 2. User Interface Requirements

The application will feature a clear, intuitive layout, allowing users to interact with various parameters and immediately see the impact on their AI-Readiness Score.

### Layout and Navigation Structure
The application will be structured using Streamlit's `st.sidebar` for global controls and `st.tabs` or `st.expander` for main content sections.

-   **Main Title**: "AI Career Navigator & Pathway Planner"
-   **Introduction Section**: Displays the introductory markdown from the notebook.
-   **Core Concepts Section**: Explains the AI-Readiness Score formula and its components.
-   **Input Parameters Section**: Allows users to input/adjust personal and market data.
-   **AI-Readiness Score Calculation Section**: Displays the calculated $V^R$, $H^R$, Synergy%, and $AI-R$ scores.
-   **What-If Scenario Analysis Section**: Enables simulation of learning pathway impacts.
-   **Data Display Section**: Showcases the underlying synthetic dataframes.

### Input Widgets and Controls
Input controls will be organized logically, with clear labels and default values derived from the synthetic data.

#### Global Parameters
-   **Weight on Individual Factors ($\alpha$)**: Slider, range $[0.0, 1.0]$, default `0.6`.
    -   *Help Text*: "Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score."
-   **Synergy Coefficient ($\beta$)**: Slider, range $[0.0, 1.0]$, default `0.15`.
    -   *Help Text*: "Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity."

#### Idiosyncratic Readiness ($V^R$) Inputs
-   **AI-Fluency Sub-Components (Sliders, range $[0.0, 1.0]$)**:
    -   `Prompting Score`: Default `0.75`.
    -   `Tools Score`: Default `0.6`.
    -   `Understanding Score`: Default `0.8`.
    -   `Datalit Score`: Default `0.9`.
    -   `Output Quality with AI`: Default `90`.
    -   `Output Quality without AI`: Default `60`.
    -   `Time without AI (hours)`: Default `4`.
    -   `Time with AI (hours)`: Default `1`.
    -   `Errors Caught`: Default `15`.
    -   `Total AI Errors`: Default `20`.
    -   `Appropriate Trust Decisions`: Default `25`.
    -   `Total Decisions`: Default `30`.
    -   `Delta Proficiency`: Default `0.3`.
    -   `Delta T Hours Invested`: Default `10`.
    -   *Help Text for AI-Fluency sub-components*: Explanations for $S_{i,1}, S_{i,2}, S_{i,3}, S_{i,4}$ from the notebook.
-   **Domain-Expertise Sub-Components**:
    -   `Education Level`: Dropdown, options: "PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other". Default "Master's".
    -   `Years Experience`: Number input/Slider, default `5`.
    -   `Portfolio Score`: Slider, range $[0.0, 1.0]$, default `0.85`.
    -   `Recognition Score`: Slider, range $[0.0, 1.0]$, default `0.7`.
    -   `Credentials Score`: Slider, range $[0.0, 1.0]$, default `0.9`.
    -   *Help Text for Domain-Expertise sub-components*: Explanations for $E_{\text{education}}, E_{\text{experience}}, E_{\text{specialization}}$ from the notebook.
-   **Adaptive-Capacity Sub-Components (Sliders, range $[0, 100]$)**:
    -   `Cognitive Flexibility`: Default `85`.
    -   `Social-Emotional Intelligence`: Default `90`.
    -   `Strategic Career Management`: Default `75`.
    -   *Help Text for Adaptive-Capacity sub-components*: Explanations from the notebook.

#### Systematic Opportunity ($H^R$) Inputs
-   **Target Occupation**: Dropdown, options from `occupational_data_df['occupation_name']`. Default 'Data Analyst with AI Skills'.
    -   *Help Text*: "Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes."
-   **Market Multiplier Parameters (Sliders)**:
    -   `Lambda value for Growth Multiplier ($\lambda$)`: Range `[0.0, 1.0]`, default `0.3`.
    -   `Gamma value for Regional Multiplier ($\gamma$)`: Range `[0.0, 1.0]`, default `0.2`.
    -   *Help Text*: "Adjust $\lambda$ to dampen volatility in job posting growth. Adjust $\gamma$ for regional market influence."

#### Synergy Inputs
-   **Individual Skills Data**: Expandable section to allow users to add/modify their skill scores.
    -   Input fields for `skill_name` and `individual_skill_score`.
    -   This could be a dynamic table or multiple input rows.
-   **Required Skills Data**: Display of required skills for the selected occupation (from `occupation_required_skills_df`).
-   `Max Possible Skills Match`: Numeric input, default `100`.

#### Pathway Simulation Inputs
-   **Select Learning Pathway**: Dropdown, options from `learning_pathways_df['pathway_name']`. Default 'Prompt Engineering Fundamentals'.
-   **Pathway Completion Score**: Slider, range $[0.0, 1.0]$, default `1.0`.
-   **Pathway Mastery Score**: Slider, range $[0.0, 1.0]$, default `1.0`.
    -   *Help Text*: "Simulate the impact of completing a learning pathway with a certain completion and mastery level."

### Visualization Components
-   **Score Display**:
    -   Display current $V^R$, $H^R$, Synergy%, and $AI-R_{i,t}$ in prominent text or gauges.
    -   Display projected $V^R_{\text{new}}$, $H^R_{\text{new}}$, Synergy%_{\text{new}}$, and $AI-R_{\text{new}}$ after pathway simulation.
-   **Comparison Chart**:
    -   Bar chart comparing current vs. projected $AI-R$ and its components ($V^R$, $H^R$) after a pathway simulation.
    -   Pie chart or bar chart visualizing the contribution of AI-Fluency, Domain-Expertise, and Adaptive-Capacity to $V^R$.
    -   Bar chart for the breakdown of $H_{\text{base}}$ components.
-   **Data Tables**: Display raw `individual_profiles_df`, `occupational_data_df`, `learning_pathways_df`, `occupation_required_skills_df`, and `individual_skills_df` for reference, possibly within expanders.

### Interactive Elements and Feedback Mechanisms
-   **Calculate Button**: A button to trigger the calculation of the AI-Readiness Score based on current inputs.
-   **Simulate Button**: A button to trigger the pathway impact simulation.
-   **Dynamic Updates**: Scores and visualizations will update upon button clicks.
-   **Error Handling**: Informative messages for invalid inputs (e.g., division by zero, out-of-range values).
-   **Loading Indicators**: Potentially spinner/progress bar for calculations (though calculations are fast for synthetic data).

## 3. Additional Requirements

### Annotation and Tooltip Specifications
-   Every input widget (slider, dropdown, text input) will include inline help text or tooltips (`st.help()` or `st.tooltip()`) explaining its purpose and how it relates to the AI-Readiness framework, as outlined in the "Input Widgets and Controls" section above. This will draw upon the narrative cells and definitions provided in the Jupyter Notebook.

### State Preservation
-   All user-modified input values (sliders, dropdowns, text inputs) will be saved using `st.session_state` to ensure that changes are not lost upon rerun or re-navigation within the application. This ensures a persistent user experience during "what-if" scenario analysis.

## 4. Notebook Content and Code Requirements

This section extracts the relevant markdown content for display and Python code stubs for functionality. **Note on Formulas**: Where mathematical formulas from the original paper (OCR) diverge from the Python code implementation in the provided Jupyter Notebook, the formulas represented here in LaTeX reflect the *code's implementation* as this is the logic to be deployed in the Streamlit application.

### Markdown Content for Streamlit Display

#### Application Title and Introduction
```python
# st.title("AI Career Navigator & Pathway Planner")
# st.markdown("""
# This Jupyter Notebook implements the AI-Readiness Score (AI-R) framework, allowing users to understand, calculate, and simulate their career readiness in AI-driven labor markets. It provides an interactive environment to explore the impact of individual capabilities, market opportunities, and learning pathways on career prospects.
#
# ### Learning Goals
# - Understand the key insights contained in the uploaded document and supporting data.
# - Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
# - Evaluate the potential impact of various learning pathways on individual skill development and career readiness.
# - Analyze different career paths based on market demand and personal capabilities through "what-if" scenarios.
# """)
```

#### Introduction to the AI-Readiness Score
```python
# st.header("Introduction to the AI-Readiness Score")
# st.markdown("""
# This application explores the AI-Readiness Score (AI-R) framework, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. The AI-R score helps in navigating career transitions by considering both individual capabilities and market opportunities.
#
# The core formula for the AI-Readiness Score for an individual $i$ at time $t$ is defined as:
# """)
# st.latex(r""" AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) """)
# st.markdown("""
# Where:
# -   $V^R(t)$ is the Idiosyncratic Readiness (individual capability).
# -   $H^R(t)$ is the Systematic Opportunity (market demand).
# -   $\alpha \in [0,1]$ is the weight on individual vs. market factors.
# -   $\beta > 0$ is the Synergy coefficient.
# -   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.
# -   $\text{Synergy}\%$ is also normalized to $[0, 100]$ percentage units.
#
# This framework allows for dynamic "what-if" scenario planning, enabling users to understand how different learning pathways and career transitions impact their future career prospects.
# """)
```

#### Setup and Data Generation
```python
# st.header("Setup and Data Generation")
# st.markdown("""
# This section prepares the environment by importing necessary libraries and generating synthetic datasets that will be used throughout the application. The datasets are designed to be lightweight and representative of the data structures described in the AI-Readiness Score paper.
#
# ### Synthetic Data Generation
# This section generates synthetic data for individual profiles, occupational opportunities, learning pathways and skill requirements. This data is designed to mimic real-world scenarios and provide a basis for calculating and visualizing the AI-Readiness Score. The synthetic data will ensure that the calculations can be tested even without access to real user data.
# """)
```

#### Core AI-Readiness Functions
```python
# st.header("Core AI-Readiness Functions")
# st.markdown("""
# This section implements the various functions required to calculate the $V^R$, $H^R$, and Synergy components, leading to the final AI-Readiness Score. Each function directly corresponds to a mathematical definition or calculation method outlined in the provided technical paper, with adjustments made to reflect the actual Python implementation in the Jupyter Notebook. The correct implementation of these functions is essential for the accuracy of the AI-R score.
# """)
```

### Extracted Code Stubs

#### Library Imports (to be executed at application start)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ipywidgets imports are not needed for Streamlit
```

#### Synthetic Data Generation (to be executed at application start as initial data)
```python
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
```

#### Core AI-Readiness Functions (to be wrapped for Streamlit callbacks)

**AI-Fluency Sub-Components**:
-   **Technical AI Skills ($S_{i,1}$)**
    $$ S_{i,1} = \frac{\text{prompting\_score} + \text{tools\_score} + \text{understanding\_score} + \text{datalit\_score}}{4} $$
    ```python
    def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
        return (prompting + tools + understanding + data_lit) / 4
    ```
-   **AI-Augmented Productivity ($S_{i,2}$)**
    $$ S_{i,2} = \frac{\text{output\_quality\_with\_ai}}{\text{output\_quality\_without\_ai}} \cdot \frac{\text{time\_without\_ai}}{\text{time\_with\_ai}} $$
    ```python
    def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
        return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)
    ```
-   **Critical AI Judgment ($S_{i,3}$)**
    $$ S_{i,3} = 1 - \frac{\frac{\text{errors\_caught}}{\text{total\_ai\_errors}} + \frac{\text{appropriate\_trust\_decisions}}{\text{total\_decisions}}}{2} $$
    ```python
    def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
        if total_ai_errors == 0 and total_decisions == 0:
            return 0.0
        if total_ai_errors == 0: # If only total_decisions is non-zero, this needs more specific handling or denominator check
             return 0.0 # This specific implementation needs review for division by zero if total_ai_errors is zero but errors_caught is not, or total_decisions is zero but appropriate_trust_decisions is not. Sticking to current notebook code.
        return 1 - (errors_caught / total_ai_errors + appropriate_trust_decisions / total_decisions) / 2
    ```
-   **AI Learning Velocity ($S_{i,4}$)**
    $$ S_{i,4} = \frac{\text{delta\_proficiency}}{\text{delta\_t\_hours\_invested}} $$
    ```python
    def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
        if delta_t_hours_invested == 0:
            if delta_proficiency == 0:
                return 0.0
            else:
                # Handle this error in Streamlit application gracefully
                raise ZeroDivisionError("Cannot divide by zero for AI Learning Velocity if hours invested is zero with non-zero proficiency change.")
        return delta_proficiency / delta_t_hours_invested
    ```
-   **AI-Fluency**
    $$ \text{AI-Fluency} = 0.1 \cdot S_{i,1} + 0.2 \cdot S_{i,2} + 0.3 \cdot S_{i,3} + 0.4 \cdot S_{i,4} $$
    ```python
    def calculate_ai_fluency(s1, s2, s3, s4):
        return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4
    ```

**Domain-Expertise Sub-Components**:
-   **Education Foundation ($E_{\text{education}}$)**
    $$ E_{\text{education}} = \begin{cases} 1.0 & \text{if Education Level is "PhD"} \\ 0.8 & \text{if Education Level is "Master's"} \\ 0.6 & \text{if Education Level is "Bachelor's"} \\ 0.4 & \text{if Education Level is "Associate's/Certificate"} \\ 0.2 & \text{if Education Level is "HS + significant coursework"} \\ 0.3 & \text{if Education Level is "Some College"} \\ 0.0 & \text{otherwise} \end{cases} $$
    ```python
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
    ```
-   **Practical Experience ($E_{\text{experience}}$)**
    $$ E_{\text{experience}} = \frac{\text{years\_experience}}{\text{years\_experience} + \frac{1}{\gamma}} $$
    *Note: $\gamma$ (gamma) is typically $0.15$ as per the original paper's context, but the code uses a flexible $\gamma$ parameter.*
    ```python
    def calculate_practical_experience(years_experience, gamma=0.15):
        return years_experience / (years_experience + (1 / gamma))
    ```
-   **Specialization Depth ($E_{\text{specialization}}$)**
    $$ E_{\text{specialization}} = \frac{\text{portfolio\_score} + \text{recognition\_score} + \text{credentials\_score}}{3} $$
    ```python
    def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
        return (portfolio_score + recognition_score + credentials_score) / 3
    ```
-   **Domain-Expertise**
    $$ \text{Domain-Expertise} = 0.125 \cdot E_{\text{education}} + 0.25 \cdot E_{\text{experience}} + 0.625 \cdot E_{\text{specialization}} $$
    ```python
    def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
        return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth
    ```

**Adaptive-Capacity**
-   **Adaptive-Capacity**
    $$ \text{Adaptive-Capacity} = \frac{\text{cognitive\_flexibility} + \text{social\_emotional\_intelligence} + \text{strategic\_career\_management}}{3} $$
    ```python
    def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
        return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3
    ```

**Idiosyncratic Readiness ($V^R$)**
-   **Idiosyncratic Readiness ($V^R$)**
    $$ V^R = w_1 \cdot \text{AI-Fluency} + w_2 \cdot \text{Domain-Expertise} + w_3 \cdot \text{Adaptive-Capacity} $$
    *where $w_1=0.45, w_2=0.35, w_3=0.20$*
    ```python
    def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
        return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)
    ```

**Systematic Opportunity ($H^R$) Sub-Components**:
-   **AI-Enhancement Potential**
    *Represents the aggregated value from Equation (6) of the paper, provided as input.*
    ```python
    def calculate_ai_enhancement_potential(ai_enhancement_score):
        return ai_enhancement_score
    ```
-   **Job Growth Projection**
    $$ \text{Job Growth Projection} = \max\left(0, \min\left(100, 50 + (\text{growth\_rate\_g} \times 100)\right)\right) $$
    ```python
    def calculate_job_growth_projection(growth_rate_g):
        score = 50 + (growth_rate_g * 100)
        score = max(0, min(score, 100))
        return int(score)
    ```
-   **Wage Premium**
    $$ \text{Wage Premium} = \frac{\text{ai\_skilled\_wage} - \text{median\_wage}}{\text{median\_wage}} $$
    ```python
    def calculate_wage_premium(ai_skilled_wage, median_wage):
        return (ai_skilled_wage - median_wage) / median_wage
    ```
-   **Entry Accessibility**
    $$ \text{Entry Accessibility} = \frac{1}{1 + 0.1 \cdot (\text{education\_years\_required} + \text{experience\_years\_required})} $$
    ```python
    def calculate_entry_accessibility(education_years_required, experience_years_required):
        return 1 / (1 + 0.1 * (education_years_required + experience_years_required))
    ```
-   **Base Opportunity Score ($H_{\text{base}}$)**
    $$ H_{\text{base}}(o) = w_1 \cdot \text{AI-Enhancement} + w_2 \cdot \text{Job Growth}_{\text{normalized}} + w_3 \cdot \text{Wage Premium} + w_4 \cdot \text{Entry Accessibility} $$
    *where $w_1=0.30, w_2=0.30, w_3=0.25, w_4=0.15$*
    ```python
    def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
        return (w1 * ai_enhancement +
                w2 * job_growth_normalized +
                w3 * wage_premium +
                w4 * entry_accessibility)
    ```
-   **Growth Multiplier ($M_{\text{growth}}$)**
    $$ M_{\text{growth}}(t) = \left( \frac{\text{current\_job\_postings}}{\text{previous\_job\_postings}} \right)^{\lambda_{\text{val}}} $$
    ```python
    def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
        if previous_job_postings == 0: # Handle division by zero gracefully
            return 1.0
        return (current_job_postings / previous_job_postings)**lambda_val
    ```
-   **Regional Multiplier ($M_{\text{regional}}$)**
    $$ M_{\text{regional}}(t) = 1 + \gamma \cdot \left( \frac{\text{local\_demand}}{\text{national\_avg\_demand}} + \text{remote\_work\_factor} - 1 \right) $$
    ```python
    def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
        return 1 + gamma * (local_demand/national_avg_demand + remote_work_factor - 1)
    ```
-   **Systematic Opportunity ($H^R$)**
    $$ H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}} $$
    ```python
    def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
        return h_base * growth_multiplier * regional_multiplier
    ```

**Synergy Components**:
-   **Skills Match Score**
    $$ \text{Skills Match Score} = \frac{\sum_{s \in S} \left( \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) / 100 \right) \cdot \text{Importance}_s}{\sum_{s \in S} \text{Importance}_s} \times 100 $$
    ```python
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
    ```
-   **Timing Factor**
    $$ \text{Timing Factor} = \begin{cases} 1 & \text{if years\_experience} \le 0 \\ 1 + \frac{\text{years\_experience}}{5} & \text{if years\_experience} > 0 \end{cases} $$
    ```python
    def calculate_timing_factor(years_experience):
        if years_experience <= 0:
            return 1
        else:
            return 1 + (years_experience / 5)
    ```
-   **Alignment Factor**
    $$ \text{Alignment} = \frac{\text{skills\_match\_score}}{\text{max\_possible\_match}} \cdot \text{timing\_factor} $$
    ```python
    def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
        return (skills_match_score / max_possible_match) * timing_factor
    ```
-   **Synergy Percentage**
    $$ \text{Synergy}\% = \frac{V^R \cdot H^R \cdot \text{Alignment}}{100.0} $$
    ```python
    def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
        return (vr_score * hr_score * alignment_factor) / 100.0
    ```

**Final AI-Readiness Score**
-   **AI-Readiness Score ($AI-R_{i,t}$)**
    $$ AI-R_{i,t} = \alpha \cdot V^R_{\text{score}} + (1-\alpha) \cdot H^R_{\text{score}} + \beta \cdot \text{synergy\_percentage} $$
    ```python
    def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
        return alpha * vr_score + (1-alpha) * hr_score + beta * synergy_percentage
    ```

**Pathway Simulation**
-   **Simulate Pathway Impact on $V^R$ Components**
    $$ \text{Component}_{\text{new}} = \min(\text{current\_component} + \text{impact\_component} \cdot \text{completion\_score} \cdot \text{mastery\_score}, 1.0) $$
    (Applied to AI-Fluency, Domain-Expertise, Adaptive-Capacity)
    ```python
    def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, pathway_type, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
        ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
        domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
        adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

        ai_fluency = min(ai_fluency, 1.0)
        domain_expertise = min(domain_expertise, 1.0)
        adaptive_capacity = min(adaptive_capacity, 1.0)

        return ai_fluency, domain_expertise, adaptive_capacity
    ```

