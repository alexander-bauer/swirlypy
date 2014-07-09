#/usr/bin/python3
#
# This is another test of question classes.

class MissingQuestionFieldException(Exception): pass

class Question(object):
    def __init__(self, qtype, output, **kwargs):
        self.qtype = qtype
        self.output = output
        self.__dict__ = kwargs

    # Require that the given list of fields is present in the object's
    # dictionary. If any are not, a MissingQuestionField exception is
    # raised.
    def require(self, fields):
        # If only one field is given, treat it sanely by wrapping it in
        # a list.
        if type(fields) != list: fields = [fields]

        for field in fields:
            if field not in self.__dict__:
                raise MissingQuestionFieldException(field)

        return True
