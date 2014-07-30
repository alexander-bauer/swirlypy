from swirlypy.question import ShellQuestion

# XXX: Get individual lines of input and evaluate them to get their
# values, rather than only looking through stored variables.
class NewVariableQuestion(ShellQuestion):
    _required_ = ["variables"]
    def get_response(self, data={}):
        return self.shell()

    def test_response(self, response, data={}):
        # Parse the variable list.
        # XXX: Make this more flexible, particularly allowing for named
        # variables.
        mustaddvals = self.variables
        print(response.added())

        # For each required new value, loop through the list of added
        # variables, and check that their value matches the required
        # one.
        for newval in mustaddvals:
            # Loop through each newly added variable, and check whether
            # they match the required newval. If none match, return
            # False.
            # XXX: The string comparison here is a hack.
            if not any([str(response.new[name]) == newval for name in
                response.added()]):
                return False

        # If we exit the loop without failing, then we must've found all
        # of our requirements.
        return True

    def yaml_hook(self):
        if type(self.variables) == str:
            self.variables = self.variables.split(";")
