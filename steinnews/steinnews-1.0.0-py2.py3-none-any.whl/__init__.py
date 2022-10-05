import re
from typing import Tuple, List
import logging

MAJOR = "* Major:"
MINOR = "* Minor:"
PATCH = "* Patch:"
AVAILABLE_LEVELS = [MAJOR, MINOR, PATCH]


VERSION_PATTERN = r"""
    \d+ # Digit (Major) positive number o fimes
    \.  # literal .
    \d+ # Digit (Minor version number)
    \.  # literal .
    \d+ # Digit (Patch version number)
    \n  # newline
    -+"""

CHANGE_LEVEL = r"""
    \*                  # Assert a literal *
    [                   # Create a character class
        \s                 # Assert a whitespace character
        \w                 # Assert a word character
    ]+                  # Close the character class and repeat it one or more times
    :                   # Assert a literal :
    """

CHANGE_PATTERN = rf"""
    ^                       # Assert start of string
    (                       # Capture group 1
        {CHANGE_LEVEL}          # Check the change level pattern
    )                       # End of capture group 1

    (                       # Capture group 2
        [\s\S]*?                # Match any character 0 or more times, non-greedy - "Do not iterate any more than is absolutely necessary"
        (?=                     # Positive lookahead
            ^{CHANGE_LEVEL}          # Check the change level pattern
            |                       # OR
            \Z                      # Assert end of string
        )                       # End of positive lookahead
    )                       # End of capture group 2
    """


# file_in and file_out may be the same
def write_next_version(file_in, file_out):
    # Read in the file
    with open(file_in, "r") as file:
        content = file.read()
    output = generate_next_version(content)

    # Write the file out again
    with open(file_out, "w") as file:
        file.write(output)


def generate_next_version(content):
    # Split the file on the first(most recent) version header
    sections_result = re.split(
        VERSION_PATTERN, content, flags=re.MULTILINE | re.VERBOSE
    )
    latest_section = sections_result[0]  # if sections_result else content
    latest_changes: List[Tuple] = re.findall(
        CHANGE_PATTERN, latest_section, re.VERBOSE | re.MULTILINE
    )

    valid_content, highest_level_seen = validate_content(latest_changes, content)

    old_version_result = re.findall(
        r"(\d+)\.(\d+)\.(\d+)\n-+", valid_content, flags=re.M
    )
    old_version = old_version_result[0] if old_version_result else ("0") * 3

    # bump version
    version = {
        MAJOR: old_version[0],
        MINOR: old_version[1],
        PATCH: old_version[2],
    }
    logging.debug(f"Old version: {version}")

    found = False
    for key in AVAILABLE_LEVELS:
        if found:
            # making sure to set lower tier version numbers to zero
            version[key] = "0"
        if key == highest_level_seen:
            version[key] = str(int(version[key]) + 1)
            found = True

    new_version_str = version[MAJOR] + "." + version[MINOR] + "." + version[PATCH]
    logging.debug("New version: %s", new_version_str)
    # Replace in the target text to write new version

    new_version_underscores = "-" * len(new_version_str)

    # Replace in the target text to write new version
    res = re.sub(
        r"(Latest\n-+\n)",
        r"\1* tbd\n\n" + new_version_str + "\n" + new_version_underscores + "\n",
        valid_content,
        flags=re.M,
    )
    return res


def validate_content(latest_changes: List[Tuple], content: str):
    """
    1. Filter latest changes are in the correct format
    2. Replace the orignal changes with the filtered ones in content
    3. Return the content and the highest level seen
    """

    def changes_to_str(changes: List[Tuple[str, str]]) -> str:
        changes_string = ""
        for change_level, text in changes:
            changes_string += change_level + text
        return changes_string

    seen_level_dict = {
        MAJOR: False,
        MINOR: False,
        PATCH: False,
    }
    valid_changes: List[Tuple] = []

    for change_level, text in latest_changes:
        if change_level not in AVAILABLE_LEVELS:
            logging.warning(
                "Invalid change level: %s with text:"
                "%sList of available change levels {AVAILABLE_LEVELS}",
                change_level,
                text,
            )
        else:
            seen_level_dict[change_level] = True
            valid_changes.append((change_level, text))

    highest_level_seen = (
        MAJOR
        if seen_level_dict[MAJOR]
        else MINOR
        if seen_level_dict[MINOR]
        else PATCH
        if seen_level_dict[PATCH]
        else None
    )
    if highest_level_seen is None:
        raise Exception("No changes found in latest section")

    # The last two characters of the changes should be newlines, one for the last bullet point and one for the version header
    # If validation removed the last change, we got rid of the newline, so we need to add it back
    valid_changes_str = changes_to_str(valid_changes)
    if valid_changes_str[-2] != "\n":
        valid_changes_str += "\n"

    changes_str = changes_to_str(latest_changes)
    valid_content = re.sub(re.escape(changes_str), valid_changes_str, content)

    logging.debug("########Old list of changes#########\n%s", changes_str)
    logging.debug("########New list of changes#########\n%s", valid_changes_str)
    logging.debug("########Validated content#########\n%s", valid_content)

    return valid_content, highest_level_seen
