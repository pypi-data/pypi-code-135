import argparse


def vpnkillswitch():
    main_group_parser = argparse.ArgumentParser(description="My Bool Argparse Script")
    mutually_exclusive_group = main_group_parser.add_mutually_exclusive_group()
    mutually_exclusive_group.add_argument("--on", action="store_true")
    mutually_exclusive_group.add_argument("--off", action="store_true")
    mutually_exclusive_group.add_argument("--protect", action="store_true")
    mutually_exclusive_group.add_argument("--vpn", action="store_true")
    mutually_exclusive_group.add_argument("--docker", action="store_true")

    my_args = main_group_parser.parse_args()

    print(my_args)
