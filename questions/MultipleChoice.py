from swirlypy.question import CategoryQuestion
import random

class MultipleChoiceQuestion(CategoryQuestion):

    _required_ = ['choices', 'correctanswer']

    def get_response(self, data={}):
        # Parse the options and shuffle them, for variety.
        options = self.choices.split(";")
        random.shuffle(options)

        # Loop until the user selects the correct answer.
        while True:
            # Begin by printing the menu with numerical identifiers.
            for i, option in enumerate(options):
                self.print_option("%d: %s" % (i+1, option))

            # Get the user's choice and try to return the relevant
            # answer, catching failures and restarting as appropriate.
            # Note that invalid input restarts the loop here, but an
            # incorrect answer will restart the loop outside of the
            # scope of the function. This allows for grading.
            # XXX: Try to match strings to choices, too.
            try:
                self.print_inst("Select one of the numbered choices: ",
                        end="")
                choice = int(input())-1
                return options[choice]
            except (ValueError, IndexError):
                self.print_help(
                    "Please pick an integer between 1 and %d" %
                    len(options))
                continue

    def test_response(self, response, data={}):
        """Check the response in the simplest way possible."""
        return response == self.correctanswer
