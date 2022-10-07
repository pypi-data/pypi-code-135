from joj_auth.joj import get_joj_sid
from typer import Typer, echo
import asyncio
import sys

app = Typer(add_completion=False)


@app.command("joj")
def echo_joj_sid():
    """
    Get the SID from JOJ cookies.
    """
    try:
        res = asyncio.get_event_loop().run_until_complete(get_joj_sid())
        echo("Here is your SID:", file=sys.stderr)
        echo(res)
    except Exception as e:
        echo("Oops, Something went wrong. Please try again.", file=sys.stderr)
        echo(e, file=sys.stderr)

if __name__ == "__main__":
    app()
