from swirlypy.question import CategoryQuestion

class TextQuestion(CategoryQuestion):
    def execute(self):
        self.print()
        self.get_response()

    def get_response(self):
        x=input('...')
