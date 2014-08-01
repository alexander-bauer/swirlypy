from swirlypy.question import CategoryQuestion
import swirlypy.colors as colors

class HelloQuestion(CategoryQuestion):
    def execute(self, data={}):
        colors.print_help("Hello!")
