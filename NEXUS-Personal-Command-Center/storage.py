
import json
import os


DATA_FOLDER = "data"


def save_data(filename, data):
    os.makedirs(DATA_FOLDER, exist_ok=True)

    filepath = os.path.join(DATA_FOLDER, filename)

    try:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

    except (OSError, TypeError) as error:
        print("Error saving data:", error)


def load_data(filename):
    filepath = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r") as file:
            return json.load(file)

    except (OSError, json.JSONDecodeError) as error:
        print("Error loading data:", error)
        return []
