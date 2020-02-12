
import os

from .script_utils import ScriptUtils
from .helper_enums import FileNameCase


class QuestionHelper(object):
    """docstring for QuestionHelper."""

    def __init__(self):
        super(QuestionHelper, self).__init__()
        self.__utils = ScriptUtils()

    # function to accept the source directory path as user input
    def get_source_directory(self):
        message = "Enter the source directory name : "
        source_path = self.__utils.ask_question(message, '*', 1)

        if not source_path:
            message = "Source directory path is mandatory, please provide an absolute path."
            return None

        if not self.__utils.does_file_or_dir_exist(source_path):
            message = "Source directory does not exist !!!"
            self.__utils.print_out(message, '', 4)
            return None

        return source_path

    # function to accept the target directory path as user input
    def get_target_directory(self, source_path):
        message = "Enter the target directory name [default is the 'target_dir' inside the source directory] : "
        target_path = self.__utils.ask_question(message, '*', 1)

        if (not target_path) or (not self.__utils.does_file_or_dir_exist(target_path)):
            message = "Target directory does not exist. Creating the default target directory."
            self.__utils.print_out(message, '', 4)
            target_path = os.path.join(source_path, 'target_dir')
            if not self.__utils.does_file_or_dir_exist(target_path):
                os.mkdir(target_path)

        return target_path

    # function to accept the file name case as a user input
    def get_file_name_case(self):
        mapping = dict((item.value, item) for item in FileNameCase)

        message = "Enter the file name case [1 for lower | 2 for upper | 3 for title, 1 is the default value] : "
        file_name_case = self.__utils.ask_question(message, '*', 1)

        if not file_name_case:
            message = "Empty input for file name case, using the default value"
            self.__utils.print_out(message, '', 4)

            return FileNameCase.LOWER

        try:
            return mapping[int(file_name_case)]
        except Exception as e:
            self.__utils.print_out(e.message, '', 4)
            message = "Wrong input for file name case, using the default value"
            self.__utils.print_out(message, '', 4)

            return FileNameCase.LOWER

    # function to accept the file name seperator as a user input
    def get_file_name_seperator(self):
        separators = ['_', '-', ' ']

        message = "Enter the file name word separator ['_' or '-', ' ' is the default]: "
        file_name_separator = self.__utils.ask_question(message, '*', 1)

        if (not file_name_separator) or (not file_name_separator in separators):
            self.__utils.print_out(
                "Empty input for file name separator, using the default value", '', 4)
            return ' '

        return file_name_separator

    # function to accept the file name prefix as a user input
    def get_file_name_prefix(self):
        prefix = self.__utils.ask_question(
            "Enter the file name prefix: ", '*', 1)

        if not prefix:
            self.__utils.print_out(
                "Empty input for file name prefix, won't be using any file prefix.", '', 4)
            prefix = ''

        return prefix

    # function to accept the words file path
    def get_config_directory_path(self):
        config_path = self.__utils.ask_question(
            "Enter the config dir path [Default is None]: ", '*', 1)

        if (not config_path) or (not self.__utils.does_file_or_dir_exist(config_path)):
            self.__utils.print_out(
                "Directory doesn't exist, using the default option", '', 4)
            config_path = None

        return config_path
