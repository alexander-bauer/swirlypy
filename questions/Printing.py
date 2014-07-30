from swirlypy.questions.Experimental import *

class PrintingQuestion(RecordingQuestion):
     
     def test_response(self, response, data={}):
        """
        just prints responses and returns True.
        """
        if "ast" in response:
            print("\nast: ", ast.dump(response["ast"]))
        if "added" in response:
            print("\nadded: ", response["added"])
        if "changed" in response:
            print("changed: ", response["changed"])
        if "removed" in response:
            print("removed: ", response["removed"])
        if "values" in response:
            print("\nvalues: ", response["values"])
        print("data: ",data)
        return True

