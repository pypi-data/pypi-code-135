__version__ = "0.1.0"
"""
Created on Oct 06, 2022

@author: gsnyder,Dinesh Ravi

Generate notices report for a given project-version
"""


def main():
    from blackduck.HubRestApi import HubInstance

    import argparse
    import json
    import logging
    import sys
    import time
    import zipfile
    import os
    from importlib_resources import files, as_file

    parser = argparse.ArgumentParser(
        "A program to generate the notices file for a given project-version"
    )
    parser.add_argument("project_name")
    parser.add_argument("version_name")
    parser.add_argument(
        "-f",
        "--file_name_base",
        default="notices_report",
        help="Base file name to write the report data into. If the report format is TEXT a .zip file will be created, otherwise a .json file",
    )
    parser.add_argument(
        "-r",
        "--report_format",
        default="TEXT",
        choices=["JSON", "TEXT", "HTML"],
        help="Report format - choices are TEXT, JSON or HTML",
    )
    parser.add_argument(
        "-c",
        "--include_copyright_info",
        action="store_true",
        help="Set this option to have additional copyright information from the Black Duck KB included in the notices file report.",
    )

    args = parser.parse_args()

    hub = HubInstance()

    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s",
        stream=sys.stderr,
        level=logging.DEBUG,
    )

    class FailedReportDownload(Exception):
        pass

    DOWNLOAD_ERROR_CODES = [
        "{report.main.read.unfinished.report.contents}",
        "{report.main.download.unfinished.report}",
    ]

    def extract_report():
        from pathlib import Path
        import zipfile
        import shutil

        zipname = f"{args.file_name_base}.zip"
        zipDir = Path(zipname).parent
        dirname = ""
        # zipname = ".zip"
        with zipfile.ZipFile(zipname, mode="r") as archive:
            for file in archive.namelist():
                if file.endswith(".txt"):
                    dir_file = file.split("/")
                    dirname = dir_file[0]
                    filename = dir_file[1].replace(
                        "version-license", "Blackduck_Report"
                    )
                    archive.extract(file, zipDir)
                    os.rename(
                        os.path.join(zipDir, file),
                        os.path.join(zipDir, filename),
                    )
        shutil.rmtree(os.path.join(zipDir, dirname))
        os.remove(os.path.join(zipDir, zipname))

    def html_report():
        import json
        from jinja2 import Template
        from jinja2 import Environment, FileSystemLoader

        this_package = __package__
        template_file = "notices-template.html"
        # template = files(this_package).joinpath("notices-template.html")
        # with as_file(template) as file_:
        #     template = Template(file_.read())
        # templates_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = files(this_package)
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template(template_file)

        with open(f"{args.file_name_base}.html", "w+", encoding="utf-8") as fh:
            with open(f"{args.file_name_base}.json", "r") as lj:
                data = json.load(lj)
                fileContent = data["reportContent"][0]["fileContent"]

                fh.write(
                    template.render(
                        componentLicenses=fileContent["componentLicenses"],
                        licenseTexts=fileContent["licenseTexts"],
                        componentCopyrightTexts=fileContent["componentCopyrightTexts"],
                        projectVersion=fileContent["projectVersion"],
                    )
                )
        os.remove(f"{args.file_name_base}.json")

    def download_report(location, file_name_base, retries=10):
        report_id = location.split("/")[-1]

        if not retries:
            raise FailedReportDownload(
                f"Failed to retrieve report {report_id} after multiple retries"
            )

        logging.debug(f"Retrieving generated report from {location}")
        # response = hub.download_report(report_id)
        response, report_format = hub.download_notification_report(location)

        if response.status_code == 200:
            if report_format == "TEXT":
                filename = f"{file_name_base}.zip"
                with open(filename, "wb") as f:
                    f.write(response.content)
            else:
                # JSON format
                filename = f"{file_name_base}.json"
                with open(filename, "w") as f:
                    json.dump(response.json(), f, indent=3)
            logging.info(
                f"Successfully downloaded json file to {filename} for report {report_id}"
            )

        elif (
            response.status_code == 412
            and response.json()["errorCode"] in DOWNLOAD_ERROR_CODES
        ):
            # failed to download, and report generation still in progress, wait and try again infinitely
            # TODO: is it possible for things to get stuck in this forever?
            logging.warning(
                f"Failed to retrieve report {report_id} for reason {response.json()['errorCode']}.  Waiting 5 seconds then trying infinitely"
            )
            time.sleep(5)
            download_report(location, file_name_base, retries)
        else:
            logging.warning(
                f"Failed to retrieve report, status code {response.status_code}"
            )
            logging.warning(
                f"Probably not ready yet, waiting 5 seconds then retrying (remaining retries={retries}"
            )

            time.sleep(5)
            retries -= 1
            download_report(location, file_name_base, retries)

    if project := hub.get_project_by_name(args.project_name):
        version = hub.get_version_by_name(project, args.version_name)
        html_json = "JSON" if args.report_format == "HTML" else args.report_format
        response = hub.create_version_notices_report(
            version, html_json, include_copyright_info=args.include_copyright_info
        )

        if response.status_code == 201:
            logging.info(
                f"Successfully created notices report in {html_json} format for project {args.project_name} and version {args.version_name}"
            )

            location = response.headers["Location"]
            download_report(location, args.file_name_base)

            if args.report_format == "TEXT":
                extract_report()
            if args.report_format == "HTML":
                html_report()

            # Showing how you can interact with the downloaded zip and where to find the
            # output content. Uncomment the lines below to see how it works.

            # with zipfile.ZipFile(zip_file_name_base, 'r') as zipf:
            #   with zipf.open("{}/{}/version-license.txt".format(args.project_name, args.version_name), "r") as license_file:
            #       print(license_file.read())
        else:
            logging.error(
                f"Failed to create reports for project {args.project_name} version {args.version_name}, status code returned {response.status_code}"
            )

    else:
        logging.warning(f"Did not find project with name {args.project_name}")


if __name__ == "__main__":
    main()
