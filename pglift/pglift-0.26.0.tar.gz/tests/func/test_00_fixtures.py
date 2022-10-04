from pglift.ctx import Context
from pglift.models import system
from pglift.settings import Settings


def test_standby(
    settings: Settings,
    ctx: Context,
    instance: system.Instance,
    standby_settings: Settings,
    standby_ctx: Context,
    standby_instance: system.Instance,
) -> None:
    assert ctx != standby_ctx
    assert settings != standby_settings
    assert instance._settings == ctx.settings == settings
    assert standby_instance._settings == standby_ctx.settings == standby_settings
