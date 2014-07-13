#!/usr/bin/env python3

import sys, argparse
import swirlypy.course

def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("course_path", help="directory of or path to \
            course.yaml file")
    parser.add_argument("--info", "-i", action="store_true",
            help="show course information")
    return parser.parse_args(args)

def main(args):
    course = swirlypy.course.Course.load(args.course_path)

    # If --info is supplied, only print metadata.
    # XXX: We should add more fields so that we can be verbose here.
    if args.info:
        course.print()
    else:
        course.print()
        course.execute()

if __name__ == "__main__":
    main(parse(sys.argv[1:]))
