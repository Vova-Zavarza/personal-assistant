import sys
import subprocess
import time

sys.path.append(r'C:\project\personal-assistant\translate')
import main_translate


def clock():
    current_time = time.strftime(' %A/%B Time: %H:%M.%S Date: %d.%m.%Y')
    cover = '|' + '-' * (len(current_time)-1) + '|'
    print(cover + '\n' + current_time + '\n' + cover)


if sys.platform[:3] == 'win':
    print(' ' * 5 + 'Your platform is Windows')
else:
    print(' ' * 5 + 'Your platform is Unix')

print('--You use voldy\'s assistant')
arguments = sys.argv[1:]

for arg in arguments:
    arg = arg[1:]
    if arg == 'T':
        main_translate.translate()
    elif arg == 't':
        clock()
    elif arg == 'ch':
        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    else:
        print('I don\'t know what you want!')
    time.sleep(2)
