"""Test suite for assuming.py"""
from assuming import AssumptionException, assume

from pytest import fail


def test_assume():
    # no assumptions
    def f(x: int) -> int:
        return x + 1

    assert (
        f(2) == 3
    ), f"(expected return value) 3 != {f(2)} = f(2) (actual return value)"

    # assumption; no ret; no msg
    @assume(lambda x: x > 10)
    def f(x: int) -> int:
        return x + 1

    try:
        f(2)
    except Exception as e:
        if type(e) == AssumptionException:
            assert (
                e.msg == "Assumption evaluated false"
            ), f'(expected exception message) "Assumption evaluated false" != "{e.msg}" (actual exception message)'
        else:
            fail(
                reason=f"(expected exception type) AssumptionException was not thrown f(2) threw {type(e)} (actual exception type"
            )

    # assumption; ret; no msg
    @assume(lambda x: x > 10, -1)
    def f(x: int) -> int:
        return x + 1

    assert f(2) == -1, f"(expected) -1 != {f(2)} = f(2) (actual)"

    # assumption; no ret; msg
    @assume(lambda x: x > 10, msg="x needs to be greater than 10")
    def f(x: int) -> int:
        return x + 1

    try:
        f(2)
    except Exception as e:
        if type(e) == AssumptionException:
            assert (
                e.msg == "x needs to be greater than 10"
            ), f'(expected exception message) "x needs to be greater than 10" != "{e.msg}" (actual exception message)'
        else:
            fail(
                reason=f"(expected exception type) AssumptionException was not thrown f(2) threw {type(e)} (actual exception type)"
            )

    # assumption; ret; msg
    @assume(lambda x: x > 10, ret=-1, msg="x needs to be greater than 10")
    def f(x: int) -> int:
        return x + 1

    assert f(2) == -1, f"(expected) -1 != {f(2)} = f(2) (actual)"
