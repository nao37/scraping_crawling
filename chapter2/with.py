import sys


def file_open(file):
    with open(file) as f:
        print(f.read())


if len(sys.argv) > 1:
    file_open(sys.argv[1])
else:
    print('fileを指定してください。')
