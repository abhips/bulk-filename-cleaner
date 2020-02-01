from enum import Enum, unique

@unique
class FileNameCase(Enum):
    """enum to represent case of the file name"""
    LOWER = 1
    UPPER = 2
    TITLE = 3

@unique
class YesNo(Enum):
    """
        enum to represent yes no
    """
    NO = 0
    YES = 1
