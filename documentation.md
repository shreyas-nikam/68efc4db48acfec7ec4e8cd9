id: 68efc4db48acfec7ec4e8cd9_documentation
summary: AI-Readiness score Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab Codelab: AI-Readiness Score Exploration

This codelab provides a comprehensive guide to understanding and utilizing the QuLab Streamlit application, which focuses on evaluating AI-Readiness. The AI-Readiness Score (AI-R) framework helps individuals quantify their preparedness for AI-enabled careers by considering their capabilities and market opportunities. Through this codelab, you'll learn how to use the application's features to assess AI-Readiness, simulate learning pathways, and explore the underlying data.

**Importance:**

In today's rapidly evolving job market, understanding one's readiness for AI-driven roles is crucial. This application provides a framework to:

*   Identify skill gaps.
*   Evaluate career path options in the AI landscape.
*   Simulate the impact of learning on AI-Readiness.
*   Understand the interplay between individual skills and market demands.

**Concepts Explained:**

*   **AI-Readiness Score (AI-R):** A composite score that quantifies an individual's preparedness for AI-enabled careers.
*   **Idiosyncratic Readiness ($V^R$):** Represents an individual's capabilities and skills related to AI.
*   **Systematic Opportunity ($H^R$):** Reflects the market demand and opportunities for AI-related roles.
*   **Synergy:** The alignment between individual readiness and market opportunity.
*   **Learning Pathways:** Structured programs or courses designed to enhance specific skills.

## Setting Up the Environment
Duration: 00:05

Before diving into the application, ensure you have the following:

1.  **Python 3.7+:** The application is built using Python.
2.  **Streamlit:** Install Streamlit using pip: `pip install streamlit`
3.  **Required Libraries:** The application uses `pandas` and `plotly`. Install them using: `pip install pandas plotly`
4.  **Download the Code:** Download or clone the provided code repository containing `app.py` and the `application_pages` directory.

## Running the Application
Duration: 00:02

1.  Open your terminal or command prompt.
2.  Navigate to the directory containing `app.py`.
3.  Run the application using the command: `streamlit run app.py`

This will launch the Streamlit application in your web browser.

## Navigating the Application
Duration: 00:03

The application consists of three main pages accessible via a sidebar:

*   **AI-Readiness Score Calculator:**  This page allows you to calculate your AI-Readiness Score based on various input parameters.
*   **Pathway Simulation:** This page enables you to simulate the impact of different learning pathways on your AI-Readiness.
*   **Data Exploration:** This page provides a view of the underlying data used in the application.

## AI-Readiness Score Calculator
Duration: 00:20

This page is the core of the QuLab application. It allows you to compute your AI-Readiness Score ($AI-R_{i,t}$) based on individual factors and market opportunities.

**Functionality:**

1.  **Global Parameters:**
    *   **Weight on Individual Factors ($\alpha$):**  A slider to adjust the weight given to individual readiness ($V^R$) versus market opportunity ($H^R$) in the overall score.  Values range from 0 to 1.
    *   **Synergy Coefficient ($\beta$):** A slider to control the impact of synergy between individual readiness and market opportunity. Values range from 0 to 1.

2.  **Idiosyncratic Readiness ($V^R$) Inputs:**
    *   **AI-Fluency Sub-Components:** Sliders to input scores for:
        *   Prompting Score ($S_{i,1}$)
        *   Tools Score ($S_{i,2}$)
        *   Understanding Score ($S_{i,3}$)
        *   Data Literacy Score ($S_{i,4}$)
        *   Output Quality with AI
        *   Output Quality without AI
        *   Time without AI (hours)
        *   Time with AI (hours)
        *   Errors Caught
        *   Total AI Errors
        *   Appropriate Trust Decisions
        *   Total Decisions
        *   Delta Proficiency
        *   Delta T Hours Invested

    *   **Domain-Expertise Sub-Components:** Input fields for:
        *   Education Level (Selectbox)
        *   Years Experience (Slider)
        *   Portfolio Score (Slider)
        *   Recognition Score (Slider)
        *   Credentials Score (Slider)

    *   **Adaptive-Capacity Sub-Components:** Sliders to input scores for:
        *   Cognitive Flexibility
        *   Social-Emotional Intelligence
        *   Strategic Career Management

3.  **Systematic Opportunity ($H^R$) Inputs:**
    *   **Target Occupation:** A selectbox to choose a target occupation from a predefined list.  This selection determines the market opportunity data used in the calculation.
    *   **Market Multiplier Parameters:**
        *   Lambda value for Growth Multiplier ($\lambda$) - Slider to adjust volatility in job posting growth.
        *   Gamma value for Regional Multiplier ($\gamma$) - Slider to adjust regional market influence.

4.  **Synergy Inputs:**
    *   **Max Possible Skills Match:** Manual Input.

**Calculations:**

The page uses several functions (defined in `application_pages/page1.py`) to calculate the AI-Readiness Score:

1.  **AI-Fluency:**

    *   Technical AI Skills:  $TechnicalAISkills = \frac{Prompting + Tools + Understanding + DataLit}{4}$
    *   AI Augmented Productivity: $AI\_Augmented\_Productivity = \frac{OutputQualityWithAI}{OutputQualityWithoutAI} * \frac{TimeWithoutAI}{TimeWithAI}$
    *   Critical AI Judgment: $CriticalAIJudgment = 1 - \frac{(\frac{ErrorsCaught}{TotalAIErrors} + \frac{AppropriateTrustDecisions}{TotalDecisions})}{2}$
    *   AI Learning Velocity: $AI\_Learning\_Velocity = \frac{DeltaProficiency}{DeltaTHoursInvested}$
    *   AI Fluency: $AI\_Fluency = 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4$

2.  **Domain-Expertise:**

    *   Education Foundation: Based on Education Level (PhD = 1.0, Master's = 0.8, etc.)
    *   Practical Experience: $PracticalExperience = \frac{YearsExperience}{YearsExperience + \frac{1}{\gamma}}$, where $\gamma = 0.15$.
    *   Specialization Depth: $SpecializationDepth = \frac{PortfolioScore + RecognitionScore + CredentialsScore}{3}$
    *   Domain Expertise: $DomainExpertise = 0.125 * EducationFoundation + 0.25 * PracticalExperience + 0.625 * SpecializationDepth$

3.  **Adaptive-Capacity:**

    *   $AdaptiveCapacity = \frac{CognitiveFlexibility + SocialEmotionalIntelligence + StrategicCareerManagement}{3}$

4.  **Idiosyncratic Readiness ($V^R$):**

    *   $V^R = (w1 * AI\_Fluency) + (w2 * DomainExpertise) + (w3 * AdaptiveCapacity)$, where $w1 = 0.45$, $w2 = 0.35$, $w3 = 0.20$.

5.  **Systematic Opportunity ($H^R$):**

    *   AI Enhancement Potential: $AIEnhancement = AIEnhancementScore$
    *   Job Growth Projection: $JobGrowthNormalized = 50 + (GrowthRateG * 100)$,  normalized to 0-1 and capped between 0 and 100.
    *   Wage Premium: $WagePremium = \frac{AISkilledWage - MedianWage}{MedianWage}$
    *   Entry Accessibility: $EntryAccessibility = \frac{1}{1 + 0.1 * (EducationYearsRequired + ExperienceYearsRequired)}$
    *   Base Opportunity Score:  $H_{base} = (w1 * AIEnhancement + w2 * JobGrowthNormalized + w3 * WagePremium + w4 * EntryAccessibility)$, where $w1 = 0.30$, $w2 = 0.30$, $w3 = 0.25$, $w4 = 0.15$.
    *   Growth Multiplier: $GrowthMultiplier = (\frac{CurrentJobPostings}{PreviousJobPostings})^{\lambda}$, where $\lambda = 0.3$.
    *   Regional Multiplier: $RegionalMultiplier = 1 + \gamma * (\frac{LocalDemand}{NationalAvgDemand} + RemoteWorkFactor - 1)$, where $\gamma = 0.2$.
    *   Systematic Opportunity: $H^R = H_{base} * GrowthMultiplier * RegionalMultiplier$

6.  **Synergy:**
    *   Skills Match Score:  Calculated based on user and required skills.
    *   Timing Factor: $TimingFactor = 1 + (YearsExperience / 5)$
    *   Alignment Factor: $AlignmentFactor = (\frac{SkillsMatchScore}{MaxPossibleMatch}) * TimingFactor$
    *   Synergy Percentage: $SynergyPercentage = \frac{V^R * H^R * AlignmentFactor}{100}$

7.  **AI-Readiness Score ($AI-R_{i,t}$):**

    *   $AI-R_{i,t} = \alpha * V^R + (1 - \alpha) * H^R + \beta * SynergyPercentage$

**Output:**

The page displays the calculated scores:

*   Idiosyncratic Readiness ($V^R$)
*   Systematic Opportunity ($H^R$)
*   Synergy %
*   AI-Readiness Score ($AI-R_{i,t}$)

It also includes visualizations (pie chart for $V^R$ components, bar chart for $H_{base}$ components) and data tables for the underlying data.

## Pathway Simulation
Duration: 00:15

This page allows you to simulate the impact of different learning pathways on your Idiosyncratic Readiness ($V^R$).

**Functionality:**

1.  **Pathway Selection:** A selectbox to choose a learning pathway from the available options (defined in `learning_pathways_df`).

2.  **Pathway Completion & Mastery:** Sliders to define the completion score and mastery score for the selected pathway.

3.  **Simulation:**
    *   The page retrieves initial values for AI-Fluency, Domain-Expertise, and Adaptive-Capacity.  These values should ideally be persisted from the "AI-Readiness Score Calculator" page using `st.session_state`.
    *   When the "Simulate Pathway Impact" button is clicked, the `simulate_pathway_impact` function (defined in `application_pages/page2.py`) is called.

**Simulation Logic (simulate_pathway_impact function):**

```python
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
```

The function updates the AI-Fluency, Domain-Expertise, and Adaptive-Capacity scores based on the pathway's impact and the completion/mastery scores.  The updated scores are capped at 1.0.

**Output:**

The page displays the simulated values for AI-Fluency, Domain-Expertise, and Adaptive-Capacity after completing the selected pathway. A bar chart visualizes the change in $V^R$ components.

## Data Exploration
Duration: 00:05

This page provides a simple view of the data used in the application. It displays the contents of the following DataFrames (defined in `application_pages/page3.py`):

*   `individual_profiles_df`
*   `occupational_data_df`
*   `learning_pathways_df`
*   `occupation_required_skills_df`
*   `individual_skills_df`

This page is useful for understanding the structure and content of the data used in the calculations.

<aside class="positive">
  <b>Tip:</b> Use this page to explore and understand the data that drives the AI-Readiness Score.
</aside>

## Code Deep Dive
Duration: 01:00

Let's examine the code structure and key functions of the application.

**app.py:**

This is the main entry point of the Streamlit application. It sets the page configuration, displays the title and introduction, and handles navigation between the three pages.

```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown(
    """In this lab, we explore the AI-Readiness Score (AI-R) framework, a
parametric model designed to quantify an individual's preparedness for AI-enabled
careers. The AI-R score helps in navigating career transitions by considering both
individual capabilities and market opportunities.

### Learning Goals
-   Understand the key insights contained in the uploaded document and supporting data.
-   Decompose the AI-Readiness Score into its systematic opportunity ($H^R$),
idiosyncratic readiness ($V^R$), and synergy components.
-   Evaluate the potential impact of various learning pathways on individual skill
development and career readiness.
-   Analyze different career paths based on market demand and personal capabilities
through "what-if" scenarios.

$\alpha$: Weight on Individual Factors (0 to 1)
$\beta$: Synergy Coefficient (0 to 1)"""
)

# Your code starts here
page = st.sidebar.selectbox(
    label="Navigation",
    options=[
        "AI-Readiness Score Calculator",
        "Pathway Simulation",
        "Data Exploration",
    ],
)

if page == "AI-Readiness Score Calculator":
    from application_pages.page1 import run_page1

    run_page1()
elif page == "Pathway Simulation":
    from application_pages.page2 import run_page2

    run_page2()
elif page == "Data Exploration":
    from application_pages.page3 import run_page3

    run_page3()
# Your code ends
```

The core logic is in the `if/elif/else` block, which imports and executes the appropriate function (`run_page1`, `run_page2`, or `run_page3`) based on the selected page.

**application_pages/page1.py (AI-Readiness Score Calculator):**

This file contains the `run_page1` function, which implements the AI-Readiness Score Calculator.

Key aspects:

*   **Data Loading:** The code initializes the DataFrames (`individual_profiles_df`, `occupational_data_df`, `learning_pathways_df`, `occupation_required_skills_df`, `individual_skills_df`) with sample data. In a real-world application, this data would likely be loaded from external sources (CSV files, databases, etc.).

*   **Input Widgets:** The code uses Streamlit widgets (sliders, selectboxes, etc.) to collect user input for the various parameters.

*   **Calculation Functions:** The code defines a set of functions (e.g., `calculate_technical_ai_skills`, `calculate_ai_augmented_productivity`, `calculate_idiosyncratic_readiness`, `calculate_systematic_opportunity`, `calculate_ai_readiness_score`) that implement the mathematical formulas described earlier.

*   **Result Display:** The code uses `st.metric` to display the calculated scores and `plotly.express` to create visualizations.

*   **Data Tables:** The code utilizes `st.dataframe` within `st.expander` to show the DataFrames.

**application_pages/page2.py (Pathway Simulation):**

This file contains the `run_page2` function, which implements the Pathway Simulation.

Key aspects:

*   **Pathway Selection:** The code uses a selectbox to allow the user to choose a learning pathway.

*   **Simulation Logic:** The `simulate_pathway_impact` function calculates the impact of the selected pathway on the AI-Fluency, Domain-Expertise, and Adaptive-Capacity scores.

*   **Result Display:** The code displays the simulated scores and a comparison chart.

**application_pages/page3.py (Data Exploration):**

This file contains the `run_page3` function, which simply displays the DataFrames used in the application.

## Extending the Application
Duration: 00:30

Here are some ideas for extending the QuLab application:

1.  **Data Persistence:** Implement data persistence using `st.session_state` to store and retrieve user input and calculated scores across different pages. This would allow users to seamlessly transition between the "AI-Readiness Score Calculator" and "Pathway Simulation" pages.

2.  **Data Input:**  Allow users to upload their own data (e.g., individual profiles, skill assessments) in CSV format.

3.  **Database Integration:** Connect the application to a database to store and manage user data, career paths, and learning pathways.

4.  **Enhanced Visualizations:**  Add more interactive and informative visualizations to help users understand their AI-Readiness and identify areas for improvement.

5.  **Career Path Recommendations:**  Develop an algorithm to recommend career paths based on the user's AI-Readiness Score and skills profile.

6.  **Personalized Learning Recommendations:**  Provide personalized learning recommendations based on the user's skill gaps and career goals.

7.  **User Authentication:** Implement user authentication to allow users to save their progress and track their AI-Readiness over time.

8.  **Improve Skills Matching Algorithm:** Enhance the skills matching algorithm in the synergy calculation to provide a more accurate assessment of skills alignment. Consider fuzzy matching or incorporating skill proficiency levels.

9.  **Dynamic UI for Skills Input:** Replace the skills input on page 1 with a dynamic UI where users can add/remove skills and specify their proficiency, instead of just relying on the hardcoded individual_skills_df.

10. **Implement actual Data upload:** Instead of relying on generated data, provide functionality to upload csv files for individual profiles, job profiles etc. and process it to generate the results.

<aside class="negative">
  <b>Warning:</b>  Be mindful of data privacy and security when implementing data persistence and user authentication features.
</aside>

## Conclusion

This codelab provided a detailed walkthrough of the QuLab Streamlit application for assessing AI-Readiness. You learned how to use the application's features to calculate your AI-Readiness Score, simulate learning pathways, and explore the underlying data. By extending the application with the suggested enhancements, you can create a powerful tool to help individuals navigate the evolving AI landscape.
