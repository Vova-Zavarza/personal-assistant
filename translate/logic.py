import os

path = r'C:\project\personal-assistant\translate\files\\'[:-1]


def write(file):
    f = open(path + file, 'a')
    while True:
        word = input('New word: ')
        if word == 'close':
            break
        tran_word = input('Translate word: ')
        if tran_word == 'close':
            break
        f.write(word + ':' + tran_word + '\n')
        print('_' * 32)
    f.close()


def read(file):
    f = open(path + file)
    words = f.readline()
    while words != '':
        for char in words:
            if char != ':':
                print(char, end='')
            else:
                print(' => ', end='')
        print('_' * 32)
        words = f.readline()
    f.close()


def listfile():
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files


def append_listfile():
    new_file = input('Name of new file: ')
    write(new_file)

