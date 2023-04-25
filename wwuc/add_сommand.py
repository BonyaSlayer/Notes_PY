from Note import Note
from save_notes import save_notes


def add_сommand(notes):
    print('Введите заголовок заметки: ')
    title = input()
    print('Введите тело заметки: ')
    msg = input()
    note = Note(-1,title, msg,-1)
    notes.append(note)
    save_notes(notes)
    print('Ваша заметка успешно сохранена!')
