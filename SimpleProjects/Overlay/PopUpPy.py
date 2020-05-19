#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sample PyQt5 app to demonstrate keybinder capabilities."""
import os
import sys

# Testing imports
import pprint as pp
import xmltodict as xmltodict
import xml.etree.ElementTree as ET

from PyQt5 import QtWidgets, QtCore, uic, QtGui
from PyQt5.QtCore import QAbstractNativeEventFilter, QAbstractEventDispatcher
from PyQt5.QtWidgets import QMainWindow, QPushButton, QSizePolicy

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

        # Key connections: key shortcut, key bound, modifier [click, longpress]
        keyCons = list()
        # Key connection page: each value is a new
        keyConPage = list()

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
            # parent_map = {c: p for p in root.iter() for c in p}
            # print(list(parent_map))

            # Find the location of keyStroke's ancestor, We use the ancestor to navigate the keybindings.
            boundSet = 0
            profileName = root.find('.//name')

            for parent in root.findall('.//keyStroke/../../../..'):

                # drop into the child of the parent.
                for child in parent:

                    # print("Child Tag: " + child.tag)
                    nameTag = child.find('ptr_wrapper/data/base/name')
                    keyStrokeChild = child.find('ptr_wrapper/data/keyStroke')
                    keyNameChild = child.find('ptr_wrapper/data/keyName')
                    keyBound = child.find('.//second/..')
                    strokeContainer = None
                    # print(keyBound)
                    # print(keyStrokeChild)

                    if nameTag is not None:
                        if nameTag.text is not None:
                            if strokeContainer is None:
                                strokeContainer = nameTag.text
                            else:
                                strokeContainer = strokeContainer + ', ' + nameTag.text
                            # print(nameTag.text)

                    if keyNameChild is not None:
                        if keyNameChild.text is not None:
                            # pass
                            # print('This should be a non empty Key: ' + keyNameChild.text)
                            keysetList.update({boundSet: keyNameChild.text})
                            if strokeContainer is None:
                                strokeContainer = keyNameChild.text
                            else:
                                strokeContainer = strokeContainer + ', ' + keyNameChild.text

                    if keyStrokeChild is not None:
                        if keyStrokeChild.text is not None:
                            # print('This Should be a list of Key Strokes: ')
                            for value in keyStrokeChild:
                                if strokeContainer is None:
                                    strokeContainer = value.text
                                else:
                                    strokeContainer = strokeContainer + ', ' + value.text
                                # print(value.text)
                            # print(strokeContainer)
                            keysetList.update({boundSet: strokeContainer})

                    if keyBound is not None:
                        # print(keyBound.find('first').text)
                        if keyBound.find('first') is not None:
                            # print('test')
                            # print(keyBound.find('first').text)
                            # print(keyBound.find('second').text)

                            boundKeyMode.update({boundSet: keyBound.find('second').text})
                            boundKeys.update({boundSet: keyBound.find('first').text})

                            if strokeContainer is None:
                                strokeContainer = keyBound.find('first').text
                                strokeContainer = strokeContainer + ', ' + keyBound.find('second').text
                            else:
                                strokeContainer = strokeContainer + ', ' + keyBound.find('first').text
                                strokeContainer = strokeContainer + ', ' + keyBound.find('second').text

                            boundSet += 1

                    # print(strokeContainer)
                    keyCons.append(strokeContainer)
            keyCons.append(profileName)
            keyConPage.append(keyCons.copy())
            keyCons = list()

        # for page in keyConPage:
        #     print(len(keyConPage))
        #     print("NEW PAGE: ")
        #     section = 1
        #     for part in page:
        #         if section == 1:
        #             print('Part 1, Name and ShortCut: ' + part)
        #             section = 2
        #         else:
        #             print('Part 2, BoundKey and Modifier: ' + part)
        #             section = 1

        return keyConPage


class WinEventFilter(QAbstractNativeEventFilter):
    def __init__(self, keybinder):
        self.keybinder = keybinder
        super().__init__()

    def nativeEventFilter(self, eventType, message):
        ret = self.keybinder.handler(eventType, message)
        return ret, 0

pageHolder = dict()
class SecondWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = uic.loadUi("C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\ui\\keyboard.ui")

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )

        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(400, 400),
                QtWidgets.qApp.desktop().availableGeometry()
            ))
        self.setStyleSheet("""QToolTip { 
                                   background-color: black; 
                                   color: white; 
                                   border: black solid 1px
                                   }""")

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        profileList = listifyFolderFiles(os.path.expandvars(r'%APPDATA%\Corsair\CUE\profiles'))
        DATA = ImportProfile()

        # profileList = ['C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\Profiles\\MainNew.cueprofile',
        #                'C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\Profiles\\PyCharm.cueprofile']
        # profileList = ['C:\\Dev\\Python-Education\\SimpleProjects\\Overlay\\Profiles\\PyCharm.cueprofile']
        shortcutsParsed = DATA.scrapeall(profileList)
        newButton = None
        pagehold = 0
        buttonList = list()
        global pageHolder
        nameHolder = list()

        for page in shortcutsParsed:
            # print(len(shortcutsParsed))
            # print("NEW PAGE: ")
            section = 1
            shortcutCounter = 0
            x = 20
            y = 20
            profileName = page.pop(-1)
            nameHolder.append(profileName.text)
            print(profileName.text)

            for part in page:

                if section == 1:
                    # print('Part 1, Name and ShortCut: ' + part)
                    shortcutName, shortcutKeys = part.split(",", 1)
                    # print('Complete shortcut')
                    # print('==================================')
                    # print("This is the shortcut name: " + shortcutName)
                    # print("This is the shortcut keys: " + shortcutKeys)

                    section = 2
                else:
                    # print('Part 2, BoundKey and Modifier: ' + part)
                    boundKey, modifier = part.split(",", 1)
                    # print("This is the bound key: " + boundKey)
                    # print("This is the modifier: " + modifier)
                    # print('==================================')
                    section = 1

                if section == 1:
                    if shortcutCounter == 9:
                        x = x + 155
                        y = 20
                        shortcutCounter = 0

                    labelNew = QPushButton(boundKey + ": " + shortcutName, self)
                    labelNew.setToolTip("The Key(s) are: " + shortcutKeys + ". Modifier: " + modifier)
                    labelNew.resize(150, 30)

                    if shortcutCounter == 0:
                        labelNew.move(x, y)
                    else:
                        y = y + 35
                        labelNew.move(x, y)

                    shortcutCounter += 1
                    # labelNew.hide()
                    buttonList.append(labelNew)
                    section = 1

            pageHolder.update({pagehold: buttonList.copy()})
            pagehold += 1
            buttonList.clear()

        # only show first "page" on start
        if pageHolder is not None:
            pageSelectBox = QtWidgets.QComboBox(self)
            pageSelectBox.resize(200,25)
            pageSelectBox.move(int((width / 2) - (pageSelectBox.width() / 2)), int(height - 50))
            pageSelectBox.activated.connect(self.changePage)

        for key, page in pageHolder.items():
            pageSelectBox.addItem(nameHolder[key])
            for button in page:
                if key == 0:
                    button.show()
                else:
                    button.hide()

        # c = 0
        # for pages in pageHolder:
        #     for button in pages:
        #         if c == 0:
        #             button.show()
        #         else:
        #             button.hide()
        #     c += 1

        # pybutton = QPushButton('Button', self)
        # pybutton.resize(80, 30)
        # pybutton.move(20, 5)


    def mousePressEvent(self, a0) -> None:
        global latch
        self.hide()
        latch = True

    def changePage(self, wantedPage):
        global pageHolder

        pp.pprint(pageHolder)
        for key, page in pageHolder.items():
            for button in page:
                if key == wantedPage:
                    button.show()
                else:
                    button.hide()


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
                QtCore.QSize(400, 300),
                QtWidgets.qApp.desktop().availableGeometry()
            ))


def listifyFolderFiles(folderPath):

    unsortedlist = os.listdir(folderPath)
    print(folderPath)
    returnlist = list()

    for path in unsortedlist:
        print(path)
        filename, extenstion = os.path.splitext(path)
        print(extenstion)
        if extenstion == '.cueprofiledata':
            print(folderPath)
            fullpath = folderPath + '\\' + path
            print(folderPath + '\\' + path)
            returnlist.append(fullpath)
            pp.pprint(fullpath)

    return returnlist

def main():
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    window = SecondWindow()

    print("Sample app for pyqtkeybind:")
    print("\tPress Ctrl+Shift+A any where to trigger a callback.")
    print("\tCtrl+Shift+F unregisters and re-registers previous callback.")
    print("\tCtrl+Shift+E exits the app.")

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
