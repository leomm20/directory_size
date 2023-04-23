import os
from pathlib import Path


def get_dir_size(path='.', size_in='bytes'):
    total = 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
    except:
        print('', end='')
    match size_in:
        case 'kb':
            return total/1024
        case 'mb':
            return total/1024/1024
        case 'gb':
            return total/1024/1024/1024
        case 'tb':
            return total/1024/1024/1024/1024
        case 'pb':
            return total/1024/1024/1024/1024/1024
        case 'eb':
            return total/1024/1024/1024/1024/1024/1024
        case 'zb':
            return total/1024/1024/1024/1024/1024/1024/1024
        case 'yb':
            return total/1024/1024/1024/1024/1024/1024/1024/1024
        case _:
            # bytes
            return total


# # NOT WAS TESTED
# def get_size(path='.'):
#     if os.path.isfile(path):
#         return os.path.getsize(path)
#     elif os.path.isdir(path):
#         return get_dir_size(path)


my_list = []
for directory in os.listdir('C:\\'):
    if Path('c:\\', directory).is_dir() and directory[0] != '$':
        size = round(get_dir_size(str(Path('C:\\', directory)), 'gb'), 2)
        if size > 1:
            my_list.append([size, str(Path('C:\\', directory))])
            print('.', end='')

print('\n')
my_list.sort(reverse=True)
for item in my_list:
    print(item[0], '\tGb', item[1])
