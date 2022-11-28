import os

files = os.listdir('.')
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".gjf":
        newname = portion[0] + ".in"
        os.rename(filename, newname)
