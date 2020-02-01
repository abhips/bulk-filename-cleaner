import os
import shutil
import pathlib

from helper_enums import FileNameCase


class FileNameCleaner(object):
    """
        Actual class which do the file name cleanup functions
    """

    def __init__(self, source_dir, target_dir):
        self._filter_words = []
        self.__source_dir = source_dir
        self.__target_dir = target_dir
        self.__file_name_prefix = None
        self.__filter_file_path = None
        self.__file_name_separator = '_'
        self.__file_name_case = FileNameCase.LOWER

    def __repr__(self):
        return ' file_name_case - ' + str(self.__file_name_case) + ' <-> source_dir - ' + str(self.__source_dir) + ' <-> target_dir - ' + str(self.__target_dir) + ' <-> file_name_prefix - ' + str(self.__file_name_prefix) + ' <-> file_name_separator - ' + str(self.__file_name_separator) + ' <-> filter_file_path - ' + str(self.__filter_file_path)

    def __str__(self):
        return ' file_name_case - ' + str(self.__file_name_case) + ' <-> source_dir - ' + str(self.__source_dir) + ' <-> target_dir - ' + str(self.__target_dir) + ' <-> file_name_prefix - ' + str(self.__file_name_prefix) + ' <-> file_name_separator - ' + str(self.__file_name_separator) + ' <-> filter_file_path - ' + str(self.__filter_file_path)

    def set__target_directory_name(self, target_dir_path):
        self.__target_dir = target_dir_path

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
                    self._filter_words = f.read().splitlines()
            else:
                self.__filter_file_path = None

    def set__file_name_prefix(self, file_name_prefix):
        self.__file_name_prefix = file_name_prefix

    def copy_files_and_directories(self):

        target_paths = [self.__target_dir, ]
        source_paths = [self.__source_dir, ]


        while len(source_paths) != 0:
            source = source_paths.pop()
            target = target_paths.pop()

            print('source -- ', source)
            print('target -- ', target)
            print()

            dir_names = []
            file_names = []

            for (dirpath, dirnames, filenames) in os.walk(source):
                file_names.extend(filenames)
                dir_names.extend(dirnames)
                break

            while len(dir_names) != 0:
                old_d = dir_names.pop()
                new_d = self.cleanup_name(old_d, True)
                source_paths.append(os.path.join(source, old_d))
                target_paths.append(os.path.join(target, new_d))

                if not os.path.exists(os.path.join(target, new_d)):
                    os.makedirs(os.path.join(target, new_d))

            while len(file_names) != 0:
                old_f = file_names.pop()
                new_f = self.cleanup_name(old_f, False)
                print("'{}' ----> '{}'".format(os.path.join(source, old_f), os.path.join(target, new_f)))
                print()
                shutil.copy(os.path.join(source, old_f), os.path.join(target, new_f))
            print()

    def cleanup_name(self, old_name, is_directory):
        if is_directory:
            return old_name.title()

        return old_name.lower()
