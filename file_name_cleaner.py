"""
    actual class which do the file name cleanup functions

    :copyright: 2020 Abhilash PS
    :license: The MIT License
"""

import os
import shutil
import pathlib

from helper_enums import FileNameCase
from script_utils import ScriptUtils


class FileNameCleaner(object):

    __script_utils_obj = ScriptUtils()

    def __init__(self, source_dir, target_dir):
        self.__filter_words = []
        self.__source_dir = source_dir
        self.__target_dir = target_dir
        self.__file_name_prefix = None
        self.__filter_file_path = None
        self.__file_name_separator = ' '
        self.__file_name_case = FileNameCase.LOWER

    def __repr__(self):
        return ' file_name_case - ' + str(self.__file_name_case) + ' <-> source_dir - ' + str(
            self.__source_dir) + ' <-> target_dir - ' + str(self.__target_dir) + ' <-> file_name_prefix - ' + str(
            self.__file_name_prefix) + ' <-> file_name_separator - ' + str(
            self.__file_name_separator) + ' <-> filter_file_path - ' + str(self.__filter_file_path)

    def __str__(self):
        return ' file_name_case - ' + str(self.__file_name_case) + ' <-> source_dir - ' + str(
            self.__source_dir) + ' <-> target_dir - ' + str(self.__target_dir) + ' <-> file_name_prefix - ' + str(
            self.__file_name_prefix) + ' <-> file_name_separator - ' + str(
            self.__file_name_separator) + ' <-> filter_file_path - ' + str(self.__filter_file_path)

    """
        Setters for the member variables
    """

    def set__target_directory_name(self, target_dir_path):
        self.__target_dir = target_dir_path
        file = pathlib.Path(target_dir_path)
        if not file.exists():
            os.makedirs(target_dir_path)

    def set__source_directory_name(self, source_dir_path):
        self.__source_dir = source_dir_path

    def set__file_name_case(self, file_name_case):
        self.__file_name_case = file_name_case

    def set__file_name_separator(self, file_name_separator):
        self.__file_name_separator = file_name_separator

    def set__filter_file_path(self, filter_file_path):
        self.__filter_file_path = filter_file_path

        if filter_file_path:
            file = pathlib.Path(filter_file_path)
            if file.exists():
                with open(filter_file_path, 'r') as f:
                    self.__filter_words = f.read().splitlines()
            else:
                self.__filter_file_path = None

    def set__file_name_prefix(self, file_name_prefix):
        self.__file_name_prefix = file_name_prefix

    """
        function to copy the files with cleaned up file names from source to target directories
    """

    def copy_files_and_directories(self):

        # initialize the directory path lists
        source_dir_paths = [self.__source_dir, ]
        target_dir_paths = [self.__target_dir, ]

        self.__script_utils_obj.talk_to_user("")

        # process directory path lists and create target directories
        while len(source_dir_paths) != 0:
            src_path = source_dir_paths.pop()
            trgt_path = target_dir_paths.pop()

            self.__script_utils_obj.talk_to_user("")
            self.__script_utils_obj.talk_to_user('source -- {}'.format(src_path), '', 4)
            self.__script_utils_obj.talk_to_user('target -- {}'.format(trgt_path), '', 4)
            self.__script_utils_obj.talk_to_user("")

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

                if source_dir_path == self.__target_dir:
                    continue

                source_dir_paths.append(source_dir_path)
                target_dir_paths.append(target_dir_path)
                if not os.path.exists(target_dir_path):
                    self.__script_utils_obj.talk_to_user("creating directory '{}'".format(target_dir_path), '', 4)
                    os.makedirs(target_dir_path)

            # copying the files
            while len(file_names) != 0:
                old_f = file_names.pop()
                new_f = self.cleanup_name(os.path.join(src_path, old_f), old_f, False)
                self.__script_utils_obj.talk_to_user("'{}' ----> '{}'".format(os.path.join(src_path, old_f), os.path.join(trgt_path, new_f)), '', 4)
                self.__script_utils_obj.talk_to_user("", '', 4)

                try:
                    shutil.copy(os.path.join(src_path, old_f), os.path.join(trgt_path, new_f))
                except PermissionError as pe:
                    self.__script_utils_obj.talk_to_user('PermissionError - {} - {}'.format(pe, os.path.join(src_path, old_f)), '#', 4)
                except FileNotFoundError as fne:
                    self.__script_utils_obj.talk_to_user('FileNotFoundError - {} - {}'.format(fne, os.path.join(src_path, old_f)), '#', 4)

    """
        function to cleanup the filename. If it is a directory then name will Title cased, for files it will be according to the user input.
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
        new_name = self.__script_utils_obj.replace_multiple_character_occurances(new_name, ' ')


        # change the file name case
        if not is_directory:
            if self.__file_name_case == FileNameCase.LOWER:
                new_name = new_name.lower()
            elif self.__file_name_case == FileNameCase.UPPER:
                new_name = new_name.upper()
            elif self.__file_name_case == FileNameCase.TITLE:
                new_name = new_name.title()
            else:
                new_name = new_name.lower()
        else:
            new_name = new_name.title()

        # add the file name prefix
        if self.__file_name_prefix and not is_directory:
            new_name = self.__file_name_prefix + ' ' + new_name

        # change the file name separator
        new_name = new_name.replace(',', self.__file_name_separator)
        new_name = new_name.replace('(', self.__file_name_separator)
        new_name = new_name.replace(')', self.__file_name_separator)
        new_name = new_name.replace('[', self.__file_name_separator)
        new_name = new_name.replace(']', self.__file_name_separator)
        new_name = new_name.replace('{', self.__file_name_separator)
        new_name = new_name.replace('}', self.__file_name_separator)
        new_name = new_name.replace('`', self.__file_name_separator)
        new_name = new_name.replace('.', self.__file_name_separator)
        new_name = new_name.replace('"', self.__file_name_separator)
        new_name = new_name.replace("'", self.__file_name_separator)
        new_name = new_name.replace(',', self.__file_name_separator)
        new_name = new_name.replace('+', self.__file_name_separator)
        new_name = new_name.replace('*', self.__file_name_separator)
        new_name = new_name.replace('~', self.__file_name_separator)
        new_name = new_name.replace('^', self.__file_name_separator)
        new_name = new_name.replace('=', self.__file_name_separator)
        new_name = new_name.replace('@', self.__file_name_separator)
        new_name = new_name.replace('#', self.__file_name_separator)
        new_name = new_name.replace('$', self.__file_name_separator)
        new_name = new_name.replace('%', self.__file_name_separator)
        new_name = new_name.replace('&', self.__file_name_separator)
        new_name = new_name.replace('!', self.__file_name_separator)
        new_name = new_name.replace('—', self.__file_name_separator)

        # strip off any leading or trailing spaces
        new_name = new_name.strip()

        if self.__file_name_separator == '_':
            new_name = new_name.replace(' ', '_')
            new_name = new_name.replace('-', '_')
        elif self.__file_name_separator == '-':
            new_name = new_name.replace(' ', '-')
            new_name = new_name.replace('_', '-')
        else:
            new_name = new_name.replace('-', ' ')
            new_name = new_name.replace('_', ' ')
            new_name = new_name.strip()

        new_name = self.__script_utils_obj.replace_multiple_character_occurances(new_name, self.__file_name_separator)

        if not is_directory:
            new_name = new_name + extension

        return new_name
