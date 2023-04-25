import json
import os
from Note import *
from import_notes import import_notes
from wwuc.add_сommand import add_сommand
from wwuc.delete_сommand import delete_сommand
from wwuc.edit_сommand import edit_сommand
from wwuc.help_command import help_command
from wwuc.show_command import show_command

notes = import_notes()


while True:
    print('\n\nВведите команду: ', end = '')
    command = input()
    match command:
        case 'add':
            add_сommand(notes)
        case 'delete':
            delete_сommand(notes)
        case 'edit':
            edit_сommand(notes)
        case 'show all':
            show_command(notes, True)
        case 'show':
            show_command(notes, False)
        case '/help':
            help_command()
        case _:
            print('Вы ввели неверную команду, попробуйте еще раз или введите /help')
