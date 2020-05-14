#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sample PyQt5 app to demonstrate keybinder capabilities."""

import sys

# Testing imports
import pprint as pp
import xmltodict as xmltodict
import xml.etree.ElementTree as ET

from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import QAbstractNativeEventFilter, QAbstractEventDispatcher
from PyQt5.QtWidgets import QMainWindow

from pyqtkeybind import keybinder

from os import system

latch = False
system("title "+ "PopUp")
profilePathList = list


class ImportProfile(profilePathList):
    """ Imports a list of predefined profiles """
    def __init__(self):
        super().__init__()

    def scrapeall(self, profileList):
        # Keyboards keybindings are found in tester['cereal']['value0']['profile']['properties']['value2']
        # further, the location of the kegbindins are
        # print(tester['cereal']['value0']['profile']['properties']['value2']['value']['properties']['value11']['ptr_wrapper']) # location of the keybindings start.

        # Dic Where KEY: is the key pressed and VALUE: is the bound keys
        rootContainer = list()

        # Dict of Dicts where KEY: is the name of the profile and VALUE is the profileKeybindings
        keybindDict = dict

        for value in profileList:
            root = ET.parse(value).getroot()
            rootContainer.append(root)

            # pp.pprint(root)

        # A list of multi key button presses (ie: shortcuts)
        keybindings = dict()
        # Once a full sequence of shortcuts are found, we append them to a list
        keysetList = dict()
        # Bound Key: the key pressed to execute the shortcuts. Order should follow the same order.
        # Bound Mouse Mode: Click, LongPress, etc..
        boundKeys = dict()
        boundKeyMode = dict()
        # Bound Mouse Buttons: The key pressed to execute the shortcuts
        # Bound Mouse Mode: Click, LongPress, etc..
        boundMouse = dict()
        boundMouseMode = dict()
        # Attempt to attempt to look ahead to find correct bound keys
        timestop = False
        mode = False

        # Search through xml for KeyStokes and Save into a list of list
        # Top list contains each list of keystrokes
        for root in rootContainer:
            parent_map = {c: p for p in root.iter() for c in p}
            # print(list(parent_map))

            # Find the location of keyStroke's ancestor, We use the ancestor to navigate the keybindings.
            for parent in root.findall('.//keyStroke/../../../..'):
                boundSet = 0
                # drop into the child of the parent.
                for child in parent:

                    # print("Child Tag: " + child.tag)
                    keyStrokeChild = child.find('ptr_wrapper/data/keyStroke')
                    keyNameChild = child.find('ptr_wrapper/data/keyName')
                    keyBound = child.find('.//second/..')
                    # print(keyBound)
                    # print(keyStrokeChild)

                    if keyNameChild is not None:
                        if keyNameChild.text is not None:
                            # pass
                            print('This should be a non empty Key: ' + keyNameChild.text)
                            keysetList.update({boundSet : keyNameChild.text})

                    if keyStrokeChild is not None:
                        if keyStrokeChild.text is not None:
                            print('This Should be a list of Key Strokes: ')
                            strokeContainer = None
                            for value in keyStrokeChild:
                                if strokeContainer is None:
                                    strokeContainer = value.text
                                else:
                                    strokeContainer = strokeContainer + ', ' + value.text
                                    keysetList.update({boundSet : strokeContainer})
                                # print(value.text)
                            print(strokeContainer)

                    if keyBound is not None:
                        # print(keyBound.find('first').text)
                        if keyBound.find('first') is not None:
                            print('test')
                            print(keyBound.find('first').text)
                            boundKeys.update({boundSet: keyBound.find('first').text})
                            print(keyBound.find('second').text)
                            boundKeyMode.update({boundSet: keyBound.find('second').text})
                    boundSet += 1

        pp.pprint(keysetList)
        # pp.pprint(keybindings)
        pp.pprint(boundKeys)
        pp.pprint(boundKeyMode)
            #
            #         if child.tag == 'base':
            #             if child.find('name').text is not None:
            #                 print(child.find('name').text)
            #                 if parent.find('keyName').text is not None:
            #                     print('=======================')
            #                     print('This should be a non empty key: ' + parent.find('keyName').text)
            #                     print('=======================')
            #                 elif parent.find('keyStroke').text is not None:
            #                     print('=======================')
            #                     for value in parent.find('keyStroke'):
            #                         print('This should be a non empty string of key strokes: ' + value.text)
            #                     print('=======================')
            #         # pp.pprint(child.text)
            #
            # for ptr in root.iter('keyStroke'):
            #     # print(ptr.getchildren())
            #     # if ptr.getchildren() == []:
            #         # print(ptr) # TODO Need to figure out how to walk back if this value is empty we need to check keyName
            #     for value in ptr:
            #         if value is not None:
            #             # print(value.text)
            #             keybindings.append(value.text)
            #     if ptr.find('value0') is not None:
            #         keysetList.append(keybindings.copy())
            #         keybindings.clear()
            #
            # for assignedKey in root.findall('.//second'):
            #     if assignedKey is not None:
            #         for value in assignedKey:
            #             if value.tag == 'second' or value.tag == 'first':
            #                 val = value.text
            #                 if val[:5] == 'Mouse':
            #                     timestop = True
            #                 elif val[:1] == 'M':
            #                     timestop = True
            #                 elif val[:3] == 'Win':
            #                     timestop = True
            #                 elif val[:3] == 'Hea':
            #                     timestop = True
            #                 elif val[:5] =='Brigh':
            #                     timestop = True
            #                 elif val[:4] == 'Key_':
            #                     timestop = True
            #                 else:
            #                     if not timestop:
            #                         if not mode:
            #                             boundKeys.append(val)
            #                             mode = True
            #                         else:
            #                             boundKeyMode.append(val)
            #                             mode = False
            #                     timestop = False
            #                     # Stopped here, TODO: finish bound key finding and futur proof for mouse, headset, trash the rest?
            #
            # for type_tag in root.findall('ptr_wrapper'):
            #     name = type_tag.find('id').text
            #     print("Test" + name)

        pp.pprint("==================================")
        pp.pprint(keysetList)
        pp.pprint("==================================")
        # pp.pprint(keybindings)
        print()
        pp.pprint("==================================")
        pp.pprint(boundKeys)
        pp.pprint("==================================")
        print()
        pp.pprint("==================================")
        pp.pprint(boundKeyMode)
        pp.pprint("==================================")

        # for assignedKey in root.iter('second'):
        #     print(len(assignedKey))
        # for value in assignedKey:
        #     if value.text == 'first':
        #     print('-------------------------------')
        #     print(value.text)
        #     print('-------------------------------')
        # if len(assignedKey) == 0:
        #     print(assignedKey.text)
        # if ptr.find('value0').text:
        #     print("testing Text")
        #     pp.pprint(ptr.get('value').text)
        # end test


    # def scrapeICUE(self):
    #     pass

    # def xmltodict(self):
    #     """ Returns the xml as a dict"""
    #     with open('C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\Profiles\\Main.cueprofile') as fd:
    #         return xmltodict.parse(fd.read())


class WinEventFilter(QAbstractNativeEventFilter):
    def __init__(self, keybinder):
        self.keybinder = keybinder
        super().__init__()

    def nativeEventFilter(self, eventType, message):
        ret = self.keybinder.handler(eventType, message)
        return ret, 0


class SecondWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = uic.loadUi("C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\ui\\keyboard.ui")

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )

    def mousePressEvent(self, a0) -> None:
        global latch
        self.hide()
        latch = True


class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 32),
                QtWidgets.qApp.desktop().availableGeometry()
            ))


def main():
    app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    window = SecondWindow()

    print("Sample app for pyqtkeybind:")
    print("\tPress Ctrl+Shift+A any where to trigger a callback.")
    print("\tCtrl+Shift+F unregisters and re-registers previous callback.")
    print("\tCtrl+Shift+E exits the app.")

    test = ImportProfile()
    profileList = ['C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\Profiles\\Main.cueprofile']
    test.scrapeall(profileList)

    # Setup a global keyboard shortcut to print "Hello World" on pressing
    # the shortcut
    keybinder.init()
    unregistered = False

    def on_toggle():

        global latch
        nonlocal window

        if latch:
            window.show()
            latch = False
            print("worked On")
        else:
            window.hide()
            latch = True
            print("worked Off")

    def exit_app():
        window.close()

    def unregister():
        keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+A")
        print("unregister and register previous binding")
        keybinder.register_hotkey(window.winId(), "Shift+Ctrl+A", on_toggle)

    keybinder.register_hotkey(window.winId(), "Shift+Ctrl+A", on_toggle)
    keybinder.register_hotkey(window.winId(), "Shift+Ctrl+E", exit_app)
    keybinder.register_hotkey(window.winId(), "Shift+Ctrl+F", unregister)

    # Install a native event filter to receive events from the OS
    win_event_filter = WinEventFilter(keybinder)
    event_dispatcher = QAbstractEventDispatcher.instance()
    event_dispatcher.installNativeEventFilter(win_event_filter)

    window.show()
    app.exec_()
    keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+A")
    keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+F")
    keybinder.unregister_hotkey(window.winId(), "Shift+Ctrl+E")


if __name__ == '__main__':
    main()
