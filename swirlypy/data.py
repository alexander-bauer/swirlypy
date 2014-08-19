import os
import yaml

class Data(dict):

    class ImmutableError(Exception): pass

    methods = { "yaml": yaml.safe_load }

    def __init__(self, directory):
        self.dir = directory
        self.loaded = {}

    def __getitem__(self, key):
        if key not in self.loaded:
            self.loaded[key] = self.load(key)

        return self.loaded[key]

    def __setitem__(self, key, value):
        raise type(self).ImmutableError("class is immutable")
            
    def load(self, key):
        # Try to find a supported filetype (identified by extension).
        for filetype, loadfunc in type(self).methods.items():
            path = os.path.join(self.dir, "%s.%s" % (key, filetype))
            if os.path.isfile(path):
                with open(path, "rb") as f:
                    return loadfunc(f)

        # If we exit the loop with no success, throw a key error.
        raise KeyError(key)
