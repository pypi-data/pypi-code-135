"""# Location data setup module.

Module contains the following functions:

    insert_default_data
    copy_files_from_directory
    location_data_setup
    location_data_cleanup
    download_location_data_file
    extract_location_data_file
    split_location_data_file

"""
import os
import shutil
import zipfile

import requests
import tqdm
import importlib

def insert_default_data(dir_path: str) -> None:
    """Insert default data.

    Inserts default data files into the data folder by copying files
    from the packages data file.

    Args:
        dir_path (str): String path to the project directory.

    """
    with importlib.resources.path("qub-amphibian-report-generator", "data") as data_path:

        # datapath = os.path.join(os.cwd(), "data")   
        old_image_path = os.path.join(data_path, "images")
        old_font_path = os.path.join(data_path, "fonts")
        old_locations_path = os.path.join(data_path, "location")

        new_image_path = os.path.join(dir_path, "data", "images")
        new_fonts_path = os.path.join(dir_path, "data", "fonts")
        new_locations_path = os.path.join(dir_path, "data", "locations")

        copy_files_from_directory(old_image_path, new_image_path)
        copy_files_from_directory(old_font_path, new_fonts_path)
        copy_files_from_directory(old_locations_path, new_locations_path)

        location_data_setup(new_locations_path)


def copy_files_from_directory(old_directory: str, new_directory: str) -> None:
    """Copy a file."""
    shutil.copytree(old_directory, new_directory)


def location_data_setup(new_locations_path: str) -> None:
    """Location Data Setup."""
    download_location_data_file(new_locations_path)

    locations_data_file_path = os.path.join(new_locations_path, "all_countries.zip")
    # locations_data_file_path = os.path.join("/", "home", "cush","a","data", "locations", "csv_files", "all_countries.zip")

    extract_location_data_file(new_locations_path, locations_data_file_path)
    split_location_data_file(new_locations_path)
    location_data_cleanup(new_locations_path, locations_data_file_path)


def location_data_cleanup(locations_path, locations_data_file_path):
    """Cleanup unneeded location data."""
    print("Cleaning up data.")
    zip_path = locations_data_file_path
    txt_path = os.path.join(locations_path, "allCountries.txt")

    os.remove(zip_path)
    os.remove(txt_path)
    print("Clean up complete.")


def download_location_data_file(location_dir: str) -> None:
    """Download location data files.

    Download location data file from the geocodes website.
    """
    print("Downloading location data file")
    location_file_url = "https://download.geonames.org/export/dump/allCountries.zip"
    with requests.get(location_file_url, stream=True) as response:

        file_path = os.path.join(location_dir, "all_countries.zip")
        response.raise_for_status()
        with open(file_path, "wb") as file:
            progress_bar = tqdm.tqdm(total=int(response.headers["Content-Length"]))
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                progress_bar.update(len(chunk))


def extract_location_data_file(
    new_locations_path: str, location_data_zip_path: str
) -> None:
    """Extract location data."""
    print("Unzipping Locations Data File:")
    # old_zip_path = os.path.join(
    #     os.getcwd(), "data", "location", "csv_files", "all_countries.zip"
    # )
    # shutil.copy(old_zip_path, new_locations_path)

    with zipfile.ZipFile(location_data_zip_path) as zipf:
        for member in tqdm.tqdm(zipf.infolist(), desc="Extracting"):
            zipf.extract(member, new_locations_path)


def split_location_data_file(locations_path: str) -> None:
    """Split location data into smaller files."""
    # Csv header
    file_header = "geoname_id\tplace_name\tascii_name\talternate_names\tlatitude"
    file_header += (
        "\tlongitude\tfeature_class\tfeature_code\tcountry_code\tcc2\tadmin1_code"
    )
    file_header += (
        "\tadmin2_code\tadmin3_code\tadmin4_code\tpopulation_info\televation\tdem"
    )
    file_header += "\ttimezone\tmodification\n"

    # Lines for each split file
    lines_per_file = 5000

    file_location = os.path.join(locations_path, "allCountries.txt")

    print("Splitting csv into chunks:")
    os.makedirs(os.path.join(locations_path, "csv_files", "split_csv"))
    smallfile = None
    with open(file_location, "r") as big_file:
        progress_bar = tqdm.tqdm(total=os.path.getsize(file_location), desc="Splitting")
        for lineno, line in enumerate(big_file):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = f"small_csv_file_{lineno + lines_per_file}.csv"
                small_filepath = os.path.join(
                    locations_path, "csv_files", "split_csv", small_filename
                )
                smallfile = open(small_filepath, "a")
                smallfile.write(file_header)
            smallfile.write(line)
            progress_bar.update(len(line))
        if smallfile:
            smallfile.close()
