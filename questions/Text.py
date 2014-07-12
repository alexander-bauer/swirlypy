from swirlypy.question import CategoryQuestion

class TextQuestion(CategoryQuestion):
    def execute(self, data={}):
        self.print()
        self.get_response()

    def get_response(self, data={}):
        x=input('...')
