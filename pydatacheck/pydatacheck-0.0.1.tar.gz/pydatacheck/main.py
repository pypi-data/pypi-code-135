import pylogconf.core
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch

from pydatacheck.static import APP_NAME, VERSION_STR


@register_endpoint(
    description="check movies",
)
def tbd() -> None:
    print("tbd")


@register_main(
    main_description="pydatacheck will check your yaml files for you",
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
