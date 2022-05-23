import logic


def translate():
    print(f'Du hast {logic.listfile()}')
    name = input('Gebst du einen Dateinamen ein: ')
    instance = logic.Vocabelheft(name)
    while True:
        command = input('Command: ')
        if command == 'r':
            instance.read()
        elif command == 'w':
            while True:
                flag = instance.write()
                if flag == 1:
                    break
        else:
            break


translate()
