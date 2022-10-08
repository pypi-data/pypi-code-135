import typer

help_msg = "Skyler CLI: The multitool I always wanted to build myself"
app = typer.Typer(
    help=help_msg,
    no_args_is_help=True,
)


@app.command()
def main():
    print("Hello World!")


@app.command()
def delete_me():
    print("Foo")


if __name__ == "__main__":
    app()
