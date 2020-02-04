"""
    program to cleanup the file names in a directory

    :copyright: 2020 Abhilash PS
    :license: The MIT License
"""

import os
import pathlib

from script_utils import ScriptUtils
from helper_enums import FileNameCase
from file_name_cleaner import FileNameCleaner

def run():
    target = os.getcwd()
    source = os.path.join(os.getcwd(), 'target_dir')
    cleaner = FileNameCleaner(target, source)
    script_utils_obj = ScriptUtils()

    while True:

        script_utils_obj.talk_to_user("")
        script_utils_obj.talk_to_user("")
        script_utils_obj.talk_to_user('------------------------------------------------------------------------------------------')
        script_utils_obj.talk_to_user('Enter "Exit" to exit the program.', '1.', 2)
        script_utils_obj.talk_to_user('You can give the empty response too, in that case default options will be used.', '2.', 2)
        script_utils_obj.talk_to_user('------------------------------------------------------------------------------------------')
        script_utils_obj.talk_to_user("")
        script_utils_obj.talk_to_user("")

        try:
            # accept the source directory path, from which the files will be accepted
            source_dir_path = script_utils_obj.ask_question("Enter the source directory name [default is the current directory]: ", '*', 1)

            if source_dir_path:
                file = pathlib.Path(source_dir_path)
                if file.exists():
                    cleaner.set__source_directory_name(source_dir_path)
                else:
                    source_dir_path = os.getcwd()
                    script_utils_obj.talk_to_user("Directory does not exist, using the default option", '', 4)
            else:
                source_dir_path = os.getcwd()
                script_utils_obj.talk_to_user("Empty input, using the default option", '', 4)

            script_utils_obj.talk_to_user("source directory is - {}".format(source_dir_path), '', 4)


            # accept the target directory path, to which the renamed files will be copied
            target_dir_path = script_utils_obj.ask_question("Enter the target directory name [default is the 'target_dir' inside the current "
                                    "directory]:", '*', 1)

            if target_dir_path:
                file = pathlib.Path(target_dir_path)
                if file.exists():
                    cleaner.set__target_directory_name(target_dir_path)
                else:
                    target_dir_path = os.path.join(os.getcwd(), 'target_dir')
                    directory = pathlib.Path(target_dir_path)
                    if not directory.exists():
                        os.mkdir(target_dir_path)
                    script_utils_obj.talk_to_user("Directory does not exist, using the default option", '', 4)
            else:
                target_dir_path = os.path.join(os.getcwd(), 'target_dir')
                directory = pathlib.Path(target_dir_path)
                if not directory.exists():
                    os.mkdir(target_dir_path)
                script_utils_obj.talk_to_user("Empty input, using the default option", '', 4)

            script_utils_obj.talk_to_user("target directory is {}".format(target_dir_path), '', 4)


            # accept the input to decide if the file name should be in lower case or upper case or title case
            file_name_case = script_utils_obj.ask_question("Enter the file name case [1 for lower | 2 for upper | 3 for title, 1 is the default value]: ", '*', 1)

            case_key = 1
            mapping = dict((item.value, item) for item in FileNameCase)

            if file_name_case:
                try:
                    case_key = int(file_name_case)
                    if case_key in list(mapping.keys()):
                        cleaner.set__file_name_case(mapping[case_key])
                    else:
                        script_utils_obj.talk_to_user("Wrong input for file name case, using the default value", '', 4)
                except Exception as e:
                    script_utils_obj.talk_to_user(e.message, '', 4)
                    script_utils_obj.talk_to_user("Wrong input for file name case, using the default value", '', 4)
            else:
                script_utils_obj.talk_to_user("Empty input for file name case, using the default value", '', 4)

            script_utils_obj.talk_to_user("File name case is {}".format(mapping[case_key].name), '', 4)

            # accept the file name seperator character
            file_name_separator = script_utils_obj.ask_question("Enter the file name word separator ['_' or '-', ' ' is the default]: ", '*', 1)

            if file_name_separator:
                separators = ['_', '-']
                if file_name_separator in separators:
                    cleaner.set__file_name_separator(file_name_separator)
                else:
                    script_utils_obj.talk_to_user("Wrong input for file name separator, using the default value", '', 4)
            else:
                file_name_separator = ' '
                script_utils_obj.talk_to_user("Empty input for file name separator, using the default value", '', 4)

            script_utils_obj.talk_to_user("File name separator is '{}'".format(file_name_separator), '', 4)



            # accept the file name seperator character
            file_name_prefix = script_utils_obj.ask_question("Enter the file name prefix: ", '*', 1)
            if file_name_prefix:
                cleaner.set__file_name_prefix(file_name_prefix)
            else:
                file_name_prefix = None
                script_utils_obj.talk_to_user("Empty input for file name prefix, not using the file prefix.", '', 4)

            script_utils_obj.talk_to_user("File name prefix is {}".format(file_name_prefix), '', 4)


            # path to the file which contains the list of words in single line separated by comma.
            # If any of these words occures in the file name then it will be removed the file name
            filter_file_path = script_utils_obj.ask_question("Enter the filter words file path [Default is None]: ", '*', 1)

            if filter_file_path:
                file = pathlib.Path(filter_file_path)
                if file.exists():
                    cleaner.set__filter_file_path(filter_file_path)
                else:
                    filter_file_path = None
                    script_utils_obj.talk_to_user("File does not exist, using the default option", '', 4)
            else:
                filter_file_path = None
                script_utils_obj.talk_to_user("Empty input, using the default option", '', 4)

            script_utils_obj.talk_to_user("Filter file path is {}".format(filter_file_path), '', 4)


            # cleaner object calling the cleaning function
            cleaner.copy_files_and_directories()

        except SystemExit:
            script_utils_obj.talk_to_user("Exit command detected! Exiting the program.", '', 4)
            break
        except KeyboardInterrupt:
            script_utils_obj.talk_to_user("Keyboard interrupt detected! Exiting the program.", '', 4)
            break
        except EOFError:
            script_utils_obj.talk_to_user("Keyboard interrupt detected! Exiting the program.", '', 4)
            break


if __name__ == "__main__":
    run()
