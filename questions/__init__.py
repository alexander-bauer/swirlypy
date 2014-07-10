import pkgutil

class NoQuestionInModuleException(Exception): pass

# Define a dict to add all of our finds to.
categories = {}

# Walk the directory.
for loader, name, ispkg in pkgutil.walk_packages(__path__):
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
