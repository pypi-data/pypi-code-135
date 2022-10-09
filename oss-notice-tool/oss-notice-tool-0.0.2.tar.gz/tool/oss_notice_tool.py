# tools/oss_notice_tool.py
# SPDX-FileCopyrightText: Copyright 2022 SK TELECOM CO., LTD. <haksung@sk.com>
# SPDX-License-Identifier: Apache-2.0

import click
from parsing.parse import parse_file
from generating.generate import generate_notice

# override the help option so that you can also see help with -h
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# create a group, cli
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Genearte Open Source Software Notice based on the SPDX document. 
    """
    pass

@click.command(help="This creates an OSS Notice file based don the excel format SPDX document.")
@click.argument('infile')
@click.option('-l', '--html_format', is_flag=True, help="Create a html format OSS notice")
@click.option('-t', '--text_format', is_flag=True, help="Create a text format OSS notice")
def create(infile, html_format, text_format):
    """
    This creates the packages of the spdx document as oss notice.

    Params
    ----------
    infile: str
        excel format spdx document file name
    html_format: bool
        if True, only create html format oss notice
    text_format: bool
        if True, only create text format oss notice
    """
    print("debug: " + 'called create')
    print("debug: " + infile)
    print("debug: " + str(html_format))
    print("debug: " + str(text_format))

    # parse excel file
    doc = parse_file(infile)

    # generate html format oss notice
    if html_format is False and text_format is True:
        raise NotImplementedError("Text format is not supported yet.")  
    else:
        generate_notice(doc, 'html')

def main():
    cli.add_command(create)
    cli()

if __name__ == "__main__":
    main()