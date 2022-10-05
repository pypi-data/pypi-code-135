import regex
from bleach import clean
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def strip_html_tags(value: str, raise_error=True, field_name=None):
    """Strip HTML tags from an input string using the bleach library.

    If raise_error is True, a ValidationError will be thrown if HTML tags are detected
    """

    cleaned = clean(
        value,
        strip=True,
        tags=[],
        attributes=[],
    )

    # Add escaped characters back in
    replacements = {
        "&gt;": ">",
        "&lt;": "<",
        "&amp;": "&",
    }

    for o, r in replacements.items():
        cleaned = cleaned.replace(o, r)

    # If the length changed, it means that HTML tags were removed!
    if len(cleaned) != len(value) and raise_error:

        field = field_name or "non_field_errors"

        raise ValidationError({field: [_("Remove HTML tags from this value")]})

    return cleaned


def remove_non_printable_characters(value: str, remove_ascii=True, remove_unicode=True):
    """Remove non-printable / control characters from the provided string"""

    if remove_ascii:
        # Remove ASCII control characters
        cleaned = regex.sub("[\x01-\x1F]+", "", value)

    if remove_unicode:
        # Remove Unicode control characters
        cleaned = regex.sub(r"[^\P{C}]+", "", value)

    return cleaned
