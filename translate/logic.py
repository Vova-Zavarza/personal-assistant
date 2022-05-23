import shelve

path = r'C:\project\personal-assistant\translate\files\\'[:-1]


class Vocabelheft:
    def __init__(self, name):
        self.name = name
        self.mainbase = shelve.open(path + 'worterdb')
        self.mainbase[self.name] = shelve.open(path + self.name)

    def write(self):
        word = input('Neues Wort: ')
        if word == 'schließen':
            return 1
        tran_word = input('Eine Übersetzung eines Wortes: ')
        if tran_word == 'schließen':
            return 1
        self.mainbase[self.name][word] = tran_word
        print('_' * 32)

    def read(self):
        db = shelve.open(path + self.name)
        for word in db:
            print(word, '=>', db[word])
            print('_' * 32)
        db.close()


def listfile():
    mainbase = shelve.open(path + 'worterdb')
    files = [f for f in mainbase]
    return files
