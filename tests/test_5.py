import pytest
from definition_38806b6838b34eb5a99b2b3420b10fda import calculate_education_foundation


@pytest.mark.parametrize(
    "education_level, expected",
    [
        ("PhD", 1.0),
        ("Master's", 0.8),
        ("Bachelor's", 0.6),
        ("Associate's/Certificate", 0.4),
        ("HS + significant coursework", 0.2),
        ("Some College", 0.3),
        ("", 0.0),
        (None, 0.0),
    ],
)
def test_calculate_education_foundation(education_level, expected):
    assert calculate_education_foundation(education_level) == expected