# Set up the ansi escape codes.

import sys

class UnknownANSICodeException(Exception): pass

class ANSI:
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = \
            ("\033[%dm" % n for n in range(30, 38))

    RESET = "\033[0m"
    BOLD = "\033[1m"

class color(object):
    """Decorator for colorize the input to a function based on the given
    ansispec. It assumes that the first argument to the decorated
    function is a string which should be wrapped in ANSI codes. The
    ansispec format is 'component0;component1;...', where each component
    is a class member of ANSI. They are case-insensitive."""

    def __init__(self, ansispec):
        self.ansi = interpret_ansispec(ansispec)

    def wrap_color(self, f, *args, **kwargs):
        newstr = "%s%s%s" % (self.ansi, args[0], ANSI.RESET)

        return f(newstr, *args[1:], **kwargs)

    def __call__(self, f):
        def wrap_color(*args, **kwargs):
            newstr = "%s%s%s" % (self.ansi, args[0], ANSI.RESET)
            return f(newstr, *args[1:], **kwargs)

        return wrap_color

def colorize(string, ansispec):
    if not sys.stdout.isatty():
        return string
    ansi = interpret_ansispec(ansispec)
    return "%s%s%s" % (ansi, string, ANSI.RESET)

def interpret_ansispec(spec):
    ansi = ""

    # Split up the spec by semicolon, and then append the ANSI code
    # matching the string.
    for component in spec.split(";"):
        component = component.upper()
        if hasattr(ANSI, component):
            ansi += ANSI.__dict__[component]
        else:
            raise UnknownANSICodeException(component)

    return ansi

def print_inst(string, **kwargs):
    print(string, **kwargs)

def print_question(string, **kwargs):
    print(colorize(string, "bold;blue"), **kwargs)

def print_option(string, **kwargs):
    print(colorize(string, "magenta"), **kwargs)

def print_help(string, **kwargs):
    print(colorize(string, "blue"), **kwargs)

def print_warn(string, **kwargs):
    print(colorize("WARNING: %s" % string, "yellow"), **kwargs)

def print_err(string, **kwargs):
    print(colorize("ERROR: %s" % string, "bold;red"), **kwargs)
