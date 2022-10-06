from .user import bp as nested_user_view
from .menu import bp as nested_menu_view

nested_views = [
    nested_user_view,
    nested_menu_view
]
