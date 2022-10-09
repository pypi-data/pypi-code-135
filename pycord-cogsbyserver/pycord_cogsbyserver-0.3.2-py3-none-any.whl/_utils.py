from discord import Guild, Reaction

DMS = 0

def find_guild(args: list) -> Guild or None:
    match args:
        case [first, *_] if hasattr(first, "guild"):
            return first.guild
        case [first, *_] if isinstance(first, Guild):
            return first
        case [first, *_] if isinstance(first, Reaction):
            return first.message.guild
        case [*_]:
            return DMS
        case _:
            raise ValueError("args must be a list")