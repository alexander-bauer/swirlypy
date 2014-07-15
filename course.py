import yaml
import swirlypy.slug
import swirlypy.lesson
import os

class NoCoursePresentException(Exception): pass
class NoSuchLessonException(Exception): pass

class Course:
    """Course is a concrete representation of a collection of lessons
    in one coherent unit."""

    def __init__(self, course, lessons, author, version, coursedir,
            **kwargs):
        self.course = course
        self.lessonnames = lessons.split(";")
        self.author = author
        self.description = ""
        self.version = version
        self.coursedir = coursedir
        self.__dict__.update(kwargs)

    def print(self):
        """Prints a textual representation of the course, including
        name, author, and description, if available."""
        print("%s by %s: %s" % (self.course, self.author,
            self.description))

    def menu(self):
        """Prints a menu containing all of the lessons in the course,
        along with their index."""
        for index, lesson in enumerate(self.lessonnames):
            print("%d: %s" % (index + 1, lesson))

    def execute(self):
        """Repeatedly prompts the user for lessons to run until
        explictly exited."""

        # Loop until user EOF.
        while True:
            # Present the menu.
            self.menu()
            try:
                identifier = input("Selection: ").strip()
                self.execute_lesson(identifier)
            except NoSuchLessonException:
                print("No lesson: %s" % identifier)
            except EOFError:
                # If the user hits CTRL-D, exit.
                # XXX: Tell the user this.
                print()
                print("Bye!")
                break

    def execute_lesson(self, identifier):
        """Executes a lesson based on a given identifier. This can be
        either an index (one-based) or a string matching a lesson name.
        If none can be found, it throws a NoSuchLessonException."""

        # Create an empty lesson name to refer to.
        lessonname = ""

        # Try to convert the identifier to an integer, failing silently
        # if it is not.
        try:
            identifier = int(identifier)
        except ValueError:
            pass

        # If it's an index, use it directly.
        if type(identifier) == int:
            try:
                lessonname = self.lessonnames[identifier - 1]
            except IndexError:
                raise NoSuchLessonException("Invalid lesson index")
        else:
            # If it's not an index, look it up, and then use the
            # resultant index.
            try:
                lessonname = self.lessonnames[
                        self.lessonnames.index(identifier)]
            except ValueError:
                raise NoSuchLessonException("Invalid lesson: %s" %
                        identifier)

        # We can construct the path that the lesson should be available
        # at by combining the coursedir, "lessons", and the slugified
        # lesson name.
        lessonpath = os.path.join(self.coursedir, "lessons",
                swirlypy.slug.slugify(lessonname) + ".yaml")

        # Open the lesson and parse it from YAML.
        with open(lessonpath, "r") as f:
            lesson = swirlypy.lesson.Lesson.load_yaml(f)

        # Execute it.
        data = lesson.execute()

        # Print a seperator to show it's complete.
        print()
        print("Lesson %s complete!" % lessonname)

    # XXX: Decide on and document the hardcoded course.yaml file here.
    @classmethod
    def load(cls, coursedir):
        """Loads a whole Course from the given course directory."""
        # Open the relevant file, and pass the rest to load_yaml.
        with open(os.path.join(coursedir, "course.yaml"), "r") as f:
            course = cls.load_yaml(f, coursedir)

            # Fill in some metadata here.
            course.packaged = False

            # Finally, return it.
            return course

    @classmethod
    def load_yaml(cls, file, coursedir):
        """Tries to construct a Course object from the first element in
        a given YAML file using yaml.safe_load. Dictionary keys are
        converted to lowercase."""
        # Load the YAML.
        y = yaml.safe_load(file)

        # Ensure that the first element exists. This should allow us to
        # safely access y[0].
        if len(y) < 1: raise NoCoursePresentException()

        # Lowercase all of the keys so that we can use it in the
        # constructor.
        document = dict((k.lower(), v) for k, v in y[0].items())

        # Construct a Course and return it.
        return cls(coursedir = coursedir, **document)
