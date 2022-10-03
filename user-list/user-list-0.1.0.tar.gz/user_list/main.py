#!/usr/bin/env python
import argparse
import csv
import json
import pandas as pd
import os
import requests



def cxn(url):
    """Function to load the url and request data/"""
    response = requests.get(url)
    r = json.loads(response.text)
    return r


# def csv_file(r):
#     header = []
#     data = []
#
#     print(len(r["data"]))
#
#     for users in r["data"]:
#         for key, value in users.items():
#             if key in header:
#                 pass
#             else:
#                 header.append(key)
#
#     with open('users.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=header)
#         writer.writeheader()
#         writer.writerows(r["data"])

def csv_file(r):
    """
    Function that will convert the data from the previous one (cxn) to a CSV file.
    """
    header = []
    data = []

    # print(len(r["data"]))

    for users in r["data"]:
        for key, value in users.items():
            if key in header:
                pass
            else:
                header.append(key)

    # with open('users.csv', 'w', encoding='UTF8', newline='') as f:
    f = open('users.csv', 'w', encoding='UTF8', newline='')
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(r["data"])
    # print(f"The Data is exported to: {f.name}")
    return f.name


def html_file():
    """
    Function that will convert the data from the previous one (csv_file) to a HTML file.
    """
    df = pd.read_csv('users.csv')
    print(df)
    f = open('users.html', 'w')
    result = df.to_html()
    f.write(result)
    f.close()
    return f.name


def clean():
    """
    Clean the csv file.
    """
    if os.path.exists("users.csv"):
        os.remove("users.csv")
    else:
        pass


def main():
    """Simple program that get data from an url and export to csv or html"""
    data = cxn(url="https://reqres.in/api/users")
    parser = argparse.ArgumentParser(description='Simple program that get data from an url and export to csv or html')

    # Optional argument
    parser.add_argument('--csv', type=bool, nargs='?',
                        help='Export to CSV file')
    parser.add_argument('--html', type=bool, nargs='?',
                        help='Export to HTML file')

    args = parser.parse_args()

    if args.csv:
        # csv_file(data)
        print(f"The Data is exported to: {csv_file(data)}")
    elif args.html:
        csv_file(data)
        # html_file()
        print(f"The Data is exported to: {html_file()}")

        clean()
    elif args.csv and args.html:
        print(f"The Data is exported to: {csv_file(data)}")
        print(f"The Data is exported to: {html_file()}")
        # csv_file(data)
        # html_file()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
