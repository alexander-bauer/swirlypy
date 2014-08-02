from swirlypy.questions.Recording import RecordingQuestion

class NewVariableQuestion(RecordingQuestion):

    _required_ = ["variables"]

    def test_response(self, response, data={}):
        mustasgn = self.variables
        didasgn = response["added"]
        didasgn.update(response["changed"])
      # For each required new variable, loop through the list of added
        # variables, and check that their value matches the required
        # one.
        for k in mustasgn.keys():
            # Check whether all required variables have been assigned and
            # have the correct values.
            if not k in didasgn:
                self.hint = "You neglected to create the variable, " + k
                return False
            if mustasgn[k] != didasgn[k] :
                self.hint = "You assigned the wrong value to the variable, " + k
                return False
        # If we exit the loop without failing, then we must've found all
        # of our requirements.
        return True

