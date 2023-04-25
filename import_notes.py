import json

from Note import Note


def import_notes():
    notes = []
    try:
        with open("notes.json", encoding="UTF-8") as file_in:
            dict_of_notes = json.load(file_in)
        for key in dict_of_notes:
            note = Note(key, dict_of_notes[key][0], dict_of_notes[key][1], dict_of_notes[key][2])
            notes.append(note)
    finally:
        return notes
