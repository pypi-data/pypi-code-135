# Widget
from Paperl.Paperui.Widgets.application import Application
from Paperl.Paperui.Widgets.window import Window
from Paperl.Paperui.Widgets.windowDevelop import WindowsDev, WindowsEffect, Windows22H2, Windows21H2
try:
    from Paperl.Paperui.Widgets.windowDevelop import ExButton
except:
    pass
from Paperl.Paperui.Widgets.scrollText import ScrollText
from Paperl.Paperui.Widgets.toplevel import Toplevel
from Paperl.Paperui.Widgets.toolBar import ToolBar
from Paperl.Paperui.Widgets.photo import Photo
from Paperl.Paperui.Widgets.panedWindow import PanedWindow
from Paperl.Paperui.Widgets.tooltip import Tooltip, TooltipEx
from Paperl.Paperui.Widgets.webBrowser import WebBrowser
from Paperl.Paperui.Widgets.treeView import TreeView
from Paperl.Paperui.Widgets.listBox import ListBox
from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.scrollBar import ScrollBar
from Paperl.Paperui.Widgets.button import Button
from Paperl.Paperui.Widgets.label import Label
from Paperl.Paperui.Widgets.message import Message
from Paperl.Paperui.Widgets.comboBox import ComboBox
from Paperl.Paperui.Widgets.checkButton import CheckButton
from Paperl.Paperui.Widgets.drag import Drag
from Paperl.Paperui.Widgets.scale import Scale
from Paperl.Paperui.Widgets.entry import Entry
from Paperl.Paperui.Widgets.sysTray import SysTray
from Paperl.Paperui.Widgets.page import Page
from Paperl.Paperui.Widgets.noteBook import NoteBook
from Paperl.Paperui.Widgets.infoBar import InfoBar
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.navigationView import NavigationView
from Paperl.Paperui.Widgets.themeBuilder import ThemeBuilder
from Paperl.Paperui.Widgets.text import Text
from Paperl.Paperui.Widgets.breadcrumbBar import BreadcrumbBar
from Paperl.Paperui.Widgets.dragFrame import DragFrameEx
from Paperl.Paperui.Widgets.progressBar import ProgressBar
from Paperl.Paperui.Widgets.popupMenuEx import PopupMenuEx
from Paperl.Paperui.Widgets.childWindow import ChildWindowEx
from Paperl.Paperui.Widgets.optionMenu import OptionMenu
from Paperl.Paperui.Widgets.menu import Menu
from Paperl.Paperui.Widgets.headerBar import HeaderBarEx
from Paperl.Paperui.Widgets.sizeGrip import SizeGrip
from Paperl.Paperui.Widgets.spinBox import SpinBox
from Paperl.Paperui.Widgets.group import Group
from Paperl.Paperui.Widgets.menuButton import MenuButton
from Paperl.Paperui.Widgets.tcl import TclAnalysis
from Paperl.Paperui.Widgets.messageBox import showMessageEx

# Core
from Paperl.Paperui.Widgets.image import Image
from Paperl.Paperui.Widgets.eventHandle import EventHandle
from Paperl.Paperui.Widgets.windowDevelop import WindowsDev

# Often
from Paperl.Paperui.Widgets.constant import *
from Paperl.Paperui.Widgets.stringsVar import StringsVar
from Paperl.Paperui.Widgets.booleanVar import BooleanVar


def aboutPaperl(mica: bool = False):
    aboutDialog = Toplevel()
    aboutDialog.maximizeBox()
    aboutDialog.minimizeBox()
    aboutDialog.setTitle("")
    aboutDialog.setSize(700, 95)
    context = Label(aboutDialog, "Paperl 是一个高级图形用户界面开发库，使用tkinter开发，与各种依赖库的支持而打造出来的。"
                                 "@XiangQinxi 版权所有")
    context.setBackground("#ffffff")
    context.setForeground("#000000")
    context.pack(fillType=FILL_BOTH, expandType=EXPAND_YES, marginX=10, marginY=10)
    return aboutDialog, context


from tkinter import Tk
def getDefaultRoot() -> Tk:
    try:
        from tkinter import _default_root
    except:
        pass
    else:
        return _default_root
