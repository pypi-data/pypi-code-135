from .models import HandlerConfig, DeadMansConfig

GLOBALS = globals()
HANDLERS: dict = GLOBALS.setdefault("handlers", {})
CONFIG: HandlerConfig | None = GLOBALS.setdefault("config", None)
DEADMANS_CONFIG: DeadMansConfig | None = GLOBALS.setdefault("deadmans_config", None)
