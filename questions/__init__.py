import pkgutil

class NoQuestionInModuleException(Exception): pass

# Define a dict to add all of our finds to.
categories = {}

def load(path):
    # Path needs to be a list in order for the following calls to work.
    if type(path) != list: path = [path]
    # Walk the directory.
    for loader, name, ispkg in pkgutil.walk_packages(path):
        module = loader.find_module(name).load_module(name)

        # Try to find the module's defined class, and add it to the
        # list.
        qname = name + "Question"
        try:
            if qname in dir(module):
                categories[qname.lower()] = module.__dict__[qname]
            else:
                raise NoQuestionInModuleException("No class %s" % qname)

        except Exception as e:
            print("Skipping module {}: {}".format(name, e))

# Load all of the questions in this path.
load(__path__)
