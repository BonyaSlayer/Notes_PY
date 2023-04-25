import datetime
import json

from Id_generator import *
from save_notes import save_notes

gap = '      '


class Note:
    def __init__(self, id, title, msg, creation_time):
        if id == -1:
            self.id = new_id_generator()
        else:
            self.id = id

        if creation_time == -1:
            self.creation_time = datetime.datetime.now().strftime("%A %d-%b-%Y %H:%M:%S")
        else:
            self.creation_time = creation_time

        self.title = title
        self.msg = msg

    @staticmethod
    def print_head():
        print('id', gap, 'Title', gap, 'Message', gap, "Creation date", '\n')    
        
    def __str__(self):
        return f"Id: {self.id} \n " \
               f"{self.title} \n\n" \
               f"{self.msg}\n\n" \
               f"Creation date: {self.creation_time}\n\n"
