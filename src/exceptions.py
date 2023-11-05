"""Errors"""


class FolderNotExists(Exception):
    """Custom exception for non-existing folder error"""

class MissingsKeys(Exception):
    """Custom exception for missing keys in parser_characters error"""

class MissingSearchWord(Exception):
    """Custom exception class for missing a specific key related to words."""