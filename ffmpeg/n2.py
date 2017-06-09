#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pythoncom
import pyHook
import time

def onMouseEvent(event):
    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Position:%s\n" % str(event.Position))
    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
    return True
if __name__ == "__main__":
    file_name = "E:\gitdb\hook.txt"
    fobj = open(file_name, 'w')
    hm = pyHook.HookManager()

    hm.MouseAll = onMouseEvent
    hm.HookMouse()

    pythoncom.PumpMessages()

    fobj.close()