"""
    helper enum classes

    :copyright: 2020 Abhilash PS
    :license: The MIT License
"""

from enum import Enum, unique


@unique
class FileNameCase(Enum):
    """enum to represent the string case of the file name"""
    LOWER = 1
    UPPER = 2
    TITLE = 3
