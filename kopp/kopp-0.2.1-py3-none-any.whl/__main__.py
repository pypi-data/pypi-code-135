import argparse

from .main import kopp


def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="text to convert", type=str)
    args = parser.parse_args()

    print(kopp(args.text))


if __name__ == "__main__":
    cli()
