# Define exceptions to be used.
class MissingFieldException(Exception):
    """Is thrown when a Course or Question requires metadata fields that
    have not been provided."""
    pass

class UnknownQuestionCategoryException(Exception): pass
class NoCoursePresentException(Exception): pass
class NoSuchLessonException(Exception): pass
