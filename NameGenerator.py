from random import randint
import os


class NameGenerator():
    def __init__(self):
        pass

    @staticmethod
    def generate_name(input_file):
        with open(NameGenerator.resource_path(input_file), "r") as name_file:
            name = name_file.readline().replace("\n", "")
            names = []
            while name != '':
                names.append(name)
                name = name_file.readline().replace("\n", "")

            selection = randint(0, len(names) - 1)
            return names[selection]

    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )