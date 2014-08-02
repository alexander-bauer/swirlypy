from swirlypy.questions.Recording import RecordingQuestion
import code, ast, sys

class GetValueQuestion(RecordingQuestion):
    
    _required_ = [ "values" ]
    #~ def get_response(self, data={}):
        #~ """Interacts with the user until broken from, or reaches EOF.
        #~ Each new expression, such as 'x**2', but unlike 'y = x**2', is
        #~ captured and yielded to the caller."""
        #~ console = self.new_console({})
        #~ for value in console.interact(""):
            #~ yield value

    def test_response(self, response, data={}):
        print("fields:", self.__dict__ )
        print(self.hint)
        # Instead of matching if the response is None, disregard the
        # "submission."
        # XXX: Allow for matching values of None.
        if response == None:
            return None
        # Note that response["values"] will always be of type Recorder (a subclass of list).
        # For now, the response will be considered correct if and only if some member
        # of response["values"] equals self.values.
        return self.values in response["values"]
