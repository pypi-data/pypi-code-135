#!/usr/bin/env python3
from capstone_api.class_api import ClassAPI
#from capstone_api.discord_api import DiscordAPI
#from capstone_api.canvas_api import CanvasAPI
import argparse
import sys


def output(args):
    capstone = ClassAPI()
    df = capstone.loadStudents()
    teams = df.groupby('team_name_2')

    if args.teams and args.students and args.emails:
        print('\n'.join([f'{team}: {list(frame["name"] + " <" + frame["email"] + ">")}'
            for team, frame in teams
        ]))
    elif args.teams and args.students:
        print('\n'.join([f'{team}: {frame.name.to_list()}' for team, frame in teams]))
    elif args.students and args.emails:
        print('\n'.join(sorted(df.name + ' <' + df.email + '>')))
    elif args.teams and args.emails:
        print('\n'.join([f'{team}: {frame.email.to_list()}' for team, frame in teams]))
    elif args.teams:
        print('\n'.join(teams.groups.keys()))
    elif args.students:
        print('\n'.join(sorted(df.name.to_list())))
    elif args.emails:
        print('\n'.join(sorted(df.email.to_list())))
    else:
        print(df)

def main():
    global args
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--teams', default=False, action='store_true', help="print team names")
    ap.add_argument('-s', '--students', default=False, action='store_true', help="print student names")
    ap.add_argument('-e', '--emails', default=False, action='store_true', help="print student emails")
    args = ap.parse_args()
    output(args)


if __name__ == '__main__':
    sys.exit(main())
