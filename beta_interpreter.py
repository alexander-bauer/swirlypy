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
            self.callback(code)

def echoback(code):
    print(code)

cc = CallbackConsole(echoback)
cc.interact()
