# Bulk filename cleaner
A python script to bulk rename/clean file names with an option to give configuration choice

## Can run the script by `python3 cleaner.py` (python 3.4 or greater is the only requirement)

This script was cearted to cleanup the messedup filenames in my Music/Videos/Documents directories.

Options can be chosen to configure how the renaming/cleanup of filenames will happen.

Options are

1) `source directory` - source directory is the directory which contains the files to be worked up on, full path is requiered.
2) `target directory` - target directory is the directory to which the cleaned up files will be copied, full path is required.
3) `string case of filename` - decides the string case of the filenames. choices are lower case, upper case, and title case.
4) `file name word separator` - charactor to separate the words in the file names. Options are _ , - and " "(single space).
5) `file name prefix` - a prefix can be used with the files, by default it is None.
6) `filter file path` - file names can be cleaned by removing certain words and these word can be provided in a file. This filter file contains each words in each lines.

P.S:- `master` branch has the stable code. `development` branch has latest code

### TODO
1) add more regex - there are lot of places where I can use regex.
2) add more comments.
3) conevrt repeatedly used code to snippets and functions and logically group them to module.
4) update README.md for more clarity.
5) update the script to accept the commandline arguments and run it as a terminal command.
6) optimize and simplify the code.
