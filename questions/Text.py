from swirlypy.question import CategoryQuestion

class TextQuestion(CategoryQuestion):
    def execute(self, data={}):
        self.print()
        self.get_response()

    def get_response(self, data={}):
        x=input('...')

    def selftest(self, on_err, on_warn):
        # Technically, we can print anything, but it's unlikely that
        # things other than strings will be meaningful.
        if type(self.output) != str:
            on_warn("Output is %s, not str: %s" % (type(self.output),
                self.output))
