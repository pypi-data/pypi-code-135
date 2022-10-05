from typing import Any

from django.conf import LazySettings

DEFAULT_SETTINGS = {
    "EXTRA_URL_SCHEMES": [],
}


class NoValue:
    """A custom class that shows nothing was found."""


class CustomLazySettings(LazySettings):
    """Custom settings class to replace django settings.

    This class is used to provide defaults for settings which are not defined in the configuration file.
    These are placed on top of the default settings provided by django.

    Callflow:
    1. django.conf.settings
    2. accu.core.settings.DEFAULT_SETTINGS
    """

    def __getattr__(self, item: Any) -> Any:
        """Override the __getattr__ method to provide default values for settings.

        Args:
            item: The setting name

        Returns:
            The setting value
        """

        try:
            # Lookup the setting the django way
            result = super().__getattr__(item)
        except AttributeError:
            # Not Found, try to get the default value
            result = DEFAULT_SETTINGS.get(item, NoValue)
            if result is NoValue:
                raise AttributeError(f"Setting '{item}' is not defined")

        return result


settings = CustomLazySettings()
