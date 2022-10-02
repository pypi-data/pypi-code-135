# Run dependency injections
import os
import tekleo_common_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(tekleo_common_utils.__file__)))
import concurrent.futures
from itertools import repeat
import multiprocessing
import argparse
import traceback
from colorama import Fore, Style
from tekleo_common_utils import UtilsImage


utils_image = UtilsImage()
number_of_cpu = multiprocessing.cpu_count()


def convert_file(source_folder_path: str, source_file_name: str, source_format: str, target_format: str, target_quality: int, target_overwrite: bool) -> bool:
    # Build two file paths
    source_file_path = source_folder_path + "/" + source_file_name
    target_file_path = source_folder_path + "/" + source_file_name[0:-1 * len(source_format)] + target_format

    # If we have a source path
    if os.path.exists(source_file_path):
        # If the target path is available
        if not os.path.exists(target_file_path):
            # Open image and save it in a new format
            image_pil = utils_image.open_image_pil(source_file_path)
            image_pil = utils_image.clear_exif_data(image_pil)
            utils_image.save_image_pil(image_pil, target_file_path, quality=target_quality)
            print(Fore.GREEN + 'SUCCESS!' + Style.RESET_ALL + ' Converted image from "' + source_file_path + '" to "' + target_file_path + '"')
            return True

        # If we already have a file at target path
        else:
            # If overwrite flag is enabled
            if target_overwrite:
                # Delete old file
                print(Fore.YELLOW + 'WARNING!' + Style.RESET_ALL + ' File already exists at "' + target_file_path + '" and we will overwrite it')
                os.remove(target_file_path)

                # Open image and save it in a new format
                image_pil = utils_image.open_image_pil(source_file_path)
                image_pil = utils_image.clear_exif_data(image_pil)
                utils_image.save_image_pil(image_pil, target_file_path, quality=target_quality)
                print(Fore.GREEN + 'SUCCESS!' + Style.RESET_ALL + ' Converted image from "' + source_file_path + '" to "' + target_file_path + '"')
                return True

            # If we can't overwrite
            else:
                print(Fore.YELLOW + 'WARNING!' + Style.RESET_ALL + ' File already exists at "' + target_file_path + '" and we don\'t want to accidentally overwrite it, skipping this file')
                return False

    # If we don't have a source path
    else:
        print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' File doesn\'t exists at "' + source_file_path + '" skipping this file')
        return False


def main():
    # Pars all CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('formatSource', metavar='S', type=str, nargs='?', choices=["jpg", "jpeg", "png", "heic"], help='images of which format should be converted')
    parser.add_argument('formatTarget', metavar='T', type=str, nargs='?', choices=["jpg", "jpeg", "png"], help='to what format we need to convert them')
    parser.add_argument('-o', metavar='o', type=str, nargs='?', choices=["y", "n", "Y", "N"], default="n", help='Y/N should we overwrite files (if they already exist), optional and defaults to N')
    parser.add_argument('-q', metavar='q', type=int, nargs='?', choices=list(range(0, 101)), default=100, help='converted image quality parameter, from 0 to 100, optional and defaults to 100, but common value for JPG is 90')
    args = parser.parse_args()
    input_source_format = args.formatSource
    input_target_format = args.formatTarget
    input_target_quality = args.q
    input_target_overwrite = str(args.o).lower().strip() == "y"
    cwd_path = os.getcwd()
    print(Fore.YELLOW + "INFO!" + Style.RESET_ALL + " number_of_cpu=" + str(number_of_cpu) + ", input_format_source=" + str(input_source_format) + ", input_format_target=" + str(input_target_format) + ", input_quality=" + str(input_target_quality) + ", input_overwrite=" + str(input_target_overwrite) + ", cwd_path=" + str(cwd_path))

    # Find files that match input format
    file_names_in_cwd = os.listdir(cwd_path)
    file_names_matched_source_format_in_cwd = [f for f in file_names_in_cwd if f.lower().endswith("." + input_source_format)]

    # If we actually have some files
    if len(file_names_matched_source_format_in_cwd) > 0:
        print(Fore.YELLOW + "INFO!" + Style.RESET_ALL + " Started conversion")
        # Convert files in parallel
        results = []
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=number_of_cpu)
        for result in executor.map(convert_file, repeat(cwd_path), file_names_matched_source_format_in_cwd, repeat(input_source_format), repeat(input_target_format), repeat(input_target_quality), repeat(input_target_overwrite)):
            results.append(result)
        print(Fore.YELLOW + "INFO!" + Style.RESET_ALL + " Finished conversion")
    print(Fore.YELLOW + "INFO!" + Style.RESET_ALL + " Exiting...")
    exit(0)


if __name__ == "__main__":
    main()
