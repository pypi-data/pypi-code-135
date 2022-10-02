#!/usr/bin/python3
"""
 Created on Sept. 12, 2022
"""
__version__ = '0.0.1'

# Standard library imports
import sys

# Third party imports
import requests
import json
import csv
import gpxpy.gpx as my_gpx  # type: ignore
from typing import Dict, Generator, List

# Local application imports
import constants  # type: ignore

csv_file_name: str = 'Coast Capital ATMs.csv'
gpx_file_name: str = 'Coast Capital ATMs.gpx'


def get_page_jdom(base_url: str, header: Dict, databits: Dict) -> List:
    """Retrieve web page information using post method (& extra info).
    :param base_url: url of the website that has the info
    :param header: details of the HTML header we send
    :param databits: the stuff that goes in the post
    :return: JSON data
    """
    try:
        r = requests.post(base_url, headers=header, json=databits, timeout=5)
    except requests.exceptions.ConnectionError as err:
        print(f"I got this strange error and I'm giving up: {err}")
        sys.exit()
    except requests.exceptions.ReadTimeout as err:
        print(f"Timed out trying to get data: {err}")
        sys.exit()
    else:
        if r.ok:
            try:
                result_json = r.json()
            except json.decoder.JSONDecodeError as err:
                print(f"I received something that wasn't JSON so I'm giving up: {err}")
                sys.exit()
            else:
                return result_json
        else:
            print(f"I got a bad return code, not OK: {r}")
            sys.exit()


def gather_details(line: Dict) -> str:
    """Combine several items to create a single one.
    :param line: dictionary of one site to check
    :return: string containing specific information we want
    """
    it = [line[k]
          for k in constants.DETAIL_KEYS if k in line if line[k] is not None]
    return ', '.join(it)


def item_generator(full_dict: List) -> Generator:
    """Get data of interest.
    :param full_dict: dictionary of all the sites
    """
    for i in full_dict:
        if i['AcceptsDeposits'] is not None:
            yield i['Latitude'], i['Longitude'], i['Owner'].title(), gather_details(i)


def main():
    data = get_page_jdom(constants.BASE_URL, constants.HEADER,
                         constants.DATABITS)  # call the post function
    gpx = my_gpx.GPX()
    line_count = 0
    with open(csv_file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        gen = item_generator(data)
        for item in gen:
            csv_writer.writerow(item)
            gpx.waypoints.append(my_gpx.GPXWaypoint(latitude=item[0],
                                                    longitude=item[1],
                                                    name=item[2],
                                                    description=item[3]))
            line_count += 1
    with open(gpx_file_name, 'w') as gpx_file:
        gpx_file.write(gpx.to_xml())
    print(f"I extracted {line_count} of {len(data)} items and I'm All Done!")


if __name__ == '__main__':
    main()
