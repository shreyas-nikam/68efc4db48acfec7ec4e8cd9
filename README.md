# QuLab: AI-Readiness Score Application

## Project Title and Description

QuLab is a Streamlit application designed to assess and simulate individual AI-Readiness. It uses the AI-Readiness Score (AI-R) framework to quantify an individual's preparedness for AI-enabled careers by considering both individual capabilities and market opportunities. The application helps users understand their current standing, explore different learning pathways, and analyze various career paths based on market demand and personal skills.

## Features

*   **AI-Readiness Score Calculator**: Calculates a comprehensive AI-Readiness score based on individual skills, experience, market opportunities, and synergy factors.
*   **Pathway Simulation**: Allows users to simulate the impact of different learning pathways on their AI fluency, domain expertise, and adaptive capacity, providing insights into skill development and career readiness.
*   **Data Exploration**: Provides interactive tables to explore the underlying datasets, including individual profiles, occupational data, learning pathways, and skill requirements.
*   **Interactive Visualizations**: Generates charts and graphs to visualize the contributions of various factors to the overall AI-Readiness score and the impact of pathway simulations.
*   **Customizable Parameters**: Allows users to adjust weights and coefficients in the AI-Readiness model to reflect their priorities and perspectives.
*   **"What-If" Scenarios**: Facilitates the analysis of different career paths based on market demand and personal capabilities.

## Getting Started

These instructions will guide you on how to install and run the QuLab application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python**: Version 3.8 or higher is recommended.
*   **Pip**: Python package installer (usually comes with Python).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

    Replace `<repository_url>` with the actual URL of your QuLab repository and `<repository_directory>` with the folder you cloned it to.

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    *   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    ```bash
    pip install streamlit pandas plotly
    ```

## Usage

1.  **Navigate to the project directory** in your terminal if you haven't already.

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

3.  **Access the application** in your web browser. Streamlit will provide the URL (usually `http://localhost:8501`).

4.  **Navigate using the sidebar**: Use the "Navigation" dropdown in the sidebar to access the different sections of the application:
    *   AI-Readiness Score Calculator
    *   Pathway Simulation
    *   Data Exploration

5.  **AI-Readiness Score Calculator**:
    *   Adjust the sliders and input fields to reflect your individual profile and target occupation.
    *   Observe the calculated AI-Readiness score and its components.
    *   Explore the visualizations to understand the contributions of different factors.

6.  **Pathway Simulation**:
    *   Select a learning pathway from the dropdown.
    *   Adjust the completion and mastery scores to reflect your progress.
    *   Click the "Simulate Pathway Impact" button to see the simulated changes in your AI fluency, domain expertise, and adaptive capacity.
    *   Analyze the comparison chart to understand the impact of the pathway.

7.  **Data Exploration**:
    *   Browse the interactive data tables to examine the underlying datasets.
    *   Use the expanders to view the contents of each DataFrame.

## Project Structure

```
QuLab/
├── app.py                          # Main Streamlit application file
├── application_pages/
│   ├── page1.py                  # AI-Readiness Score Calculator page
│   ├── page2.py                  # Pathway Simulation page
│   ├── page3.py                  # Data Exploration page
├── README.md                     # Project documentation
└── venv/                         # Virtual environment (optional, but recommended)
```

*   `app.py`: The main entry point for the Streamlit application. It sets up the sidebar navigation and calls the appropriate page based on user selection.
*   `application_pages/`: This directory contains the individual pages of the application, each implemented as a separate Python file.
    *   `page1.py`: Implements the AI-Readiness Score Calculator, including input widgets, calculations, visualizations, and data tables.
    *   `page2.py`: Implements the Pathway Simulation, allowing users to simulate the impact of learning pathways on their AI fluency, domain expertise, and adaptive capacity.
    *   `page3.py`: Implements the Data Exploration page, providing interactive tables to explore the underlying datasets.
*   `README.md`: This file provides an overview of the project, instructions for installation and usage, and other relevant information.
*   `venv/`: The virtual environment directory (if created) contains the project's dependencies.

## Technology Stack

*   **Python**: Core programming language
*   **Streamlit**: Web framework for creating interactive data applications
*   **Pandas**: Data manipulation and analysis library
*   **Plotly**: Interactive visualization library

## Contributing

Contributions are welcome! Here's how you can contribute:

1.  **Fork the repository:** Create a copy of the project in your GitHub account.
2.  **Create a new branch:**  For each feature or bug fix, create a new branch with a descriptive name.
3.  **Make your changes:** Implement the feature or fix the bug.
4.  **Test your changes:** Ensure that your changes work as expected and do not introduce new issues.
5.  **Commit your changes:** Write clear and concise commit messages.
6.  **Push your changes to your fork:** Upload your branch to your forked repository.
7.  **Create a pull request:** Submit a pull request from your branch to the main repository.

Please follow these guidelines when contributing:

*   Write clean, well-documented code.
*   Follow the project's coding style.
*   Provide tests for your changes.
*   Write clear and concise commit messages.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.  *(Replace `LICENSE` with the actual license file name if different or link to the full license text).*

## Contact

If you have any questions or suggestions, please feel free to contact us:

*   [Your Name/Organization]
*   [Your Email]
*   [Link to Your Website/Portfolio (optional)]
