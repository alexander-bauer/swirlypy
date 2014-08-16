from swirlypy.question import CategoryQuestion
import swirlypy.colors as colors
import random

class MultipleChoiceQuestion(CategoryQuestion):
    """Presents a list of options in random order to the user to select
a correct ansewr from."""

    _required_ = ['choices', 'answer']

    def get_response(self, data={}):
        # Parse the options and shuffle them, for variety.
        options = self.choices
        random.shuffle(options)

        # Loop until the user selects the correct answer.
        while True:
            # Begin by printing the menu with numerical identifiers.
            for i, option in enumerate(options):
                colors.print_option("%d: %s" % (i+1, option))

            # Get the user's choice and try to return the relevant
            # answer, catching failures and restarting as appropriate.
            # Note that invalid input restarts the loop here, but an
            # incorrect answer will restart the loop outside of the
            # scope of the function. This allows for grading.
            # XXX: Try to match strings to choices, too.
            try:
                colors.print_inst("Select one of the numbered choices: ",
                        end="")
                choice = int(input())-1
                return options[choice]
            except (ValueError, IndexError):
                colors.print_help(
                    "Please pick an integer between 1 and %d" %
                    len(options))
                continue

    def test_response(self, response, data={}):
        """Check the response in the simplest way possible."""
        return response == self.answer

    def selftest(self, on_err, on_warn):
        if self.answer not in self.choices:
            on_err("answer \"%s\" not in available choices" % self.answer)
        if not self.test_response(self.answer):
            on_err("test_response fails with correct answer")

    def yaml_hook(self):
        """If `choices` is a string, split is on semicolon to form a
list."""
        if type(self.choices) == str:
            self.choices = self.choices.split(";")
