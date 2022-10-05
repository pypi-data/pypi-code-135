import typer

app = typer.Typer(help="Ferramentas para a Analize CLI.")


@app.command()
def ip(username: str):
    """
    Mostra o ip da máquina.
    """
    print(f"Creating user: {username}")


if __name__ == "__main__":
    app()
