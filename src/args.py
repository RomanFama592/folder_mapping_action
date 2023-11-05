"""Modules"""
from pathlib import Path
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


parser = ArgumentParser(
    prog="folder_mapping",
    description="Map folders and files to text using a template or without one.",
    formatter_class=ArgumentDefaultsHelpFormatter,
)

# groups

input_group = parser.add_argument_group(
    title="directory", description="Options for mapping a directory."
)

output_group = parser.add_argument_group(
    title="output", description="Options for the output of the mapping."
)

# args

input_group.add_argument(
    "path_directory",
    type=Path,
    help="The path to the input directory to map."
)

# flags

input_group.add_argument(
    "-sw",
    "--search_word",
    type=str,
    help=""
)

output_group.add_argument(
    "-po",
    "--path_output",
    type=Path,
    help="The path to the output directory. If not specified, the current directory is used.",
)

output_group.add_argument(
    "-to",
    "--template_output",
    type=Path,
    help="Specify a template for the output.",
)

output_group.add_argument(
    "-p",
    "--print",
    action="store_true",
    help="Print the map of folders and files to the console.",
)

args = parser.parse_args()
