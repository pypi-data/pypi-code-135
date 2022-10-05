from pathlib import Path


def is_true(x):
    """Shortcut function to determine if a value "looks" like a boolean"""
    return str(x).strip().lower() in ["1", "y", "yes", "t", "true", "on"]


def get_base_dir() -> Path:
    """Returns the base (top-level) InvenTree directory."""
    return Path(__file__).parent.parent.resolve()
