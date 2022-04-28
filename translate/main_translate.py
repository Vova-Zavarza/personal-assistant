import logic


close = '---Program closed---'

listfile = logic.listfile()


def translate():

    print(8 * '=' + 'If you want close translate program write <close>', '=' * 8)

    user = input('<r> if read or <w> if write: ')

    if user != 'close' and user == 'r' or user == 'w':

        print(f"You have {', '.join(listfile)} files. For create file write <new>.")
        file = input('File name: ')
        if file in listfile:
            if file == 'close':
                print(close)
            elif user == 'r':
                if file in logic.listfile():
                    logic.read(file)
                else:
                    print('File not found')
            elif user == 'w':
                logic.write(file)
            else:
                print('I don\'t know')
        elif file == 'new':
            logic.append_listfile()
        else:
            print('File not found')

    elif user == 'close':
        print(close)
    else:
        print('I don\'t know try again.')
