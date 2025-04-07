import os, json, sys
from PySide6 import QtGui, QtUiTools, QtWidgets, QtCore
from .view import Bob
from .utils import loglib
from .config import config_loader
from . import unreal_work

from importlib import reload


# loglib.LogUtil.create(__name__)
# from PySide6.QtUiTools import QUiLoader

# ========
# FUNCTION
# ========

ps6_folder = os.path.dirname(QtGui.__file__)


app = None
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)


class Picker(QtWidgets.QMainWindow):
    DATA = ""

    def __init__(self):
        super(Picker, self).__init__()
        self.ui = Bob.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setupUi(self)
        self.rubberband = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self)
        self.setMouseTracking(True)

        self.charName = ""

        self.preCtrl = []
        self.ctrlRig = None
        self.ctrlRigs = None
        self._connect_event()
        self.populateCtrlRigs()
        icon = QtGui.QIcon()
        riot_ico = r"D:\P4_Internal\CTS_ControlRigTraining 5.5\Plugins\CTS_UE_Python\Content\Python\UEPicker\view\images\smile.jpg"
        icon.addPixmap(QtGui.QPixmap(riot_ico), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def _connect_event(self):
        self.ui.refresh_btn.clicked.connect(self.populateCtrlRigs)
        self.ui.ctrlRigNames_cbx.currentIndexChanged.connect(self.getCtrlRig)

    def saveData(self):
        config_loader.saveJson(self.DATA,self.currentDataFile)

    def add_item_to_cr_cbx(self, items):
        self.ui.ctrlRigNames_cbx.clear()
        self.ui.ctrlRigNames_cbx.addItems(items)

    def loadData(self):
        if not os.path.isfile(self.currentDataFile):
            self.currentDataFile = config_loader.get_default_cfg()

        self.DATA = config_loader.readJson(self.currentDataFile)

    def populateCtrlRigs(self):
        seq = unreal_work.get_focused_level_seq()
        self.ctrlRigs = unreal_work.get_control_rigs_in_lev_seq(seq)
        l = sorted([str(i.track.get_display_name()) for i in self.ctrlRigs])
        self.ctrlRigs = [i for i in self.ctrlRigs]
        self.add_item_to_cr_cbx(l)

    def getCtrlRig(self):
        self.getCharName()
        ctrlRigs_ = [i for i in self.ctrlRigs if i.track.get_display_name() == self.charName]
        if not ctrlRigs_:
            return
        self.ctrlRig = ctrlRigs_[0]
        self.preCtrl = self.ctrlRig.control_rig.current_control_selection()
        print(self.ctrlRig)
        log_file = loglib.get_log_file()
        self.currentDataFile = f"{log_file}{self.charName}.json"
        if not os.path.isfile(self.currentDataFile):
            self.currentDataFile = config_loader.get_default_cfg()
            self.loadData()
            self.currentDataFile = f"{log_file}{self.charName}.json"
            self.saveData()
        self.refreshData()

    def refreshData(self):
        self.loadData()
        self.addSelectEvent()

    def select(self, ctrlnames, keyName=""):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            print('Shift+Click')
        elif modifiers == QtCore.Qt.ControlModifier:
            print('Control+Click')
        elif modifiers == (QtCore.Qt.ControlModifier |
                           QtCore.Qt.ShiftModifier):
            print('Control+Shift+Click')
            if keyName:
                self.saveSelection(keyName)
                self.refreshData()
        else:
            print('Click')
            if not self.ctrlRig: return
            if not self.ctrlRig: return
            for i in ctrlnames:
                print(i)
                self.ctrlRig.control_rig.select_control(i)
                self.preCtrl.append(i)

    def deselect(self, o=None):
        if not self.ctrlRig: return
        if o:
            self.ctrlRig.control_rig.select_control(o, False)
            self.preCtrl.remove(o)
        else:
            if self.preCtrl:
                for i in self.preCtrl:
                    self.ctrlRig.control_rig.select_control(i, False)
                    self.preCtrl.remove(i)

    def addSelectEvent(self):
        for k, v in self.DATA["anim_table"].items():
            if hasattr(self.ui, k):
                btn = getattr(self.ui, k)
                btn.clicked.connect(lambda event=0, t=[v, k]: self.select([t[0]], t[1]))
        # select all
        self.ui.select_all.clicked.connect(
            lambda event=0, t=self.DATA["anim_table"].values(): self.select([i for i in t]))
        self.ui.select_all.clicked.connect(self.checkAllButton)

    def checkAllButton(self):
        print("select all!")
        for child in self.findChildren(QtWidgets.QPushButton):
            child.setChecked(True)

    def getCharName(self):
        self.charName = self.ui.ctrlRigNames_cbx.currentText()
        return self.charName



    def saveSelection(self, objectName):
        # sel = unreal.EditorActorSubsystem().get_selected_level_actors()[0]
        sel = self.ctrlRig.control_rig.current_control_selection()
        if sel:
            name = str(sel[0])
            self.DATA["anim_table"][objectName] = name
            print("save " + objectName + " to anim_table --> " + self.DATA["anim_table"][objectName])
            self.saveData()

    def mousePressEvent(self, event):

        self.origin = event.position()
        self.rubberband.setGeometry(
            QtCore.QRect(self.origin.toPoint(), QtCore.QSize()))
        self.rubberband.show()

        self.focused_widget = QtWidgets.QApplication.focusWidget()
        if self.focused_widget:
            self.focused_widget.clearFocus()

        QtWidgets.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin.toPoint(), event.position().toPoint()).normalized())
        QtWidgets.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.hide()
            selected = []
            rect = self.rubberband.geometry()
            for child in self.findChildren(QtWidgets.QPushButton):
                if rect.intersects(child.geometry()):
                    selected.append(child)
            if selected:
                [child.click() for child in selected]
                for child in selected:
                    print(self.DATA)
                    name = self.DATA["anim_table"][child.objectName()]
                    self.select(name)
            else:
                for child in self.findChildren(QtWidgets.QPushButton):
                    child.setChecked(False)
                    self.deselect()
        QtWidgets.QWidget.mouseReleaseEvent(self, event)

def show():
    global wid
    # wid = QtWidgets.QWidget()
    wid = Picker()
    unreal_work.parent_external_window(wid)
    wid.show()
