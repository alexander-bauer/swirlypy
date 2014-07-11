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
    def __init__(self, new, old):
        self.new, self.old = new, old
        self.set_current, self.set_past = set(new.keys()), set(old.keys())
        self.intersect = self.set_current.intersection(self.set_past)
    def added(self):
        return self.set_current - self.intersect
    def removed(self):
        return self.set_past - self.intersect
    def changed(self):
        return set(o for o in self.intersect if self.old[o] != self.new[o])
    def unchanged(self):
        return set(o for o in self.intersect if self.old[o] == self.new[o])
