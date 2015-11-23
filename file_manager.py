import os
from sys import argv

script, dir_path = argv

os.chdir(dir_path)

list_all = os.listdir()

list_dir = []
list_file = []

# print
for i in list_all:
    if os.path.isdir(i):
        list_dir.append(i)
    else:
        list_file.append(i)

print("Number of directory: %d" % len(list_dir))
for dir_name in list_dir:
    print(dir_name)

print("Number of common files: %d"  % len(list_file))


list_ext = []

for file in list_file:
    splitname = os.path.splitext(file)

    #Exeptional handling
    if (len(splitname) != 2):
        raise AssertionError("Splited name size not equal to 2")

    if (len(splitname[1]) == 0):
        print(splitname)
        raise AssertionError("Extension string length is 0")

    if (splitname[1][0] != '.'):
        raise AssertionError("Extesion string does not start with point")

    str = splitname[1].replace(".", "")
    print(str)
    list_ext.append(str)



