import os
import json
import sys
import shutil
import platform
from pathlib import Path

from pbnative.utils import colorize, get_firefox_profile_dir_path, get_mozilla_path, get_resources_path, plateform_switch
from . import __version__

if platform.system() == "Windows":
    import winreg


OS_PLATFORM = platform.system()
CURRENT_FILE_PATH = os.path.join(os.path.dirname(__file__))
NATIVE_MANIFEST = {
    "name": "prettier_bookmarks",
    "description": "Prettier Bookmarks Native App",
    "path": "__PATH_TO_THE_NATIVE_APP_LAUNCHER__",
    "type": "stdio",
    "allowed_extensions": [
        "prettier_bookmarks@keops.me"
    ]
}
MANIFEST_NAME = "prettier_bookmarks.json"


def make_manifest():
    linux_manifest_path = [Path.home(), ".local", "bin", "pbnative-start"]
    win_manifest_path = [os.path.dirname(
        sys.executable), "Scripts", "pbnative-start.exe"]

    manifest = NATIVE_MANIFEST
    manifest_path_tuple = plateform_switch(
        linux_manifest_path, win_manifest_path)
    manifest["path"] = os.path.join(*manifest_path_tuple)

    return manifest


def create_manifest_win_registry_key(manifest_path):
    print("Creating Windows registry key", end=" ")
    try:
        pbnative_key = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER, r"SOFTWARE\Mozilla\NativeMessagingHosts\pbnative")
        winreg.SetValue(pbnative_key, "",
                        winreg.REG_SZ, manifest_path)
        pbnative_key.Close()
        print(colorize("Ok !", color="GREEN"))
    except OSError:
        print(colorize(
            "Error: La clé n'a pas pu être ajoutée au registre Windows."), color="RED")
    except:
        print(colorize(
            "Error: Les clés n'ont pas pu être ajouté au registre Windows.", color="RED"))


def install_native_manifest():
    print("Installing manifest...", end=" ")
    manifest = make_manifest()

    if OS_PLATFORM == "Linux":
        manifest_dir_path = os.path.join(
            get_mozilla_path(), "native-messaging-hosts")

    elif OS_PLATFORM == "Windows":
        manifest_dir_path = os.path.dirname(__file__)
        # windows need to have manifest path in a registry key
        create_manifest_win_registry_key(
            os.path.join(manifest_dir_path, MANIFEST_NAME))
    else:
        sys.exit("Unmanaged OS")

    with open(os.path.join(manifest_dir_path, MANIFEST_NAME), "w") as manifest_file:
        json.dump(manifest, manifest_file, indent=4)

    print(colorize("Manifest installed !", color="GREEN"))


def make_chrome_directory():
    print("Creating chrome directory in your firefox's profile folder", end=" ")
    profile_path = get_firefox_profile_dir_path()
    chrome_path = os.path.join(profile_path, "chrome")

    if not(os.path.isdir(chrome_path)):
        os.mkdir(chrome_path)
        print(colorize("Ok !", color="GREEN"))
    else:
        print("Chrome directory exist, next.")


# crée le fichier userChrome.css s'il n'existe pas
# crée un fichier prettierBookmarks.css qui servira pour les regles de l'appli
# ajoute un import dans le fichier userChrome.css pointant vers prettierBookmarks.css
def install_userchrome_css():
    print("Installing userChrome.css and prettierBookmarks.css file...", end=" ")
    profile_path = get_firefox_profile_dir_path()
    chrome_path = os.path.join(profile_path, "chrome")
    userchrome_path = os.path.join(chrome_path, "userChrome.css")
    pb_css_path = os.path.join(chrome_path, "prettierBookmarks.css")
    userchrome_css_template_path = os.path.join(os.path.dirname(
        __file__), 'resources', 'userChrome.css')
    import_line = f"@import 'prettierBookmarks.css';\n"

    if not(os.path.isfile(pb_css_path)):
        with open(pb_css_path, "w") as pb_css_file:
            pb_css_file.write("")

    with open(userchrome_path, "w+") as userchrome_file:
        lines = userchrome_file.readlines()

        if not lines:
            with open(userchrome_css_template_path, "r") as userchrome_css_template_file:
                template = userchrome_css_template_file.read()
                lines.append(template)

        if not any(import_line in line for line in lines):
            userchrome_file.seek(0)
            lines.insert(0, import_line)
            userchrome_file.writelines(lines)
    print(colorize("Ok !", color="GREEN"))


def install_user_js():
    print("Installing user.js file... ", end=" ")

    user_js_path = os.path.join(get_firefox_profile_dir_path(), "user.js")

    stylesheet_line = f"user_pref('toolkit.legacyUserProfileCustomizations.stylesheets', true);\n"
    svg_context_line = f"user_pref('svg.context-properties.content.enabled', true);\n"

    if not (os.path.isfile(user_js_path)):
        shutil.copy(os.path.join(
            get_resources_path(), 'user.js'), user_js_path)
    else:
        with open(user_js_path, "r+") as user_js_file:
            lines = user_js_file.readlines()

            lines_loop = (line for line in lines)

            if not stylesheet_line in lines_loop:
                user_js_file.write(stylesheet_line)
            if not svg_context_line in lines_loop:
                user_js_file.write(svg_context_line)

    print(colorize("Ok !", color="GREEN"))


def start():
    print("Prettier Bookmarks")
    print("Version " + __version__.version + "\n")
    print("Hey it's Keops ! Thanks to use Prettier Bookmarks. Hope you like the extension.")
    print("Feel free to send me your comments or suggest improvements ! ;)\n")
    print(("-" * 20) + "\n")
    print("Installation start\n")
    install_native_manifest()
    make_chrome_directory()
    install_userchrome_css()
    install_user_js()

    print("Prettier Bookmarks ", colorize("setup completed !", color="GREEN"))


if __name__ == "__main__":
    start()
