import pathlib
import os.path as path
import shutil
import sys

exactPath = path.join(path.expandvars(r"%APPDATA%"), "Mozilla/Firefox/Profiles")
pathObj = pathlib.Path(exactPath).resolve()

profileDirs = [
    x for x in pathObj.iterdir() if x.is_dir() and "prefs.js" in str(list(x.iterdir()))
]

shutil.move(
    path.join(sys.path[0], "CustomUser.js"), path.join(profileDirs[0], "user.js")
)
