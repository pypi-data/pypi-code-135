"""Helper functions for GS1 barcode standard."""
from itertools import cycle

CHECK_DIGIT_FACTORS = (3, 1)
# Defaults.
APP_ID = "(00)"
EXT = "0"
# TODO: replace this with dataclass, once we can drop 3.6 support.
BARCODE_LENGTHS = {
    "gtin-8": 7,
    "gtin-12": 11,
    "gtin-13": 12,
    "gtin-14": 13,
    "gsin": 16,
    "sscc": 17,
}


def calculate_check_digit(number: str) -> int:
    """Calculate check digit according to GS1 rules."""
    factors = cycle(CHECK_DIGIT_FACTORS)
    # Step 1. Multiply by factor
    # Step 2. Sum multiplied numbers
    total = sum(int(n) * next(factors) for n in reversed(number))
    # Step 3. Subtract the sum from nearest equal or higher multiple of ten
    ten_remainder = 10 - total % 10
    return ten_remainder % 10


def get_barcode_gtin8(
    company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    """Combine serial with company prefix to form gtin-8 barcode."""
    return _get_barcode(
        "gtin-8", company_prefix, serial, app_id=app_id, ext=ext
    )


def get_barcode_gtin12(
    company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    """Combine serial with company prefix to form gtin-12 barcode."""
    return _get_barcode(
        "gtin-12", company_prefix, serial, app_id=app_id, ext=ext
    )


def get_barcode_gtin13(
    company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    """Combine serial with company prefix to form gtin-13 barcode."""
    return _get_barcode(
        "gtin-13", company_prefix, serial, app_id=app_id, ext=ext
    )


def get_barcode_gtin14(
    company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    """Combine serial with company prefix to form gtin-14 barcode."""
    return _get_barcode(
        "gtin-14", company_prefix, serial, app_id=app_id, ext=ext
    )


def get_barcode_gsin(
    company_prefix: str, serial: str, app_id: str = APP_ID, ext: str = EXT
) -> str:
    """Combine serial with company prefix to form gsin barcode."""
    return _get_barcode(
        "gsin", company_prefix, serial, app_id=app_id, ext=ext
    )


def get_barcode_sscc(
    company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    """Combine serial number with company prefix to form SSCC barcode.

    Additionally, Application Identifier and Extension are included at
    the start of barcode. Can pass empty string, to omit that.
    """
    return _get_barcode("sscc", company_prefix, serial, app_id=app_id, ext=ext)


def _get_barcode(
    type_: str, company_prefix: str, serial: str, app_id=APP_ID, ext=EXT
) -> str:
    len_needed = BARCODE_LENGTHS[type_]
    len_got = len(serial + company_prefix)
    padding = len_needed - len_got
    if padding < 0:
        raise ValueError(
            f"Barcode expects to be of {len_needed} length "
            + "(without check digit). "
            + f"Got {len_got} length. Make sure company_prefix and/or serial "
            + f"are not too long for barcode of type {type_}."
        )
    sscc_raw = f"{company_prefix}{''.zfill(padding)}{serial}"
    cdigit = calculate_check_digit(sscc_raw)
    return f"{app_id}{ext}{sscc_raw}{cdigit}"
