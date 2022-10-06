"""Manage and load font choices.

"""
import os

import yaml

from report_generator.config import dump_config, load_config


def font_dict_loader() -> dict:
    """Load fonts from yaml file.

    Show dict of font-name, font-location pairings
    based on yaml file in projects data/fonts directory.

    Returns:
        font-dict (dict): dict of font-name, font-file-path str
                          values. Used to select font choices or
                          to add font to pdf.
    """
    fonts = {}
    config = load_config()
    font_path = os.path.join(config["dir_path"], "data", "fonts")
    font_yaml = os.path.join(font_path, "fonts.yaml")

    with open(font_yaml, "r") as file:
        fonts = yaml.load(file, Loader=yaml.loader.SafeLoader)

    return fonts


def font_selection_updater(chosen_fonts: dict) -> None:
    """Update config.yaml with default font selection.

    Takes a dict of chosen fonts and updates the config.yaml
    with the selection. Fonts included for:
        - Title Font, colour, font-size
        - Paragraph Font, colour, font-size
        - Heading Font, colour, font-size

    Args:
        chosen_fonts (dict): Dict

    """
    config = load_config()
    dump_config(config)


def add_font_choices_to_pdf(pdf: object, font_options: dict) -> object:
    """Add font to choices to pdf.

    Takes PDF instance and checks if the selected fonts are
    default fonts to FPDF2. If they are not default it takes the font location from the fonts.yaml file and adds the
    font under its name to the pdf.

    Args:
        pdf ()              - FPDF2 PDF class instantiation.
        font_options (dict) - Selected fonts and settings
    """
    config = load_config()

    config["fonts"]
    font_dict = font_dict_loader()

    for font_name, font_val in font_dict["font_types"].items():
        if font_val is not True:
            print(font_name, font_val)
            font_path = os.path.join(config["dir_path"], "data", "fonts")
            font_loc = os.path.join(font_path, font_val)
            pdf.add_font(font_name, "", font_loc)

    font_path = os.path.join(config["dir_path"], "data", "fonts")
    font_loc = os.path.join(font_path, "OpenSans-Bold.ttf")
    pdf.add_font("OpenSans", "b", font_loc)

    # if (font_options is None):
    #     header_font = config['fonts']['default_header_font']
    #     title_font = config['fonts']['default_title_font']
    #     title_sub_font = config['fonts']['default_title_sub']
    #     paragraph_font = config['fonts']['default_paragraph_font']

    #     fonts = [header_font, title_font, title_sub_font,paragraph_font]
    #     font_path = os.path.join(config['dir_path'], "data", "fonts")

    #     for font in fonts:
    #         if not check_if_default_font(font):
    #             font_location = os.path.join(
    #                 font_path,
    #                 font_dict['font_types'][font]
    #             )
    #             pdf.add_font(font,"", font_location)
    # else:
    #     header_font = font_options['header_font']
    #     title_font = font_options['title_font']
    #     paragraph_font = font_options['paragraph_font']

    #     fonts = [header_font, title_font, paragraph_font]
    #     font_path = os.path.join(config['dir_path'], "data", "fonts")

    #     for font in fonts:
    #         if not check_if_default_font(font):
    #             font_location = os.path.join(
    #                 font_path,
    #                 font_dict["font_types"][font]
    #             )
    #             pdf.add_font(font,"", font_location)
    return pdf


def check_if_default_font(font_name: str) -> bool:
    """Check if choice is a default font.

    Checks if the font_name passed into method is on
    the list of the 14 default fonts built into the
    PDF engine.

    Args:
        font_name (str) - The name of the font to be
                          checked.

    Returns:
        bool            - Whether the font is a default
                          font or not.
    """

    fonts_dict = font_dict_loader()

    if fonts_dict["font_types"][font_name] is True:
        return True
    else:
        return False
