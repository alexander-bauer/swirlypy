#!/usr/bin/python3

import code as pycode

# DictDiffer code borrowed from StackOverflow:
# http://stackoverflow.com/a/1165552/1550074
class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)
    def added(self):
        return self.set_current - self.intersect 
    def removed(self):
        return self.set_past - self.intersect 
    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])


class PristineConsole:
    def __init__(self, locals, **kwargs):
        self.locals = locals
        self.kwargs = kwargs

    def run(self, codebuf):
        console = pycode.InteractiveConsole(locals = self.locals.copy(),
                **self.kwargs)
        for line in codebuf:
            console.push(line)

        return DictDiffer(console.locals, self.locals.copy())

pc = PristineConsole(locals())
dd = pc.run(["x = 10"])
print("x = 10")
print("Added:", dd.added())
print("Removed:", dd.removed())
print("Changed:", dd.changed())

dd = pc.run(["data = 11", "lst = [1, 2, 3]"])
print("x = 10")
print("Added:", dd.added())
print("Removed:", dd.removed())
print("Changed:", dd.changed())
