import csv

import warnings

warnings.filterwarnings('ignore')


def csv_txt(csv_file, txt_file):
    text_list = []

    with open(csv_file, "r") as my_input_file:
        for line in my_input_file:
            line = line.split(",", 2)
            text_list.append(" ".join(line))

    with open(txt_file, "w") as my_output_file:
        my_output_file.write("#1\n")
        my_output_file.write("double({},{})\n".format(len(text_list), 2))
        for line in text_list:
            my_output_file.write("  " + line)
        print("Successfully converted csvfile to txtfile!.")


def txt_csv(txtfile, csvfile):
    with open(txtfile, 'r') as infile, open(csvfile, 'w') as outfile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        writer = csv.writer(outfile)
        writer.writerows(lines)
        print("Successfully converted txtfile to csvfile!")
