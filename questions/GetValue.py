from swirlypy.question import ShellQuestion
import code, ast, sys

class GetValueQuestion(ShellQuestion):
    _required_ = [ "values" ]
    def get_response(self, data={}):
        """Interacts with the user until broken from, or reaches EOF.
        Each new expression, such as 'x**2', but unlike 'y = x**2', is
        captured and yielded to the caller."""
        console = self.new_console({})
        for value in console.interact(""):
            yield value

    def test_response(self, response, data={}):
        # Instead of matching if the response is None, disregard the
        # "submission."
        # XXX: Allow for matching values of None.
        if response == None:
            return None

        if type(self.values) == str:
            return response in self.values.split(";")
        else:
            return response == self.values

    def execute(self, data={}):
        self.print()

        # Loop until we get the correct answer.
        while True:
            # Get any values that the user generates, and pass them to
            # test_response.
            for value in self.get_response(data=data):
                tested = self.test_response(value, data=data)
                if tested == True:
                    return
                elif tested == False:
                    try:
                        print(self.hint)
                    except AttributeError:
                        pass

    def new_console(self, locals):
        """Creates a new console and recorder, and includes the recorder
        as __swirlypy_recorder__ in the new console."""
        # Create the new recorder.
        # XXX: This is also a bit hacky. The recorder should be handled
        # entirely by the VPC.
        self._recorder = Recorder()
        newlocals = locals.copy()
        newlocals["__swirlypy_recorder__"] = self._recorder
        return ValuePeekerConsole(newlocals)

class ValuePeekerConsole(code.InteractiveConsole):
    """Allows the user to interact with a console, and yields each value
    that their code results in. For example, entering the interact()
    loop will allow the user to run arbitrary code in their environment,
    until they input something that returns a value on the terminal,
    such as '256**2'. The result of this value is then yielded to the
    caller."""

    class RecorderCorruptedException(Exception): pass

    @staticmethod
    def compile_ast(source, filename = "<input>", symbol = "single"):
        # Due to the nature of code's compile_command, we need to ask it
        # to compile the user's command first. If successful, then we
        # need to recompile it for ourselves, adding the appropriate
        # hooks. If it fails, then we'll allow that to be indicated.
        precompiled = code.compile_command(source, filename, symbol)

        # If the command succeeded, as indicated by its object not being
        # None, and no exception having occurred, parse it with AST.
        if precompiled != None:
            parsed = ast.parse(source, filename, symbol)

            # Find all of the expressions that we want to capture in the
            # tree, and wrap them in a __swirlypy_record__.record()
            # call.
            CaptureExprs().visit(parsed)

            # Compile the command in a standard way and return it.
            return compile(parsed, filename, symbol)

    def interact(self, banner=None):
        """Interact with the user until they produce a raw value in the
        console (such as '256**2'), and then yield the result. Will
        resume if run as a generator.

        If an EOFError is raised, it will exit with no return value."""

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
            # Keep track of the number of value recorded. If it goes up,
            # then extract those results and yield them. If it's not
            # present, fail.
            try:
                numrecorded = len(self.locals["__swirlypy_recorder__"])
            except KeyError:
                raise self.RecorderCorruptedException()

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

                    # Check to see if any more values have been
                    # recorded. If so, yield them.
                    try:
                        newnumrecorded = \
                                len(self.locals["__swirlypy_recorder__"])

                        if newnumrecorded > numrecorded:
                            # We need to yield them one at a time.
                            for value in \
                                    self.locals["__swirlypy_recorder__"]\
                                    [numrecorded:newnumrecorded]:
                                    yield value
                    except KeyError:
                        raise self.RecorderCorruptedException()

            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0

class CaptureExprs(ast.NodeTransformer):
    def visit_Expr(self, node):
        newnode = ast.copy_location(ast.Expr(value = ast.Call(func =
            ast.Attribute(value = ast.Name(id='__swirlypy_recorder__',
                ctx=ast.Load()), attr="record", ctx=ast.Load()),
            args=[node.value], keywords=[], starargs=None,
            kwargs=None)), node)
        ast.fix_missing_locations(newnode)
        return newnode

class Recorder(list):
    def record(self, value):
        """Appends the given value to the interal list, and returns the
        same value."""
        self.append(value)
        return value
