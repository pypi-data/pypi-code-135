def escape(text: str) -> str:
    return text.replace('_', '\\_')


# underline
def uline(string: str, char: str = "="):
    return char * len(string)


# escape underline
def euline(string: str, char: str = "="):
    return uline(escape(string), char=char)


jinja_filters = dict(
    escape=escape,
    euline=euline,
    uline=uline,
)
