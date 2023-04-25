import json


def save_notes(notes):
    dict = {}
    for note in notes:
        dict[note.id] = note.title, note.msg, note.creation_time

    with open("notes.json", "w+", encoding="UTF-8") as file_out:
        json.dump(dict, file_out, default=str)
