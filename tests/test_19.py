import pytest
from definition_c2a85c494c3a4eea891b811a1c936da3 import calculate_skills_match_score
import pandas as pd


def test_calculate_skills_match_score_empty_dataframes():
    user_skills_df = pd.DataFrame({'skill_name': [], 'individual_skill_score': []})
    required_skills_df = pd.DataFrame({'skill_name': [], 'required_skill_score': [], 'skill_importance': []})
    assert calculate_skills_match_score(user_skills_df, required_skills_df) is None


def test_calculate_skills_match_score_no_skill_overlap():
    user_skills_df = pd.DataFrame({'skill_name': ['Python', 'Communication'], 'individual_skill_score': [80, 90]})
    required_skills_df = pd.DataFrame({'skill_name': ['Java', 'Leadership'], 'required_skill_score': [70, 85], 'skill_importance': [0.8, 0.9]})
    assert calculate_skills_match_score(user_skills_df, required_skills_df) == 0


def test_calculate_skills_match_score_perfect_match():
    user_skills_df = pd.DataFrame({'skill_name': ['Python', 'Communication'], 'individual_skill_score': [100, 100]})
    required_skills_df = pd.DataFrame({'skill_name': ['Python', 'Communication'], 'required_skill_score': [100, 100], 'skill_importance': [1, 1]})
    assert calculate_skills_match_score(user_skills_df, required_skills_df) == 100


def test_calculate_skills_match_score_some_overlap():
    user_skills_df = pd.DataFrame({'skill_name': ['Python', 'Communication', 'Java'], 'individual_skill_score': [80, 90, 70]})
    required_skills_df = pd.DataFrame({'skill_name': ['Python', 'Leadership', 'Communication'], 'required_skill_score': [70, 85, 95], 'skill_importance': [0.8, 0.9, 0.7]})
    # Expected: ((min(80, 70)/100)*0.8) + ((min(90, 95)/100)*0.7)  = (70/100)*0.8 + (90/100)*0.7 = 0.56 + 0.63 = 1.19 . Needs to be divided by the sum of skill importance = 0.8+0.9+0.7 = 2.4. 1.19/2.4*100 = 49.58
    expected_score = ((min(80, 70)/100)*0.8 + (min(90, 95)/100)*0.7) / (0.8+0.9+0.7)*100
    assert abs(calculate_skills_match_score(user_skills_df, required_skills_df) - expected_score) < 0.01


def test_calculate_skills_match_score_skill_importance_zero():
    user_skills_df = pd.DataFrame({'skill_name': ['Python'], 'individual_skill_score': [80]})
    required_skills_df = pd.DataFrame({'skill_name': ['Python'], 'required_skill_score': [70], 'skill_importance': [0]})
    assert calculate_skills_match_score(user_skills_df, required_skills_df) == 0