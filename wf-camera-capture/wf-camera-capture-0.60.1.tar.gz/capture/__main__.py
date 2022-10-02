import click

from capture import capture_loop, upload_loop


@click.group()
def main():
    pass


@main.command()
def capture():
    capture_loop()


@main.command()
def upload():
    upload_loop()


if __name__ == '__main__':
    main()
