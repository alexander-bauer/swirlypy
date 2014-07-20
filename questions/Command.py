from swirlypy.question import ShellQuestion
import code, ast, sys

class CommandQuestion(ShellQuestion):
    _required_ = [ "answer" ]
    def get_response(self, data={}):
        """Interacts with the user until broken from, or reaches EOF.
        Each new command that the user enters is captured and yielded to
        the caller."""
        console = self.new_console({})
        for value in console.interact(self.output):
            yield value

    def test_response(self, response, data={}):
        # Parse the provided correct answer in the same way it's parsed
        # by the CommandReturnerConsole.
        answer_tree = ast.parse(self.answer, filename="<answer>", \
                mode="single")

        # Now, we have to test their string dumps, because otherwise
        # it will resort to reference equality.
        # XXX: Find a more elegant way to do this.
        return ast.dump(answer_tree) == ast.dump(response)

    def execute(self, data={}):
        # Don't print the output. That gets handled by the console.

        # Loop until we get the correct answer.
        while True:
            # Get any values that the user generates, and pass them to
            # test_response.
            for value in self.get_response(data=data):
                if self.test_response(value, data=data):
                    return
                else:
                    try:
                        print(self.hint)
                    except AttributeError:
                        pass

    def new_console(self, locals):
        """Creates a new CommandReturnerConsole."""
        return CommandReturnerConsole({})

class CommandReturnerConsole(code.InteractiveConsole):
    """Allows the user to interact with a console, and yields every
    command that they type in as an AST."""

    def compile_ast(self, source, filename = "<input>", symbol = "single"):
        # Here, we try to compile the relevant code. It may throw an
        # exception indicating that the command is not complete, in
        # which case we cannot proceed, but a full command will be
        # supplied eventually.
        compiled = code.compile_command(source, filename, symbol)

        # If the compilation succeeded, as indicated by its object not being
        # None, and no exception having occurred, parse it with AST and
        # store that.
        if compiled != None:
            self.latest_parsed = ast.parse(source, filename, symbol)

        return compiled

    def interact(self, banner=None):
        """Interacts with the user. Each time a complete command is
        entered, it is parsed using AST and yielded."""

        # XXX: This is a hack to override parent precedence. This needs
        # to be fixed in a better way.
        self.compile = self.compile_ast

        # Borrow a block of code from code.InteractiveConsole
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = ">>> "
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = "... "
        cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
        if banner is None:
            self.write("Python %s on %s\n%s\n(%s)\n" %
                       (sys.version, sys.platform, cprt,
                        self.__class__.__name__))
        elif banner:
            self.write("%s\n" % str(banner))
        more = 0
        while 1:
            # Reset the value of latest_parsed.
            self.latest_parsed = None

            try:
                if more:
                    prompt = sys.ps2
                else:
                    prompt = sys.ps1
                try:
                    line = self.raw_input(prompt)
                except EOFError:
                    self.write("\n")
                    break
                else:
                    more = self.push(line)

                    # Check to see if a new value has been parsed yet.
                    # If so, yield it.
                    if self.latest_parsed != None:
                        yield self.latest_parsed

            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0
