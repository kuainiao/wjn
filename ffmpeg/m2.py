# -*- coding: utf-8 -*- #
import pythoncom
import pyHook

def onMouseEvent(event):
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Position:", event.Position
    where=event.Position
    print where
    x=where[0]
    y=where[1]
    print x+y
    print"---"
    return True
def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()