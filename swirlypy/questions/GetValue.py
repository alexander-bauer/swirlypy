from swirlypy.questions.Recording import RecordingQuestion
import code, ast, sys

class GetValueQuestion(RecordingQuestion):
    """Presents the user with a shell, and captures every line of input
which results in a value being computed, and specifically not captured
in a variable. If the value captured matches the stored correct value,
then the question is marked correct."""
    
    _required_ = [ "value" ]

    def test_response(self, response, data={}):
        # Instead of matching if the response is None, disregard the
        # "submission."
        # XXX: Allow for matching values of None.
        if response == None:
            return None
        # Note that response["values"] will always be of type Recorder
        # (a subclass of list).  For now, the response will be
        # considered correct if and only if some member of
        # response["values"] equals self.values.
        return self.value in response["values"]

    def yaml_hook(self):
        """If converted from YAML, perform the following
transformations:
        
- If given, use the `type` attribute to convert `value` to that type. If
  `value` is a list, then use it as `*args` to the type."""
        # If type is present, use 'value' to construct the type.
        if hasattr(self, "type"):
            # Try to evaluate the type as a builtin.
            # XXX: This only supports builtings.
            if hasattr(__builtins__, self.type):
                newtype = getattr(__builtins__, self.type)
                if type(self.value) == list:
                    self.value = newtype(**self.value)
                else:
                    self.value = newtype(self.value)
