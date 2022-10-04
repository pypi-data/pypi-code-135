import argparse
import asyncio
from . import PPGEE


def get_args():
    parser = argparse.ArgumentParser(description="Confirm your montly PPGEE attendency")
    parser.add_argument("username", type=str, help="Your PPGEE's username")
    parser.add_argument("password", type=str, help="Your PPGEE's password")
    return parser.parse_args()


async def cli():
    args = get_args()
    user, password = args.username, args.password
    async with PPGEE(user=user, password=password) as ppgee:
        frequency_page = await ppgee.frequency()
        await asyncio.sleep(1)
        if frequency_page.is_available():
            print("Attendency confirmed.")
            await frequency_page.confirm()
        else:
            print("Attendency not available yet.")
        await asyncio.sleep(1)

def main():
    asyncio.run(cli())

if __name__ == "__main__":
    main()
