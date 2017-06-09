#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import pythoncom
import pyHook

a1=0
b1=0
l=1500
h=850
left=(a1,b1)
vlist0=('v1.mp4','v2.mp4')
vlist1=('v3.mp4','v4.mp4')

def onMouseEvent(event):
    if "mouse left" in event.MessageName:
        print '----------------'
        print "MessageName:", event.MessageName
        print "WindowName:", event.WindowName
        print "Position:", event.Position
        where=event.Position
        # print where
        x=where[0]
        y=where[1]
        l1=l/2
        h1=h/2
        x1=(x-a1)/l1
        y1=(y-b1)/h1
        print x1,y1
        if y1==0 :
            print vlist0[x1]
        elif y1==1 :
            print vlist1[x1]


    return True
def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()