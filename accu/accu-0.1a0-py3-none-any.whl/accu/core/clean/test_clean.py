from .svg import ALLOWED_ELEMENTS_SVG, sanitize_svg

SVG_BAS_STRING = "<svg><script>alert('xss')</script></svg>"


def test_true():
    assert True


def test_sanitize_svg():
    """Test that the svg sanitizer works."""
    assert sanitize_svg(SVG_BAS_STRING) == "<svg>alert('xss')</svg>"
    assert (
        sanitize_svg(SVG_BAS_STRING, strip=False)
        == "<svg>&lt;script&gt;alert('xss')&lt;/script&gt;</svg>"
    )
    assert sanitize_svg(SVG_BAS_STRING, strip=True) == "<svg>alert('xss')</svg>"

    ### Advanced options
    EXTENDED_BASE_STRING = f"<xyz>{SVG_BAS_STRING}</xyz>"
    # Normal run
    assert sanitize_svg(EXTENDED_BASE_STRING) == "<svg>alert('xss')</svg>"
    # Allow custom tag
    assert (
        sanitize_svg(EXTENDED_BASE_STRING, elements=ALLOWED_ELEMENTS_SVG + ["xyz"])
        == "<xyz><svg>alert('xss')</svg></xyz>"
    )
