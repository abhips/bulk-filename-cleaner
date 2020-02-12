import os

from .script_utils import ScriptUtils
from .helper_enums import FileNameCase


class UserInput(object):
    """
        initialization
    """

    def __init__(self):
        super(UserInput, self).__init__()

        pwd = os.path.dirname(__file__)

        self.__source_dir = None
        self.__target_dir = None
        self.__file_name_prefix = ''
        self.__file_name_separator = ' '
        self.__file_name_case = FileNameCase.LOWER
        self.__config_directory_path = os.path.join(pwd, '../config')

    def __repr__(self):
        return '[Source]    - ' + str(self.__source_dir) + ' \n[Target]    - ' + str(self.__target_dir )+ ' \n[Prefix]    - "' + str(self.__file_name_prefix) + '" \n[Seperator] - "' + str(self.__file_name_separator) + '" \n[Case]      - ' + str(self.__file_name_case) + ' \n[Config]    - ' + str(self.__config_directory_path)

    def __str__(self):
        return '[Source]    - ' + str(self.__source_dir) + ' \n[Target]    - ' + str(self.__target_dir )+ ' \n[Prefix]    - "' + str(self.__file_name_prefix) + '" \n[Seperator] - "' + str(self.__file_name_separator) + '" \n[Case]      - ' + str(self.__file_name_case) + ' \n[Config]    - ' + str(self.__config_directory_path)

    """
        source_directory_path getter and
    """

    def get_source_directory_path(self):
        return self.__source_dir

    def set_source_directory_path(self, source_dir):
        self.__source_dir = source_dir

    source_directory_path = property(
        get_source_directory_path, set_source_directory_path)

    """
        target_directory_path getter and
    """

    def get_target_directory_path(self):
        return self.__target_dir

    def set_target_directory_path(self, target_dir):
        self.__target_dir = target_dir

    target_directory_path = property(
        get_target_directory_path, set_target_directory_path)

    """
        file_name_prefix getter and
    """

    def get_file_name_prefix(self):
        return self.__file_name_prefix

    def set_file_name_prefix(self, prefix):
        self.__file_name_prefix = prefix

    file_name_prefix = property(get_file_name_prefix, set_file_name_prefix)

    """
        file_name_case getter and
    """

    def get_file_name_case(self):
        return self.__file_name_case

    def set_file_name_case(self, name_case):
        self.__file_name_case = name_case

    file_name_case = property(get_file_name_case, set_file_name_case)

    """
        file_name_separator getter and
    """

    def get_file_name_separator(self):
        return self.__file_name_separator

    def set_file_name_separator(self, separator):
        self.__file_name_separator = separator

    file_name_separator = property(
        get_file_name_separator, set_file_name_separator)

    """
        config_directory_path getter and
    """

    def get_config_directory_path(self):
        return self.__config_directory_path

    def set_config_directory_path(self, config_directory):
        self.__config_directory_path = config_directory

    config_directory_path = property(
        get_config_directory_path, set_config_directory_path)
