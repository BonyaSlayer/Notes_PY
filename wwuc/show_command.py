from Note import *


def show_command(notes, flag):  # the flag indicates whether to output all notes or a specific
    if flag:
        for note in notes:
            print(note)
    else:
        print('Введите id заметки: ', end='')
        id = int(input())
        for note in notes:
            if note.id == id:
                print(note)

