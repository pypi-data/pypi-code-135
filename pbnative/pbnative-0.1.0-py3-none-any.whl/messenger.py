#!/usr/bin/env python3

import struct
import os
import sys
import json
import logging

from pbnative.utils import get_firefox_profile_dir_path, plateform_switch


logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "./prettier_bookmarks.log"),
                    encoding='utf-8',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S',
                    level=logging.DEBUG)


# TODO: vérifier les données envoyés
# TODO: renvoyer des messages d'erreurs ou de confirmation après les actions

CURRENT_FILE_PATH = os.path.join(os.path.dirname(__file__))
PB_CSS_PATH = os.path.join(
    get_firefox_profile_dir_path(), "chrome", "prettierBookmarks.css")
ICONS_FOLDER_PATH = os.path.join(CURRENT_FILE_PATH, "icons")


def icon_path(icon): return os.path.join(ICONS_FOLDER_PATH, icon + ".svg")
def icon_path_win(icon): return os.path.join(
    ICONS_FOLDER_PATH, icon + ".svg").replace('\\', '\\\\')


def id_string(id): return f"/* PrettierBookmark bookmarkId=\"{id}\" */"
def label_string(label): return f"[label=\"{label}\"]"
def icon_string(icon): return f"url(\"{icon_path(icon)}\")"
def icon_string_win(icon): return f"url(\"file:///{icon_path_win(icon)}\")"


def folderTemplate(ident: str, title: str, icon: str, color: str):
    linux_temp = f"""
/* PrettierBookmark bookmarkId="{ident}" */
.bookmark-item[container][label="{title}"] {{
    list-style-image: {icon_string(icon)} !important;
}}
.bookmark-item[container][label="{title}"] > .toolbarbutton-icon {{
    fill: {color} !important;
}}
        """

    win_temp = f"""
/* PrettierBookmark bookmarkId="{ident}" */
.bookmark-item[container][label="{title}"] {{
    list-style-image: {icon_string_win(icon)} !important;
}}
.bookmark-item[container][label="{title}"] > .toolbarbutton-icon {{
    fill: {color} !important;
}}
        """

    return plateform_switch(linux_temp, win_temp)


def update_folder(data):
    logging.debug("An update of the file has been requested")
    folder = data["folder"]

    with open(PB_CSS_PATH, "r") as chrome:
        if chrome.closed:
            logging.error("Le fichier useChrome.css n'a pas été trouvé")
        else:
            logging.debug("userChrome.css file ok")

        chromeLines = chrome.readlines()

    hasBookmark = any(id_string(folder["id"]) in line for line in chromeLines)

    if(hasBookmark):
        logging.debug("Bookmark found. It's an update",
                      f"Updating bookmark {folder['id']}")

        bookmarkStart = [index for index, string in enumerate(
            chromeLines) if id_string(folder["id"]) in string][0]

        labelLineIndex = bookmarkStart+1
        labelLine = chromeLines[labelLineIndex]
        secondLabelLineIndex = bookmarkStart+4
        secondLabelLine = chromeLines[secondLabelLineIndex]
        iconLineIndex = bookmarkStart+2
        iconLine = chromeLines[iconLineIndex]
        colorLineIndex = bookmarkStart+5
        colorLine = chromeLines[colorLineIndex]

        # update label
        if(".bookmark-item[container]" in labelLine):
            chromeLines[
                labelLineIndex] = f".bookmark-item[container]{label_string(folder['title'])} {{\n"

        # update second label
        if(".bookmark-item[container]" in secondLabelLine):
            chromeLines[
                secondLabelLineIndex] = f".bookmark-item[container]{label_string(folder['title'])} > .toolbarbutton-icon {{\n"

        # update icon
        if("list-style-image" in iconLine):
            chromeLines[
                iconLineIndex] = f"    list-style-image: {icon_string(folder['icon'])} !important;\n"

        # update color
        if(".fill" in colorLine):
            chromeLines[
                colorLineIndex] = f"    fill: {folder['color']} !important;\n"

    else:
        logging.debug("Bookmark not found. It's a creation")
        tmp = folderTemplate(
            folder["id"], folder["title"], folder["icon"], folder["color"])
        chromeLines.append(tmp)

    with open(PB_CSS_PATH, "w") as file:
        file.writelines(chromeLines)

    logging.debug("Bookmark created/updated")
    send_message(encode_message({"action": "update_folder", "data": "true"}))


def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    logging.debug(f"Message arrived : {message}")
    return json.loads(message)


def get_object():
    raw_length = sys.stdin.buffer.read(4)

    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return message

# Encode a message for transmission, given its content.


def encode_message(message_content):
    encoded_content = json.dumps(message_content).encode("utf-8")
    encoded_length = struct.pack('=I', len(encoded_content))
    # use struct.pack("10s", bytes), to pack a string of the length of 10 characters
    return {'length': encoded_length, 'content': struct.pack(str(len(encoded_content))+"s", encoded_content)}


# Send an encoded message to stdout.
def send_message(encoded_message):
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()


def start():
    logging.debug("Prettier Bookmarks native app running")

    while True:
        message = get_message()

        if message["action"] == "pbnative_ping":
            send_message(encode_message(
                {"action": "pbnative_ping", "data": "true"}))

        elif message["action"] == "update_folder":
            update_folder(message["data"])


if __name__ == "__main__":
    start()
