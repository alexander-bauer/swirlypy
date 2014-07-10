from swirlypy.question import Question

class TextQuestion(Question):
    def __init__(self, category, output, **kwargs):
        self.category = category
        self.output = output
        self.__dict__.update(kwargs)
    def execute(self):
        self.print()
