from FileReader import FileReader


class StoryGenerator():

    def __init__(self):
        pass

    @staticmethod
    def create_story():
        story = FileReader.generate_sentence_1()
        story += " "
        story += FileReader.generate_sentence_2()
        story += " "
        story += FileReader.generate_sentence_3()
        print(story)
