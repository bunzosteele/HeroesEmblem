from random import randint
import os


class FileReader():
    def __init__(self):
        pass

    @staticmethod
    def generate_name():
        with open(FileReader.resource_path("Units/Names.txt"), "r") as name_file:
            name = name_file.readline().replace("\n", "")
            names = []
            while name != '':
                names.append(name)
                name = name_file.readline().replace("\n", "")

            selection = randint(0, len(names) - 1)
            return names[selection]

    @staticmethod
    def generate_hometown():
        with open(FileReader.resource_path("Units/Hometowns.txt"), "r") as name_file:
            name = name_file.readline().replace("\n", "")
            names = []
            while name != '':
                names.append(name)
                name = name_file.readline().replace("\n", "")

            selection = randint(0, len(names) - 1)
            return names[selection]

    @staticmethod
    def generate_hobby():
        with open(FileReader.resource_path("Units/Hobbies.txt"), "r") as name_file:
            name = name_file.readline().replace("\n", "")
            names = []
            while name != '':
                names.append(name)
                name = name_file.readline().replace("\n", "")

            selection = randint(0, len(names) - 1)
            return names[selection]

    @staticmethod
    def generate_opinion():
        with open(FileReader.resource_path("Units/LikesDislikes.txt"), "r") as name_file:
            name = name_file.readline().replace("\n", "")
            names = []
            while name != '':
                names.append(name)
                name = name_file.readline().replace("\n", "")

            selection = randint(0, len(names) - 1)
            return names[selection]

    @staticmethod
    def generate_battlefield(difficulty):
            if difficulty <= 4:
                selection = randint(-10, difficulty)
            else:
                selection = randint(-10, 4)
            return str(selection)

    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )