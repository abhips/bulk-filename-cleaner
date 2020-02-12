# """
#     program to cleanup the file names in a directory
#
#     :copyright: 2020 Abhilash PS
#     :license: The MIT License
# """

from .user_input import UserInput
from .script_utils import ScriptUtils
from .question_helper import QuestionHelper
from .file_name_cleaner import FileNameCleaner


def run():
    input = UserInput()
    utils = ScriptUtils()
    qstn_helper = QuestionHelper()
    cleaner = FileNameCleaner(input)

    utils.print_out("")
    utils.print_out('------------------------------------------------------')
    utils.print_out('Enter "Exit" to exit the program.', '', 2)
    utils.print_out('For empty responses default options will be used.', '', 2)
    utils.print_out('------------------------------------------------------')
    utils.print_out("")

    while True:
        try:
            # accept the source directory path, from which the files will be accepted
            source_path = qstn_helper.get_source_directory()
            if not source_path:
                continue
            input.source_directory_path = source_path
            message = "source directory is - '{}'".format(source_path)
            utils.print_out(message, '', 4)

            # accept the target directory path, to which the renamed files will be copied
            input.target_directory_path = qstn_helper.get_target_directory(
                input.source_directory_path)
            message = "target directory is - '{}'".format(
                input.target_directory_path)
            utils.print_out(message, '', 4)

            # accept the input to decide if the file name should be in lower case or upper case or title case
            input.file_name_case = qstn_helper.get_file_name_case()
            message = "file name case is - '{}'".format(input.file_name_case)
            utils.print_out(message, '', 4)

            # accept the file name seperator character
            input.file_name_separator = qstn_helper.get_file_name_seperator()
            message = "file name case is - '{}'".format(input.file_name_separator)
            utils.print_out(message, '', 4)

            # accept the file name prefix
            input.file_name_prefix = qstn_helper.get_file_name_prefix()
            message = ''
            if input.file_name_prefix:
                message = "file name prefix is - '{}'".format(input.file_name_prefix)
            utils.print_out(message, '', 4)

            # path to the file which contains the list of words in single line separated by comma.
            # If any of these words occures in the file name then it will be removed the file name
            input.config_directory_path = qstn_helper.get_config_directory_path()
            message = "config directory path is - '{}'".format(
                input.config_directory_path)
            utils.print_out(message, '', 4)
            utils.print_out("", '', 0)

            # value of input
            print('----------------------------------------------------')
            print(input)
            print('----------------------------------------------------')

            # calling the cleaning function : this will cleanup the file names and copy them to the target directories
            if cleaner.cleanup():
                utils.print_out("------------- Finished -------------", '', 0)
                break


        except (KeyboardInterrupt, EOFError, SystemExit) as e:
            utils.print_out('', '', 4)
            message = "Exit request detected! Exiting the program."
            utils.print_out(message, '', 4)
            utils.print_out('', '', 4)
            utils.print_out("------------- Finished -------------", '', 0)
            break
        except Exception as ex:
            utils.print_out('', '', 4)
            message = "Unintented exception caught, #{}".format(
                type(ex).__name__)
            utils.print_out(message, '', 4)
            utils.print_out('', '', 4)
            utils.print_out("-------------- Something went wrong ----------------", '', 0)
            utils.print_out('', '', 4)
            continue
