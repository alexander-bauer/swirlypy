from swirlypy.questions.Recording import RecordingQuestion
import swirlypy.colors as colors
import code, ast, sys

class CommandQuestion(RecordingQuestion):
    
    _required_ = [ "answer" ]
    
    def test_response(self, response, data={}):
        # Parse the provided correct answer in the same way it's parsed
        # by the CommandReturnerConsole.
        answer_tree = ast.parse(self.answer, filename="<answer>", \
                mode="single")

        # Now, we have to test their string dumps, because otherwise
        # it will resort to reference equality.
        # XXX: Find a more elegant way to do this.
        return ast.dump(answer_tree) == ast.dump(response["ast"])

