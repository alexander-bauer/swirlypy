#!/usr/bin/python3

import code as pycode

class CallbackConsole(pycode.InteractiveConsole):
    # Take a callback function to call every time a new line is
    # executed.
    def __init__(self, callback, **kwargs):
        self.callback = callback
        super().__init__(kwargs)

    def runcode(self, code):
        super().runcode(code)
        if self.callback:
            self.callback(self, code)

def echoback(self, code):
    print(self.locals)

def hookvar(self, code):
    if "hook_count" in self.locals:
        self.locals["hook_count"] += 1
    else:
        self.locals["hook_count"] = 1

def showbuf(self, code):
    print(self.buffer)

cc = CallbackConsole(showbuf)
cc.interact()
