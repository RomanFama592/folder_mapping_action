"""This module contains functions for mapping and formatting directory structures."""
from pathlib import Path
from gitignore_parser import parse_gitignore
from src.short_folders import list_and_short_files

CHARACTERS = {
    "init": "/",
    "end_init": "",
    "isFolder": "",
    "end_isFolder": "/",
    "verticalLine": "│",
    "TLine": "├── ",
    "end_TLine": "",
    "LLine": "└── ",
    "end_LLine": "",
    "indent": "     ",
    "end_indent": "\n",
}


def return_false(
    x,
):  # pylint: disable=unused-argument disable=missing-function-docstring
    return False


def map_folders(
    directory_path: Path, indent: str = "", is_ignored=return_false, characters=None
) -> str:
    # pylint: disable=line-too-long
    """
    Recursively maps the folder structure of the given directory, ignoring files and folders specified in a `.gitignore` file.

    Args:
        directory_path (Path): The path to the directory to be mapped.
        indent (str, optional): The indentation string used for formatting the folder structure. Default is an empty string.
        is_ignored (function, optional): A function that determines whether a file or folder should be ignored. Default is return_false().
        characters (dict, optional): A dictionary containing characters used for indentation and line styling. Default is None.

    Returns:
        str: The string representation of the folder structure.
    """
    if characters is None:
        characters = CHARACTERS

    text = ""

    gitignore_path = Path(directory_path, ".gitignore")
    gitignore_exists = gitignore_path.exists()

    list_files = list_and_short_files(directory_path)

    if gitignore_exists:
        is_ignored = parse_gitignore(gitignore_path)

    for file in list_files:
        if file == ".git":
            continue

        file_path = Path(directory_path, file)

        if is_ignored(file_path):
            continue

        line_char = "LLine" if list_files[-1] == file else "TLine"

        if file_path.is_dir():
            folder_text = characters["isFolder"] + file + characters["end_isFolder"]

            line_text = characters[line_char] + folder_text + characters["end_" + line_char]

            text += f"{indent}{line_text}{characters['end_indent']}"

            if line_char == "LLine":
                text += map_folders(
                    file_path, indent + characters["indent"], is_ignored, characters
                )
            else:
                text += map_folders(
                    file_path,
                    indent + characters["verticalLine"] + characters["indent"],
                    is_ignored,
                    characters,
                )

            if gitignore_exists:
                is_ignored = parse_gitignore(gitignore_path)
        else:
            line = characters[line_char] + file + characters["end_" + line_char]
            text += f"{indent}{line}{characters['end_indent']}"

    if gitignore_exists:
        is_ignored = return_false

    return text
