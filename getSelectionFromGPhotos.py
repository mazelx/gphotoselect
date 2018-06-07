import os
from core.api import gpFinder

SELECTED_FOLDER = "gpselected"
REJECTED_FOLDER = "gprejected"

def get_files(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """

    dir = "/Users/mazelx/Pictures/Sources/2017/2017-07-16/"
    #dir = "C:\\Users\\xavier.mazellier\\Downloads\\test_gpFinder"
    os.chdir(dir)
    if not os.path.exists(SELECTED_FOLDER):
        os.mkdir(SELECTED_FOLDER)
    if not os.path.exists(REJECTED_FOLDER):
        os.mkdir(REJECTED_FOLDER)
    files = get_files(".")
    gpf = gpFinder()
    for i, file in enumerate(files):
        _file = file.split(".")[0]
        print("[" + str(i+1) + "/" + str(len(files)) + "] searching for " + _file)
        if gpf.exists(_file):
            os.rename(file, SELECTED_FOLDER + "/" + file)
        else:
            os.rename(file, REJECTED_FOLDER + "/" + file)
    print("done")

if __name__ == '__main__':
    main()
