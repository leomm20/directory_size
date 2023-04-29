EXAMPLE:

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




OUTPUT EXAMPLE:

........

120.41 	Gb C:\Program Files
87.92 	Gb C:\Users
32.95 	Gb C:\Windows.old
29.97 	Gb C:\Riot Games
25.45 	Gb C:\Program Files (x86)
23.91 	Gb C:\Windows
10.47 	Gb C:\ProgramData
1.77 	Gb C:\1Leo


----------------------

[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_2.svg)](https://cafecito.app/leomm20)
