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
        max_field = 6
        if difficulty > max_field:
            selection = randint(-6, max_field)
        else:
            selection = randint(-6, difficulty - 1)
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

    @staticmethod
    def generate_profession():
        with open(FileReader.resource_path("Story\my_professions.txt"), "r") as the_nouns:
            noun = the_nouns.readline().replace("\n", "")
            nouns = []
            while noun != '':
                nouns.append(noun)
                noun = the_nouns.readline().replace("\n", "")

            selection = randint(0, len(nouns) - 1)
            return nouns[selection]

    @staticmethod
    def generate_thing():
        with open(FileReader.resource_path("Story\my_things.txt"), "r") as the_things:
            thing = the_things.readline().replace("\n", "")
            things = []
            while thing != '':
                things.append(thing)
                thing = the_things.readline().replace("\n", "")

            selection = randint(0, len(things) - 1)
            return things[selection]

    @staticmethod
    def generate_pronoun():
        with open(FileReader.resource_path("Story\pronouns.txt"), "r") as the_pronouns:
            pronoun = the_pronouns.readline().replace("\n", "")
            pronouns = []
            while pronoun != '':
                pronouns.append(pronoun)
                pronoun = the_pronouns.readline().replace("\n", "")

            selection = randint(0, len(pronouns) - 1)
            return pronouns[selection]

    @staticmethod
    def generate_adjective():
        with open(FileReader.resource_path("Story\my_adjectives.txt"), "r") as the_adjective:
            adjective = the_adjective.readline().replace("\n", "")
            adjectives = []
            while adjective != '':
                adjectives.append(adjective)
                adjective = the_adjective.readline().replace("\n", "")

            selection = randint(0, len(adjectives) - 1)
            return adjectives[selection]

    @staticmethod
    def generate_adjective_2():
        with open(FileReader.resource_path("Story\more_adjectives.txt"), "r") as the_adjective:
            adjective = the_adjective.readline().replace("\n", "")
            adjectives = []
            while adjective != '':
                adjectives.append(adjective)
                adjective = the_adjective.readline().replace("\n", "")

            selection = randint(0, len(adjectives) - 1)
            return adjectives[selection]

    @staticmethod
    def generate_object():
        with open(FileReader.resource_path("Story\my_objects.txt"), "r") as the_objects:
            a_object = the_objects.readline().replace("\n", "")
            objects = []
            while a_object != '':
                objects.append(a_object)
                a_object = the_objects.readline().replace("\n", "")

            selection = randint(0, len(objects) - 1)
            return objects[selection]

    @staticmethod
    def generate_sentence_1():
        with open(FileReader.resource_path("Story\sentences_1.txt"), "r") as sentences_1:
            sentence = sentences_1.readline().replace("\n", "")
            sentence = sentence.replace("%n", FileReader.generate_profession())
            sentences = []
            while sentence != '':
                sentences.append(sentence)
                sentence = sentences_1.readline().replace("\n", "")
                sentence = sentence.replace("%n", FileReader.generate_profession())
            selection = randint(0, len(sentences) - 1)
            return sentences[selection]

    @staticmethod
    def generate_sentence_2():
        with open(FileReader.resource_path("Story\sentences_2.txt"), "r") as sentences_2:
            sentence = sentences_2.readline().replace("\n", "")
            sentence = sentence.replace("%n", FileReader.generate_thing())
            sentence = sentence.replace("%p", FileReader.generate_pronoun())
            sentence = sentence.replace("%a", FileReader.generate_adjective())
            sentences = []
            while sentence != '':
                sentences.append(sentence)
                sentence = sentences_2.readline().replace("\n", "")
                sentence = sentence.replace("%n", FileReader.generate_thing())
                sentence = sentence.replace("%p", FileReader.generate_pronoun())
                sentence = sentence.replace("%a", FileReader.generate_adjective())
            selection = randint(0, len(sentences) - 1)
            return sentences[selection]

    @staticmethod
    def generate_sentence_3():
        with open(FileReader.resource_path("Story\sentences_3.txt"), "r") as sentences_3:
            sentence = sentences_3.readline().replace("\n", "")
            sentence = sentence.replace("%a", FileReader.generate_adjective_2())
            sentence = sentence.replace("%n", FileReader.generate_object())
            sentences = []
            while sentence != '':
                sentences.append(sentence)
                sentence = sentences_3.readline().replace("\n", "")
                sentence = sentence.replace("%a", FileReader.generate_adjective_2())
                sentence = sentence.replace("%n", FileReader.generate_object())
            selection = randint(0, len(sentences) - 1)
            return sentences[selection]
