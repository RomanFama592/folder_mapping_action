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
"end_indent": "\n"
}

def map_folders(directory_path: Path, indent: str = "", is_ignored = None, characters = None) -> str:
    if is_ignored == None:
        is_ignored = lambda x: False

    if characters == None:
        characters = CHARACTERS

    text = ""

    gitignore_path = Path(directory_path, ".gitignore")
    gitignore_exists = gitignore_path.exists()

    list_files = list_and_short_files(directory_path)
    
    if gitignore_exists:
        is_ignored = parse_gitignore(gitignore_path)
    
    for i, item in enumerate(list_files):
        file_path = Path(directory_path, item)

        if is_ignored(file_path) or item == ".git":
            continue


        # new
        line_char = "LLine" if list_files[-1] == item else "TLine"

        if file_path.is_dir():
            folder_name = characters["isFolder"] + item + characters["end_isFolder"]
            
            text += f"{indent}{characters[line_char]}{folder_name}{characters['end_' + line_char]}{characters['end_indent']}"
            
            if line_char == "LLine":
                text += map_folders(file_path, indent + characters["indent"], is_ignored, characters)
            else:
                text += map_folders(file_path, indent + characters["verticalLine"] + characters["indent"], is_ignored, characters)
            
            if gitignore_exists:
                is_ignored = parse_gitignore(gitignore_path)
        else:
            text += f"{indent}{characters[line_char]}{item}{characters['end_' + line_char]}{characters['end_indent']}"
        
    if gitignore_exists:
        is_ignored = lambda x: False

    return text