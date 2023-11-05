"""Modules"""
from os import listdir
from pathlib import Path


def get_folder_key(directory_path):
    """
    Returns a function that can be used as a key for sorting files in a directory.

    Args:
        directory_path (str): The path of the directory for which the key is being generated.

    Returns:
        function: A function that can be used as a key for sorting files in a directory.

    Example:
        directory_path = '/path/to/directory'
        key = get_folder_key(directory_path)
        files = ['file1.txt', 'file2.txt', 'file3.txt']
        sorted_files = sorted(files, key=key)
        print(sorted_files)
    """
    directory_path = Path(directory_path)

    def key_for_sorting(file_name):
        """
        Nested function that defines the key for sorting files.

        Args:
            file_name (str): The name of the file.

        Returns:
            tuple: A tuple containing two values:
                - The negation of the result of `file_path.is_dir()` 
                (to sort directories before files).
                - The `file_name` itself.
        """
        file_path = directory_path.joinpath(file_name)
        return (not file_path.is_dir(), file_name)

    return key_for_sorting


def list_and_short_files(directory):
    """
    Returns a sorted list of files in the given directory.

    Args:
        directory (str): The path of the directory for which the files need to be listed and sorted.

    Returns:
        list[str]: A sorted list of files in the given directory.
    """
    list_files: list[str] = listdir(directory)
    list_files.sort(key=get_folder_key(directory))

    return list_files
