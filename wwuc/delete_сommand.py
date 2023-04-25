from Note import *


def delete_сommand(notes):
    print('Введите id заметки: ', end='')
    id = int(input())
    for note in notes:
        if note.id == id:
            notes.remove(note)
            break
    save_notes(notes)

