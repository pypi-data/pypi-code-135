import re

import pytest

from magnetismi.model import cof


def test_coefficients_from_past_before_models_available():
    msg = r'requested year (1234) not within (2020, 2021, 2022, 2023, 2024, 2025)'
    with pytest.raises(ValueError, match=re.escape(msg)):
        cof.Coefficients(1234)


def test_coefficients_from_future_after_models_available():
    msg = r'requested year (9876) not within (2020, 2021, 2022, 2023, 2024, 2025)'
    with pytest.raises(ValueError, match=re.escape(msg)):
        cof.Coefficients(9876)


def test_coefficients_from_within_models_available():
    coefficients = cof.Coefficients(2022)
    assert coefficients.model['epoch'] == 2020
    assert coefficients.model['model_code'] == 'WMM-2020'
    assert coefficients.model['model_date_string'] == '12/10/2019'
    assert len(coefficients.model['coeffs']) == 90


def test_coefficients_2020_slot_1_0():
    slot_1_2 = {c: val for c, val in zip(cof.CS, (1, 0, -29404.5, 0.0, 6.7, 0.0))}
    coefficients = cof.Coefficients(2024)
    assert coefficients.model['coeffs'][0] == slot_1_2


def test_coefficients_2020_slot_12_12():
    slot_12_12 = {c: val for c, val in zip(cof.CS, (12, 12, -0.3, 0.5, -0.1, -0.1))}
    coefficients = cof.Coefficients(2024)
    assert coefficients.model['coeffs'][-1] == slot_12_12
