"""Test class for GS1 number calculations."""
import pytest

from gsone import gsone


def test_01_calculate_check_digit():
    """Calculate check digit for SSCC."""
    assert gsone.calculate_check_digit("01213456000000001") == 5


def test_02_calculate_check_digit():
    """Calculate check digit for GTIN-13."""
    assert gsone.calculate_check_digit("629104150022") == 0


def test_03_calculate_check_digit():
    """Calculate check digit for GTIN-13."""
    assert gsone.calculate_check_digit("62910415001") == 7


def test_04_calculate_check_digit():
    """Calculate check digit for GTIN-8."""
    assert gsone.calculate_check_digit("1111111") == 5


def test_05_get_barcode_gtin8():
    """Get gtin8 with company_prefix=123, serial=32."""
    gtin8 = gsone.get_barcode_gtin8("123", "32", app_id="", ext="")
    assert gtin8 == "12300327"


def test_06_get_barcode_gtin12():
    """Get gtin12 with company_prefix=123, serial=32."""
    gtin12 = gsone.get_barcode_gtin12("123", "32", app_id="", ext="")
    assert gtin12 == "123000000327"


def test_07_get_barcode_gtin13():
    """Get gtin13 with company_prefix=123, serial=32."""
    gtin13 = gsone.get_barcode_gtin13("123", "32", app_id="", ext="")
    assert gtin13 == "1230000000321"


def test_08_get_barcode_gtin14():
    """Get gtin14 with company_prefix=123, serial=32."""
    gtin14 = gsone.get_barcode_gtin14("123", "32", app_id="", ext="")
    assert gtin14 == "12300000000327"


def test_09_get_barcode_gsin():
    """Get gsin with company_prefix=123, serial=32."""
    gsin = gsone.get_barcode_gsin("123", "32", app_id="", ext="")
    assert gsin == "12300000000000321"


def test_10_get_barcode_sscc():
    """Get sscc with company_prefix=123, serial=32."""
    sscc = gsone.get_barcode_sscc("123", "32", app_id="", ext="")
    assert sscc == "123000000000000327"


def test_11_get_barcode_sscc():
    """Get SSCC with company_prefix=1044670, serial=1282329809."""
    sscc = gsone.get_barcode_sscc("1044670", "128232980")
    assert sscc == "(00)0104467001282329809"
    sscc = gsone.get_barcode_sscc("1044670", "128232980", app_id="", ext="")
    assert sscc == "104467001282329809"


def test_12_get_barcode_sscc():
    """Get SSCC with company_prefix=1044670, serial=01282329809."""
    sscc = gsone.get_barcode_sscc("1044670", "0128232980")
    assert sscc == "(00)0104467001282329809"


def test_13_get_barcode_sscc():
    """Try to use too long serial."""
    with pytest.raises(ValueError):
        gsone.get_barcode_sscc("1044670", "1111110128232980")
