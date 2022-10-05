from functools import wraps


def auth_exempt(view_func):
    """Mark a view function as being exempt from auth requirements."""

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    wrapped_view.auth_exempt = True
    return wraps(view_func)(wrapped_view)
