from swirlypy.question import CategoryQuestion

class MultipleChoiceQuestion(CategoryQuestion):
    def execute(self):
        self.print()
        correct = False
        while(not correct):
            response = self.get_response()
            correct = self.test_response(response)
            if(not correct):
                print(self.hint)

    def get_response(self):
        options = self.choices.split(";")
        # todo: randomize order of choices
        selection = ""
        while(selection == ""):
            n = 0
            for x in options:
                n += 1
                print(n, ": ", x)
            k = int(input("Select one of the numbered choices: "))-1
            # todo: try/catch integer; allow user to type string matching
            # one of the answers.
            if(k < 0 or k > n-1):
                selection=""
                print("Please type an integer between 1 and ", n)
            else:
                return(options[k])

    def test_response(self, response):
        '''This hard-coded test is a stub, awaiting plug-in tests'''
        return(response == self.correctanswer)


