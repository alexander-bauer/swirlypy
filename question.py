#/usr/bin/python3
#
# This is another test of question classes.

import abc, yaml

class MissingQuestionFieldException(Exception): pass

# XXX: Add a __str__ method to represent the question in some way.
# XXX: Add some 'hint' capacity
# XXX: Provide an inbuilt capability to print errors or respond to
# incorrect user input.
class Question(object):
    """Question is an abstract class used to provide utilities for and
    embody a generic question to be asked in a course, which provides a
    prompt, or just text, request user response, and test it for
    correctness."""

    # Mark this class as an abstract.
    __metaclass__ = abc.ABCMeta

    def __init__(self, category, output, **kwargs):
        self.category = category
        self.output = output
        self.__dict__.update(kwargs)

    # Require that the given list of fields is present in the object's
    # dictionary. If any are not, a MissingQuestionField exception is
    # raised.
    def require(self, fields):
        # If only one field is given, treat it sanely by wrapping it in
        # a list.
        if fields == None: return True
        elif type(fields) != list: fields = [fields]

        for field in fields:
            if field not in self.__dict__:
                raise MissingQuestionFieldException(field)

        return True

    # Output in whatever format desired, defaults to self.output.
    # XXX: Could be much more advanced; automatically paginating, for
    # example.
    def print(self):
        print(self.output)

    @abc.abstractmethod
    def get_response(self):
        """Get user question response and returns it as an object that
        can be tested via test_response."""

    @abc.abstractmethod
    def test_response(self, response):
        """Test the user's response as returned by get_response,
        returning True if successful, and False if not."""

    def execute(self):
        """Execute the question in the default way, by first printing
        itself, then asking for a response and testing it in a loop
        until it is correct."""
        # XXX: Collect statistics here so that it can be used for
        # grading.

        # Print the output.
        self.print()

        # Loop until correct.
        while True:
            # Get the user's response.
            resp = self.get_response()

            # Test it. If correct (True), then break from this loop.
            if test_response(resp):
                break

    @classmethod
    def load_yaml(cls, file):
        """Tries to construct any number of Questions in the given YAML
        file by using yaml.safe_load. Dictionary keys are converted to
        lowercase."""
        # Try to load the YAML, minimizing code execution
        # vulnerabilities.
        y = yaml.safe_load(file)

        # Instantiate a list in which to return questions.
        questions = []

        for document in y:
            # First, lowercase keys in the given document.
            document = dict((k.lower(), v) for k, v in document.items())

            # Try to construct a class from the result (as **kwargs).
            # The __init__ method *should* ensure that the required
            # fields are present.
            questions.append(cls(**document))

        return questions
