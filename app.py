"""import streamlit as st
st.set_page_config(page_title=\"QuLab\", layout=\"wide\")
st.sidebar.image(\"https://www.quantuniversity.com/assets/img/logo5.jpg\")
st.sidebar.divider()
st.title(\"QuLab\")
st.divider()
st.markdown(\"\"\"In this lab, we explore the AI-Readiness Score (AI-R) framework, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. The AI-R score helps in navigating career transitions by considering both individual capabilities and market opportunities.\n\n### Learning Goals\n-   Understand the key insights contained in the uploaded document and supporting data.\n-   Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.\n-   Evaluate the potential impact of various learning pathways on individual skill development and career readiness.\n-   Analyze different career paths based on market demand and personal capabilities through \"what-if\" scenarios.\n\n$\alpha$: Weight on Individual Factors (0 to 1)\n$\beta$: Synergy Coefficient (0 to 1)\"\"\")

# Your code starts here
page = st.sidebar.selectbox(label=\"Navigation\", options=[\"AI-Readiness Score Calculator\", \"Pathway Simulation\", \"Data Exploration\"])

if page == \"AI-Readiness Score Calculator\":
    from application_pages.page1 import run_page1
    run_page1()
elif page == \"Pathway Simulation\":
    from application_pages.page2 import run_page2
    run_page2()
elif page == \"Data Exploration\":
    from application_pages.page3 import run_page3
    run_page3()
# Your code ends
"""