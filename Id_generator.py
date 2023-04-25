import json


def new_id_generator():
    with open("id.json", encoding="UTF-8") as file_in:
        id = int(json.load(file_in))
    with open("id.json", "w+", encoding="UTF-8") as file_out:
        json.dump(id+1, file_out)

    return id