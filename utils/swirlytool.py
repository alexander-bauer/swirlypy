#!/usr/bin/env python3

# swirlytool is the primary Swirlypy user interface tool, which is
# responsible for the running, creation, and inspection of Swirlypy
# courses.

import sys, argparse

try:
    # XXX: We should be able to just import swirlypy here. We need to
    # set __all__ in the __init__.py of the main module.
    import swirlypy.course
except ImportError:
    print("Can't import swirlypy. Is it in your PYTHONPATH?")
    sys.exit(1)

def load_course(path):
    """Helper function for subcommands which need to load courses
    predictably."""
    # Try to load the course.
    try:
        return swirlypy.course.Course.load(path)
    except FileNotFoundError as e:
        print(e)
        print("Couldn't load course; does it have course.yaml?")
        return None

def run(args):
    """Run a swirlypy course, packaged or raw."""
    course = load_course(args.course_path)
    if not course:
        return 1

    # If successful, print its description and execute it.
    course.print()
    course.execute()

def info(args):
    """Print verbose information about a course, packaged or raw."""
    course = load_course(args.course_path)
    if not course:
        return 1

    # If successful, print its description, and some other data about
    # it: including...
    course.print()

    # Whether the course is packaged in a pretty format or not.
    print("Course is", "" if course.packaged else "not", "packaged")

def main(args):
    # If the subcommand is known and registered, pass it the arguments
    # and let it run.
    try:
        args.func(args)
    except AttributeError as e:
        print(e)
        parser.print_usage()

def parse(args):
    global parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")
    run_command = subparsers.add_parser("run", help="run a course from \
            a local file")
    run_command.add_argument("course_path", help="directory of or path \
        to directory containing course.yaml file")
    run_command.set_defaults(func=run)
    info_command = subparsers.add_parser("info", help=info.__doc__)
    info_command.add_argument("course_path", help="directory of or path \
        to directory containing course.yaml file")
    info_command.set_defaults(func=info)
    return parser.parse_args(args)

if __name__ == "__main__":
    sys.exit(main(parse(sys.argv[1:])))
