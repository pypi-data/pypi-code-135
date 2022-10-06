"""# Clean Data.

Script to clean data from dataset and create new excel sheet with data.

Can be ran from command line.

        python3 clean_data.py {input_file} {output_file}

Or import clean_data function.

        from clean_data import clean_data

This module contains the following functions:


"""

import os
import re
import sys

import pandas

import report_generator.config


def create_data_frame(path_to_dataset: str) -> object:
    """## Create data frame.

    Loads excel file and returns Pandas DataFrame obj

    Args:
        path_to_data_set (str): file path string

    Returns:
        data_frame (object): Pandas DataFrame object

    """
    data_frame = None
    try:
        data_frame = pandas.read_excel(path_to_dataset)

    except FileNotFoundError as e:
        print("Failed to open excel file")
        print(e)

    return data_frame


def clean_data(data_frame: object) -> object:
    """## Clean data.

    Takes data_frame object and cleans data by using 'applymap' to apply a lamda
    function to all DataFrame values.

    1st Lambda function converts values to strings, replaces instances of ND with
    empty string, and strips whitespace and quotation marks.

    2nd Lambda function converts values that should be numeric back to numeric
    values.

    Args:
        data_frame (object): Pandas DataFrame object

    Returns:
        clean_data_frame (object) Pandas DataFrame object

    """
    clean_data_frame = data_frame.applymap(
        lambda x: re.sub("ND", "", str(x)).strip().strip('"'), na_action="ignore"
    )
    clean_data_frame = clean_data_frame.applymap(
        lambda x: pandas.to_numeric(x, errors="coerce")
        if str(x).replace(".", "").isdigit()
        else x
    )
    clean_data_frame = clean_data_frame.applymap(lambda x: None if x == "" else x)
    clean_data_frame = remove_duplicates(clean_data_frame)

    return clean_data_frame


def remove_duplicates(data_frame: object) -> object:
    """## Remove duplicates from data.

    Takes a data_frame object and looks for duplicate name combination entries
    and removes the row from the dataset and puts it into a separate file.

    Args:
        data_frame (object): Pandas Dataframe object

    Returns
        clear_data_frame (object): Cleaned Dataframe for duplicates
    """
    print("****************************************")
    print(f"Searching Duplicates: Current Row Count={len(data_frame.index)}")
    dups = data_frame[
        data_frame.duplicated(["Order", "Family", "Genus", "Species"], keep=False)
    ]
    print(len(data_frame.index))
    print(dups)
    settings = report_generator.config.load_config()
    dir_path = settings["dir_path"]
    duplicate_path = os.path.join(dir_path, "data", "duplicates", "duplicates.xlsx")
    print(f"Saving duplicates to duplicates file: {duplicate_path}")
    print()
    dups.to_excel(duplicate_path)

    print("Removing Duplicates")

    dups = data_frame[
        data_frame.duplicated(["Order", "Family", "Genus", "Species"], keep="first")
    ]
    print(dups)
    data_frame = data_frame.drop_duplicates(
        subset=["Order", "Family", "Genus", "Species"], keep="first"
    )
    print(f"Removed Duplicates: Current Row Count={len(data_frame.index)}")
    print("***************************************")
    return data_frame


def main(input_file_name: str, output_file_name: str) -> None:
    """## Clean data main.

    Takes input_file_name and output_file_name.
    Loads data from input_file
    Cleans data
    Saves as output_file

    Args:
        input_file_name (str): The input file name string
        output_file_name (str): The output file name string

    """
    # Get filepaths
    cur_dir = os.getcwd()
    path_to_dataset = os.path.join(cur_dir, input_file_name)
    path_to_output_file = os.path.join(cur_dir, output_file_name)

    # load df
    try:
        data_frame = create_data_frame(path_to_dataset)
        # print(data_frame["RangeSize"].head(5))

        # clean df
        clean_data_frame = clean_data(data_frame)
        # print(clean_data_frame["RangeSize"].head())

        # output to new file
        clean_data_frame.to_excel(path_to_output_file, index=False)

    except FileExistsError as e:
        print(e)


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        print("Not enough args")

    else:
        main(args[1], args[2])
