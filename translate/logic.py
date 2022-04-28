def write(file):
    f = open(r'C:\testCode\Germany\translate\files\\'[:-1] + file + '.txt', 'a')
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
    f = open(r'C:\testCode\Germany\translate\files\\'[:-1] + file + '.txt')
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
    files = open(r'C:\testCode\Germany\translate\files\listfile.txt')
    list_files = files.read().split(',')
    return list_files


def append_listfile():
    files = open(r'C:\testCode\Germany\translate\files\listfile.txt', 'a')
    new_file = input('Name of new file: ')
    files.write(',' + new_file)
    write(new_file)

