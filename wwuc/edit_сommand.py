from Note import *


def edit_сommand(notes):
    print('Введите id заметки: ')
    id = int(input())

    print('Введите новый загаловок или нажмите Enter: ')
    title1 = title = input()
    print('Введите новое тело заметки или нажмите Enter : ')
    msg1 = msg = input()
    if title1.strip() != '':
        for note in notes:
            if note.id == id:
                note.title = title
    if msg1.strip() != '':
        for note in notes:
            if note.id == id:
                note.msg = msg
    save_notes(notes)
    print('Ваша заметка успешно сохранена!')

