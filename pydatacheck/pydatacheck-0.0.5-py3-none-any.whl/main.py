import pylogconf.core
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch, get_free_args


from pydatacheck.static import APP_NAME, VERSION_STR
from pydatacheck.data_check_books import do_check_books
from pydatacheck.data_check_videos import do_check_videos


@register_endpoint(
    description="check videos",
)
def check_videos() -> None:
    do_check_videos(get_free_args())


@register_endpoint(
    description="check books",
)
def check_books() -> None:
    do_check_books(get_free_args())


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
