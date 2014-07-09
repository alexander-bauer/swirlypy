#!/usr/bin/python3

# This approach, modeled after R swirl's, strikes me as crufty.
# All that's really needed are three user input methods: input("yada yada: "),
# choose from a list (y|n, etc), and capture input from >>>.

import yaml, abc

class DemoBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, details):
        self.detail = details
        self.ptr = 0
        self.stack = [presentText, getResponse, testResponse]
        self.finished = False

    def nextOp(self):
        if finished:
            return False
        else:
            stack[ptr]()
            return(finished)

    def presentText(self):
        print(details["Output"])
        ptr += 1

    @abc.abstractmethod
    def getResponse(self):
        """Gets user response in any number of ways."""

    def testResponse(self):
        """A dummy for now."""
        finished = True


class text(DemoBase):

    def getResponse(self):
        output("Type enter to proceed...")
        ptr = 0
        finished = True

class mult_question(DemoBase):

    def getResponse(self):
        choices = details["AnswerChoices"].split(";")
        n = 0
        choice = ""
        while(choice == ""):
            for x in choices:
                n += 1
                print(n, ": ", x)
            k = input("Select one of the numbered choices: ")    
            # todo: check for integer
            if(k < 0 or k > n):
                choice=""
            else:
                self.choice = choice
        ptr += 1
        finished = False # Must test answer


