from swirlypy.questions.Recording import RecordingQuestion
import swirlypy.colors as colors
import code, ast, sys

class CommandQuestion(RecordingQuestion):
    """Gives the user a shell prompt, and compares their inputs to a
given answer. This is accomplished by parsing both inputs as Abstract
Syntax Trees, and comparing those directly. Thus, syntactical
differences, such as single-quotes versus double-quotes, do not
matter."""
    
    _required_ = [ "answer" ]
    
    def test_response(self, response, data={}):
        # We have to test their string dumps, because otherwise
        # it will resort to reference equality.
        # XXX: Find a more elegant way to do this.
        return ast.dump(answer_tree) == ast.dump(response["ast"])

    def yaml_hook(self):
        """Parses given answer as an AST and stores it as
answer_tree."""
        # Parse the provided correct answer a standard way.
        self.answer_tree = ast.parse(self.answer, filename="<answer>", \
                mode="single")
