# pylint: disable=missing-module-docstring
from pathlib import Path
from src.args import args
from src.exceptions import FolderNotExists, MissingSearchWord
from src.map_folders import map_folders, CHARACTERS

# verify if exists folder

if not args.path_directory.exists():
    raise FolderNotExists(f"The folder objective '{args.path_directory}' not exists.")

# create output file

if isinstance(args.path_output, Path) and args.path_output:
    with open(args.path_output, "a", encoding="utf-8") as output:
        output.write("")

# if exists a search word
if args.search_word:
    key_word = r"%{{" + args.search_word + r"}}%"
else:
    raise MissingSearchWord("")

# update characters

characters = CHARACTERS

# create map folder

text = (
    f"{characters['init']}\n"
    + map_folders(args.path_directory)
    + characters["end_init"]
)

text_final = text

# verify if exists a template and read template to modify

if isinstance(args.template_output, Path) and args.template_output.exists():
    with open(args.template_output, "r", encoding="utf-8") as template:
        text_final = template.read()
        text_final = text_final.replace(key_word, text)

# print by console the text

if args.print:
    print(text_final)

# write text_final in path_output

if isinstance(args.path_output, Path):
    with open(args.path_output, "w", encoding="utf-8") as output:
        output.write(text_final)
