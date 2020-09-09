from os import listdir, rename
from os.path import isfile, join
from sanitize_filename import sanitize

if __name__ == "__main__":
    target_dir = "./"

    onlyfiles = [f for f in listdir(target_dir) if isfile(join(target_dir, f))]
    for file in onlyfiles:
        sanitized = sanitize(file)
        if sanitized != file:
            # we need to rename the file
            rename(target_dir+file, target_dir+sanitized)
