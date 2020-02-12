"""
    actual class which do the file name cleanup functions

    :copyright: 2020 Abhilash PS
    :license: The MIT License
"""

import os
import shutil
import pathlib

from .helper_enums import FileNameCase
from .script_utils import ScriptUtils


class FileNameCleaner(object):


    def __init__(self, input):
        self.__filter_words = []
        self.__excluded_directories = []
        self.__input = input
        self.__utils = ScriptUtils()

    def __repr__(self):
        return ''

    def __str__(self):
        return ''

    """
        function to copy the files with cleaned up file names from source to target directories
    """

    def cleanup(self):

        # initialize the directory path lists
        source_dir_paths = [self.__input.source_directory_path, ]
        target_dir_paths = [self.__input.target_directory_path, ]

        self.__utils.print_out("")

        # process directory path lists and create target directories
        while len(source_dir_paths) != 0:
            src_path = source_dir_paths.pop()
            trgt_path = target_dir_paths.pop()

            # initialize lists to hold filenames and directory names for the current directory
            dir_names = []
            file_names = []

            # append filenames and directory names to the corresponding lists
            for (dirpath, dirnames, filenames) in os.walk(src_path):
                file_names.extend(filenames)
                dir_names.extend(dirnames)
                break

            # adding to sub directory list
            while len(dir_names) != 0:
                old_dir = dir_names.pop()
                source_dir_path = os.path.join(src_path, old_dir)

                # cleanup the old directory name
                new_dir = self.cleanup_name(source_dir_path, old_dir, True)
                target_dir_path = os.path.join(trgt_path, new_dir)

                if source_dir_path == self.__input.target_directory_path:
                    continue

                source_dir_paths.append(source_dir_path)
                target_dir_paths.append(target_dir_path)
                if not os.path.exists(target_dir_path):
                    self.__utils.print_out(
                        "creating directory '{}'".format(target_dir_path), '', 4)
                    os.makedirs(target_dir_path)

            # copying the files
            while len(file_names) != 0:
                old_f = file_names.pop()
                new_f = self.cleanup_name(os.path.join(src_path, old_f), old_f, False)
                self.__utils.print_out(
                    "'{}' ----> '{}'".format(os.path.join(src_path, old_f), os.path.join(trgt_path, new_f)), '', 4)
                self.__utils.print_out("", '', 4)

                try:
                    shutil.copy(os.path.join(src_path, old_f),
                                os.path.join(trgt_path, new_f))
                except PermissionError as pe:
                    self.__utils.print_out(
                        'PermissionError - {} - {}'.format(pe, os.path.join(src_path, old_f)), '#', 4)
                except FileNotFoundError as fne:
                    self.__utils.print_out(
                        'FileNotFoundError - {} - {}'.format(fne, os.path.join(src_path, old_f)), '#', 4)

        return True

    """
        function to cleanup the filename. If it is a directory then name will Title cased,
        for files it will be according to the user input.
    """
    def cleanup_name(self, old_full_path, old_name, is_directory):

        extension = ''
        root_name = old_name
        if not is_directory:
            _, extension = os.path.splitext(old_full_path)
            root_name = root_name.replace(extension, '')
            extension = extension.lower()

        new_name = root_name.lower()

        # filter out the words in the filter list
        if len(self.__filter_words) > 0:
            for filter in self.__filter_words:
                new_name = new_name.replace(filter.lower(), ' ')

        # replace the excess ' ' with single ' '
        new_name = self.__utils.replace_multiple_character_occurances(
            new_name, ' ')

        # change the file name case
        if not is_directory:
            if self.__input.file_name_case == FileNameCase.LOWER:
                new_name = new_name.lower()
            elif self.__input.file_name_case == FileNameCase.UPPER:
                new_name = new_name.upper()
            elif self.__input.file_name_case == FileNameCase.TITLE:
                new_name = new_name.title()
            else:
                new_name = new_name.lower()
        else:
            new_name = new_name.title()

        # add the file name prefix
        if self.__input.file_name_prefix and not is_directory:
            new_name = self.__input.file_name_prefix + ' ' + new_name

        # change the file name separator
        new_name = new_name.replace(',', self.__input.file_name_separator)
        new_name = new_name.replace('(', self.__input.file_name_separator)
        new_name = new_name.replace(')', self.__input.file_name_separator)
        new_name = new_name.replace('[', self.__input.file_name_separator)
        new_name = new_name.replace(']', self.__input.file_name_separator)
        new_name = new_name.replace('{', self.__input.file_name_separator)
        new_name = new_name.replace('}', self.__input.file_name_separator)
        new_name = new_name.replace('`', self.__input.file_name_separator)
        new_name = new_name.replace('.', self.__input.file_name_separator)
        new_name = new_name.replace('"', self.__input.file_name_separator)
        new_name = new_name.replace("'", self.__input.file_name_separator)
        new_name = new_name.replace(',', self.__input.file_name_separator)
        new_name = new_name.replace('+', self.__input.file_name_separator)
        new_name = new_name.replace('*', self.__input.file_name_separator)
        new_name = new_name.replace('~', self.__input.file_name_separator)
        new_name = new_name.replace('^', self.__input.file_name_separator)
        new_name = new_name.replace('=', self.__input.file_name_separator)
        new_name = new_name.replace('@', self.__input.file_name_separator)
        new_name = new_name.replace('#', self.__input.file_name_separator)
        new_name = new_name.replace('$', self.__input.file_name_separator)
        new_name = new_name.replace('%', self.__input.file_name_separator)
        new_name = new_name.replace('&', self.__input.file_name_separator)
        new_name = new_name.replace('!', self.__input.file_name_separator)
        new_name = new_name.replace('—', self.__input.file_name_separator)

        # strip off any leading or trailing spaces
        new_name = new_name.strip()

        if self.__input.file_name_separator == '_':
            new_name = new_name.replace(' ', '_')
            new_name = new_name.replace('-', '_')
        elif self.__input.file_name_separator == '-':
            new_name = new_name.replace(' ', '-')
            new_name = new_name.replace('_', '-')
        else:
            new_name = new_name.replace('-', ' ')
            new_name = new_name.replace('_', ' ')
            new_name = new_name.strip()

        new_name = self.__utils.replace_multiple_character_occurances(
            new_name, self.__input.file_name_separator)

        if not is_directory:
            new_name = new_name + extension

        return new_name
