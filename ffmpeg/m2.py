#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import pythoncom
import pyHook

def onMouseEvent(event):
    if "mouse left" in event.MessageName:
        print "MessageName:", event.MessageName
        print "WindowName:", event.WindowName
        print "Position:", event.Position
        where=event.Position
        print where
        x=where[0]
        y=where[1]
        print x+y
    return True
def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()