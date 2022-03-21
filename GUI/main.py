#Created by Cole Hagen intended for annotation of actigraph and feature data

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QInputDialog, QMessageBox
from pyqtgraph import PlotWidget
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtGui import *
import webbrowser

class ChecklistDialog(QtGui.QDialog):

    def __init__(
        self,
        name,
        stringlist=None,
        checked=False,
        icon=None,
        parent=None,
        ):
        super(ChecklistDialog, self).__init__(parent)

        self.name = name
        self.icon = icon
        self.model = QtGui.QStandardItemModel()
        self.listView = QtGui.QListView()

        for string in stringlist:
            item = QtGui.QStandardItem(string)
            item.setCheckable(True)
            check = \
                (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(check)
            self.model.appendRow(item)

        self.listView.setModel(self.model)

        self.okButton = QtGui.QPushButton('OK')
        self.cancelButton = QtGui.QPushButton('Cancel')
        self.selectButton = QtGui.QPushButton('Select All')
        self.unselectButton = QtGui.QPushButton('Unselect All')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.selectButton)
        hbox.addWidget(self.unselectButton)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setWindowTitle(self.name)
        if self.icon:
            self.setWindowIcon(self.icon)

        self.okButton.clicked.connect(self.onAccepted)
        self.cancelButton.clicked.connect(self.reject)
        self.selectButton.clicked.connect(self.select)
        self.unselectButton.clicked.connect(self.unselect)

    def onAccepted(self):
        self.choices = [self.model.item(i).text() for i in
                        range(self.model.rowCount())
                        if self.model.item(i).checkState()
                        == QtCore.Qt.Checked]
        self.accept()

    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1706, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        #####set palette here
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons8-checked-checkbox-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.signalWidget = PlotWidget(self.centralwidget)
        self.signalWidget.setGeometry(QtCore.QRect(10, 10, 1561, 831))
        self.signalWidget.setObjectName("signalWidget")
        #self.signalWidget.addLegend()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1706, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSave = QtWidgets.QMenu(self.menuMenu)
        self.menuSave.setObjectName("menuSave")
        self.menuLoad = QtWidgets.QMenu(self.menuMenu)
        self.menuLoad.setObjectName("menuLoad")
        #self.menuHelp = QtWidgets.QMenu(self.menubar)
        #self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setIconSize(QtCore.QSize(40, 40))
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionPrev = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../hagen/.designer/backup/icons8-previous-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrev.setIcon(icon1)
        self.actionPrev.setObjectName("actionPrev")
        self.actionFace = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../hagen/.designer/backup/icons8-face-id-96 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFace.setIcon(icon2)
        self.actionFace.setObjectName("actionFace")
        self.actionGraph = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../hagen/.designer/backup/icons8-graph-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGraph.setIcon(icon3)
        self.actionGraph.setObjectName("actionGraph")
        self.actionDataframe = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../hagen/.designer/backup/icons8-data-sheet-96 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataframe.setIcon(icon4)
        self.actionDataframe.setObjectName("actionDataframe")
        self.actionNext = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../hagen/.designer/backup/icons8-next-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext.setIcon(icon5)
        self.actionNext.setObjectName("actionNext")
        self.actionDeploy_Model = QtWidgets.QAction(MainWindow)
        self.actionDeploy_Model.setObjectName("actionDeploy_Model")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionXLXV = QtWidgets.QAction(MainWindow)
        self.actionXLXV.setObjectName("actionXLXV")
        self.actionTSV = QtWidgets.QAction(MainWindow)
        self.actionTSV.setObjectName("actionTSV")
        self.actionTXT = QtWidgets.QAction(MainWindow)
        self.actionTXT.setObjectName("actionTXT")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_Model = QtWidgets.QAction(MainWindow)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionDeploy_Model_2 = QtWidgets.QAction(MainWindow)
        self.actionDeploy_Model_2.setObjectName("actionDeploy_Model_2")
        self.actionCreate_Playlist = QtWidgets.QAction(MainWindow)
        self.actionCreate_Playlist.setObjectName("actionCreate_Playlist")
        self.actionExtract_Faces = QtWidgets.QAction(MainWindow)
        self.actionExtract_Faces.setObjectName("actionExtract_Faces")
        self.actionLoad_Project = QtWidgets.QAction(MainWindow)
        self.actionLoad_Project.setObjectName("actionLoad_Project")
        self.actionLoad_Annotations = QtWidgets.QAction(MainWindow)
        self.actionLoad_Annotations.setObjectName("actionLoad_Annotations")
        self.actionLoad_Image_Directory = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image_Directory.setObjectName("actionLoad_Image_Directory")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionCSV_2 = QtWidgets.QAction(MainWindow)
        self.actionCSV_2.setObjectName("actionCSV_2")
        self.actionXLXV_2 = QtWidgets.QAction(MainWindow)
        self.actionXLXV_2.setObjectName("actionXLXV_2")
        self.actionTSV_2 = QtWidgets.QAction(MainWindow)
        self.actionTSV_2.setObjectName("actionTSV_2")
        self.actionSaveAnn = QtWidgets.QAction(MainWindow)
        self.actionSaveAnn.setObjectName("actionSaveAnn")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSave_Annotation = QtWidgets.QAction(MainWindow)
        self.actionSave_Annotation.setObjectName("actionSave_Annotation")
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionCreate_Model = QtWidgets.QAction(MainWindow)
        self.actionCreate_Model.setObjectName("actionCreate_Model")
        self.actionOpen_Image_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image_Directory.setObjectName("actionOpen_Image_Directory")
        self.actionAnnotation_Key = QtWidgets.QAction(MainWindow)
        self.actionAnnotation_Key.setObjectName("actionAnnotation_Key")
        self.actionAnnotation_Key_2 = QtWidgets.QAction(MainWindow)
        self.actionAnnotation_Key_2.setObjectName("actionAnnotation_Key_2")
        self.actionExtract_Frames_from_Video = QtWidgets.QAction(MainWindow)
        self.actionExtract_Frames_from_Video.setObjectName("actionExtract_Frames_from_Video")
        self.actionSaveFD = QtWidgets.QAction(MainWindow)
        self.actionSaveFD.setObjectName("actionSaveFD")
        self.actionSaveML = QtWidgets.QAction(MainWindow)
        self.actionSaveML.setObjectName("actionSaveML")
        self.actionLoad_Signal_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_Signal_File.setObjectName("actionLoad_Signal_File")
        self.actionAnotation_File = QtWidgets.QAction(MainWindow)
        self.actionAnotation_File.setObjectName("actionAnotation_File")
        self.actionAdd_Annotation = QtWidgets.QAction(MainWindow)
        self.actionAdd_Annotation.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons8-add-database-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Annotation.setIcon(icon6)
        self.actionAdd_Annotation.setVisible(False)
        self.actionAdd_Annotation.setObjectName("actionAdd_Annotation")
        self.actionClassKey = QtWidgets.QAction(MainWindow)
        self.actionClassKey.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/icons8-list-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClassKey.setIcon(icon7)
        self.actionClassKey.setVisible(True)
        self.actionClassKey.setIconVisibleInMenu(True)
        self.actionClassKey.setObjectName("actionClassKey")
        self.actionLoad_Signal_Data = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/icons8-export-csv-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Signal_Data.setIcon(icon8)
        self.actionLoad_Signal_Data.setObjectName("actionLoad_Signal_Data")
        self.actionExport_Annotations = QtWidgets.QAction(MainWindow)
        self.actionExport_Annotations.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/icons8-import-csv-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_Annotations.setIcon(icon9)
        self.actionExport_Annotations.setObjectName("actionExport_Annotations")
        self.actionConfirm_Annotation_Area = QtWidgets.QAction(MainWindow)
        self.actionConfirm_Annotation_Area.setEnabled(False)
        self.actionTime = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/icons8-checked-checkbox-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        time_ico = QtGui.QIcon()
        time_ico.addPixmap(QtGui.QPixmap("resources/icons8-time-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
        self.actionConfirm_Annotation_Area.setIcon(icon10)
        self.actionTime.setIcon(time_ico)
        self.actionConfirm_Annotation_Area.setVisible(False)
        self.actionTime.setVisible(False)
        self.actionConfirm_Annotation_Area.setObjectName("actionConfirm_Annotation_Area")
        self.actionTime.setObjectName("actionTime")
        self.actionClass_1 = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_1.setIcon(icon11)
        self.actionClass_1.setVisible(False)
        self.actionClass_1.setObjectName("actionClass_1")
        self.actionClass_2 = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-y.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_2.setIcon(icon12)
        self.actionClass_2.setVisible(False)
        self.actionClass_2.setObjectName("actionClass_2")
        self.actionClass_3 = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-db.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_3.setIcon(icon13)
        self.actionClass_3.setVisible(False)
        self.actionClass_3.setObjectName("actionClass_3")
        self.actionClass_4 = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-t.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_4.setIcon(icon14)
        self.actionClass_4.setVisible(False)
        self.actionClass_4.setObjectName("actionClass_4")
        self.actionClass_5 = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-gg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_5.setIcon(icon15)
        self.actionClass_5.setVisible(False)
        self.actionClass_5.setObjectName("actionClass_5")
        self.actionClass_6 = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-dr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_6.setIcon(icon16)
        self.actionClass_6.setVisible(False)
        self.actionClass_6.setObjectName("actionClass_6")
        self.actionClass_7 = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-dt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_7.setIcon(icon17)
        self.actionClass_7.setVisible(False)
        self.actionClass_7.setObjectName("actionClass_7")
        self.actionClass_8 = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-pi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_8.setIcon(icon18)
        self.actionClass_8.setVisible(False)
        self.actionClass_8.setObjectName("actionClass_8")
        self.actionClass_9 = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-dy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_9.setIcon(icon19)
        self.actionClass_9.setVisible(False)
        self.actionClass_9.setObjectName("actionClass_9")
        self.actionClass_10 = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-w.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_10.setIcon(icon20)
        self.actionClass_10.setVisible(False)
        self.actionClass_10.setObjectName("actionClass_10")
        self.actionClass_11 = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-hp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_11.setIcon(icon21)
        self.actionClass_11.setVisible(False)
        self.actionClass_11.setObjectName("actionClass_11")
        self.actionClass_12 = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_12.setIcon(icon22)
        self.actionClass_12.setVisible(False)
        self.actionClass_12.setObjectName("actionClass_12")
        self.actionClass_13 = QtWidgets.QAction(MainWindow)
        self.actionClass_13.setIcon(icon15)
        self.actionClass_13.setVisible(False)
        self.actionClass_13.setObjectName("actionClass_13")
        self.actionClass_14 = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-o.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_14.setIcon(icon23)
        self.actionClass_14.setVisible(False)
        self.actionClass_14.setObjectName("actionClass_14")
        self.actionClass_15 = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("resources/icons8-heat-map-96-m.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClass_15.setIcon(icon24)
        self.actionClass_15.setVisible(False)
        self.actionClass_15.setObjectName("actionClass_15")


        self.actionClass_16 = QtWidgets.QAction(MainWindow)
        self.actionClass_16.setIcon(icon12)
        self.actionClass_16.setVisible(False)
        self.actionClass_16.setObjectName("actionClass_16")
        
        self.actionClass_17 = QtWidgets.QAction(MainWindow)
        self.actionClass_17.setIcon(icon13)
        self.actionClass_17.setVisible(False)
        self.actionClass_17.setObjectName("actionClass_17")
        
        
        
        self.menuSave.addAction(self.actionSave_Project)
        self.menuLoad.addAction(self.actionLoad_Project)
        self.menuMenu.addAction(self.menuLoad.menuAction())
        self.menuMenu.addAction(self.menuSave.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        #self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionLoad_Signal_Data)
        self.toolBar.addAction(self.actionExport_Annotations)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Annotation)
        self.toolBar.addAction(self.actionConfirm_Annotation_Area)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClassKey)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTime)
        self.toolBar_2.addAction(self.actionClass_1)
        self.toolBar_2.addAction(self.actionClass_2)
        self.toolBar_2.addAction(self.actionClass_3)
        self.toolBar_2.addAction(self.actionClass_4)
        self.toolBar_2.addAction(self.actionClass_5)
        self.toolBar_2.addAction(self.actionClass_6)
        self.toolBar_2.addAction(self.actionClass_7)
        self.toolBar_2.addAction(self.actionClass_8)
        self.toolBar_2.addAction(self.actionClass_9)
        self.toolBar_2.addAction(self.actionClass_10)
        self.toolBar_2.addAction(self.actionClass_11)
        self.toolBar_2.addAction(self.actionClass_12)
        self.toolBar_2.addAction(self.actionClass_13)
        self.toolBar_2.addAction(self.actionClass_14)
        self.toolBar_2.addAction(self.actionClass_15)
        self.toolBar_2.addAction(self.actionClass_16)
        self.toolBar_2.addAction(self.actionClass_17)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QualAI-Signal"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
        #self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionPrevious.setText(_translate("MainWindow", "Previous"))
        self.actionPrev.setText(_translate("MainWindow", "Previous"))
        self.actionPrev.setToolTip(_translate("MainWindow", "Previous Image"))
        self.actionPrev.setShortcut(_translate("MainWindow", "Left"))
        self.actionFace.setText(_translate("MainWindow", "Analyze"))
        self.actionFace.setToolTip(_translate("MainWindow", "Face Analysis: Action Units and Emotion Predictions"))
        self.actionFace.setShortcut(_translate("MainWindow", "F"))
        self.actionGraph.setText(_translate("MainWindow", "Graph"))
        self.actionGraph.setToolTip(_translate("MainWindow", "Graph Annotation and Analysis Data"))
        self.actionGraph.setShortcut(_translate("MainWindow", "G"))
        self.actionDataframe.setText(_translate("MainWindow", "Dataframe"))
        self.actionDataframe.setToolTip(_translate("MainWindow", "Dataframe of Annotation and Analysis"))
        self.actionDataframe.setShortcut(_translate("MainWindow", "D"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionNext.setToolTip(_translate("MainWindow", "Next Image"))
        self.actionNext.setShortcut(_translate("MainWindow", "Right"))
        self.actionDeploy_Model.setText(_translate("MainWindow", "Deploy Model"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionXLXV.setText(_translate("MainWindow", "XLXV"))
        self.actionTSV.setText(_translate("MainWindow", "TSV"))
        self.actionTXT.setText(_translate("MainWindow", "TXT"))
        self.actionAbout.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setShortcut(_translate("MainWindow", "?"))
        self.actionLoad_Model.setText(_translate("MainWindow", "Load Model"))
        self.actionDeploy_Model_2.setText(_translate("MainWindow", "Deploy Model"))
        self.actionCreate_Playlist.setText(_translate("MainWindow", "Create Directory"))
        self.actionExtract_Faces.setText(_translate("MainWindow", "Extract Faces from Images"))
        self.actionLoad_Project.setText(_translate("MainWindow", "Import Data"))
        self.actionLoad_Project.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionLoad_Annotations.setText(_translate("MainWindow", "Load Annotations"))
        self.actionLoad_Image_Directory.setText(_translate("MainWindow", "Load Image Playlist"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Data"))
        self.actionSave_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCSV_2.setText(_translate("MainWindow", "CSV"))
        self.actionXLXV_2.setText(_translate("MainWindow", "XLXV"))
        self.actionTSV_2.setText(_translate("MainWindow", "TSV"))
        self.actionSaveAnn.setText(_translate("MainWindow", "Annotations"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSave_Annotation.setText(_translate("MainWindow", "Save Annotations"))
        self.actionCreate.setText(_translate("MainWindow", "New Project"))
        self.actionCreate_Model.setText(_translate("MainWindow", "Create Model"))
        self.actionOpen_Image_Directory.setText(_translate("MainWindow", "Open Image Directory"))
        self.actionOpen_Image_Directory.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionAnnotation_Key.setText(_translate("MainWindow", "Annotation"))
        self.actionAnnotation_Key_2.setText(_translate("MainWindow", "Annotation Key"))
        self.actionExtract_Frames_from_Video.setText(_translate("MainWindow", "Extract Frames from Video"))
        self.actionSaveFD.setText(_translate("MainWindow", "Notes"))
        self.actionSaveML.setText(_translate("MainWindow", "Loaded Model Predictions"))
        self.actionLoad_Signal_File.setText(_translate("MainWindow", "Signal File"))
        self.actionAnotation_File.setText(_translate("MainWindow", "Anotation File"))
        self.actionAdd_Annotation.setText(_translate("MainWindow", "Add Annotation"))
        self.actionAdd_Annotation.setStatusTip(_translate("MainWindow", "Add Annotation"))
        self.actionClassKey.setText(_translate("MainWindow", "Create Classification Key"))
        self.actionClassKey.setStatusTip(_translate("MainWindow", "Create Classification Key"))
        self.actionLoad_Signal_Data.setText(_translate("MainWindow", "Load Signal Data"))
        self.actionExport_Annotations.setText(_translate("MainWindow", "Export Annotations"))
        self.actionConfirm_Annotation_Area.setText(_translate("MainWindow", "Confirm Annotation Area"))
        self.actionTime.setText(_translate("MainWindow", "Time Tool"))
        self.actionConfirm_Annotation_Area.setStatusTip(_translate("MainWindow", "Confirm Annotation Area"))
        self.actionTime.setStatusTip(_translate("MainWindow", "Time Tool"))
        self.actionClass_1.setText(_translate("MainWindow", "Class 1"))
        self.actionClass_2.setText(_translate("MainWindow", "Class 2"))
        self.actionClass_3.setText(_translate("MainWindow", "Class 3"))
        self.actionClass_4.setText(_translate("MainWindow", "Class 4"))
        self.actionClass_5.setText(_translate("MainWindow", "Class 5"))
        self.actionClass_6.setText(_translate("MainWindow", "Class 6"))
        self.actionClass_7.setText(_translate("MainWindow", "Class 7"))
        self.actionClass_8.setText(_translate("MainWindow", "Class 8"))
        self.actionClass_9.setText(_translate("MainWindow", "Class 9"))
        self.actionClass_10.setText(_translate("MainWindow", "Class 10"))
        self.actionClass_11.setText(_translate("MainWindow", "Class 11"))
        self.actionClass_12.setText(_translate("MainWindow", "Class 12"))
        self.actionClass_13.setText(_translate("MainWindow", "Class 13"))
        self.actionClass_14.setText(_translate("MainWindow", "Class 14"))
        self.actionClass_15.setText(_translate("MainWindow", "Class 15"))
        self.actionClass_16.setText(_translate("MainWindow", "Class 16"))
        self.actionClass_17.setText(_translate("MainWindow", "Class 17"))        
        self.signalWidget.setBackground(background=None)
        self.actionLoad_Signal_Data.triggered.connect(self.load_signal_file)
        self.actionClassKey.triggered.connect(self.create_key)
        self.actionClass_1.triggered.connect(self.class_1_img)
        self.actionClass_2.triggered.connect(self.class_2_img)    
        self.actionClass_3.triggered.connect(self.class_3_img)
        self.actionClass_4.triggered.connect(self.class_4_img) 
        self.actionClass_5.triggered.connect(self.class_5_img)
        self.actionClass_6.triggered.connect(self.class_6_img)  
        self.actionClass_7.triggered.connect(self.class_7_img)
        self.actionClass_8.triggered.connect(self.class_8_img)
        self.actionClass_9.triggered.connect(self.class_9_img)    
        self.actionClass_10.triggered.connect(self.class_10_img)
        self.actionClass_11.triggered.connect(self.class_11_img) 
        self.actionClass_12.triggered.connect(self.class_12_img)
        self.actionClass_13.triggered.connect(self.class_13_img)  
        self.actionClass_14.triggered.connect(self.class_14_img)
        self.actionClass_15.triggered.connect(self.class_15_img) 
        self.actionClass_16.triggered.connect(self.class_16_img)
        self.actionClass_17.triggered.connect(self.class_17_img)
        self.actionExport_Annotations.triggered.connect(self.export_data)
        self.actionSave_Project.triggered.connect(self.export_data)
        self.actionLoad_Project.triggered.connect(self.load_signal_file)
        self.actionConfirm_Annotation_Area.triggered.connect(self.get_annotation_values)
        self.actionTime.triggered.connect(self.time_tool)
        self.actionAbout.triggered.connect(self.helpsy)



        self.c1_cnt = 0
        self.c2_cnt = 0
        self.c3_cnt = 0
        self.c4_cnt = 0
        self.c5_cnt = 0
        self.c6_cnt = 0
        self.c7_cnt = 0
        self.c8_cnt = 0
        self.c9_cnt = 0
        self.c10_cnt = 0
        self.c11_cnt = 0
        self.c12_cnt = 0
        self.c13_cnt = 0
        self.c14_cnt = 0
        self.c15_cnt = 0
        self.c16_cnt = 0
        self.c17_cnt = 0
        
    def load_signal_file(self):
        self.loaded_signal_file, _ = QFileDialog.getOpenFileName()
        print(self.loaded_signal_file)
        rows,ok = QInputDialog.getInt(MainWindow,"Header Rows","Enter Number of Header Rows (actigraph has 10)", min =0, max=15)
        if ok:
            self.signal_df = pd.read_csv(self.loaded_signal_file, header=rows)
        form = ChecklistDialog('Enter Columns to Plot', list(self.signal_df), checked=False)
        colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']
        if form.exec_() == QtGui.QDialog.Accepted:
            print(list(form.choices))
            for x,y in zip(form.choices,colors):
                self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df[x], pen=y)
        
        #self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df.iloc[:,1], pen = "b")
        #self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df.iloc[:,2], pen = "r")
        #self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df.iloc[:,3], pen = 'g')
        self.signal_df.insert(0, 'class', 0)
        self.signal_df.insert(1, 'anno_key', "NAN")
        self.actionExport_Annotations.setEnabled(True)
        self.actionLoad_Signal_Data.setEnabled(False)
        self.actionClassKey.setEnabled(True)
        self.signalWidget.setMouseEnabled(y=False)
        self.actionConfirm_Annotation_Area.setEnabled(True)
        self.actionConfirm_Annotation_Area.setVisible(True)
        self.actionTime.setVisible(True)
        
        

        
    def get_annotation_values(self):
        self.lr_region = list(self.lr.getRegion())
        self.lr_region_max = int(max(self.lr_region)) 
        self.lr_region_min = int(min(self.lr_region))
        self.lr_range = range(self.lr_region_min, self.lr_region_max)
        self.signal_df.loc[self.lr_range, 'class'] = self.cur_class 
        self.signal_df.loc[self.lr_range, 'anno_key'] = self.cur_txt
        print(self.signal_df)
        #self.txt_itm = pg.TextItem(self.cur_txt, color='k', anchor=(self.lr_region_min,-10))
        #self.signalWidget.addItem(self.txt_itm)
        #self.lr.setMovable(False)
        #self.lr.sigRegionChanged.connect(self.change_data)
        #self.lr.sigRegionChangeFinished.connect(self.replace_data)
        self.lr.setMovable(False)



    def create_key(self):
        anns,ok = QInputDialog.getInt(MainWindow,"Number of Classifications","Enter Number of Classifications", min =1, max=17)
        if ok:
            self.class_num = anns
            self.set_vis_classes()
        self.actionClassKey.setEnabled(False)
    def set_vis_classes(self):
        if self.class_num == 1:
            self.actionClass_1.setVisible(True)
        if self.class_num == 2:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
        if self.class_num == 3:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
        if self.class_num == 4:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
        if self.class_num == 5:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
        if self.class_num == 6:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
        if self.class_num == 7:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
        if self.class_num == 8:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
        if self.class_num == 9:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
        if self.class_num == 10:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
        if self.class_num == 11:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
        if self.class_num == 12:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
        if self.class_num == 13:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
            self.actionClass_13.setVisible(True)
        if self.class_num == 14:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
            self.actionClass_13.setVisible(True)
            self.actionClass_14.setVisible(True)
        if self.class_num == 15:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
            self.actionClass_13.setVisible(True)
            self.actionClass_14.setVisible(True)
            self.actionClass_15.setVisible(True)
        if self.class_num == 16:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
            self.actionClass_13.setVisible(True)
            self.actionClass_14.setVisible(True)
            self.actionClass_15.setVisible(True)
            self.actionClass_16.setVisible(True)
        if self.class_num == 17:
            self.actionClass_1.setVisible(True)
            self.actionClass_2.setVisible(True)
            self.actionClass_3.setVisible(True)
            self.actionClass_4.setVisible(True)
            self.actionClass_5.setVisible(True)
            self.actionClass_6.setVisible(True)
            self.actionClass_7.setVisible(True)
            self.actionClass_8.setVisible(True)
            self.actionClass_9.setVisible(True)
            self.actionClass_10.setVisible(True)
            self.actionClass_11.setVisible(True)
            self.actionClass_12.setVisible(True)
            self.actionClass_13.setVisible(True)
            self.actionClass_14.setVisible(True)
            self.actionClass_15.setVisible(True)
            self.actionClass_16.setVisible(True)
            self.actionClass_17.setVisible(True)

    def class_1_img(self):
        self.cur_class = 1
        self.brush = 255, 102, 102, 100
        if self.c1_cnt == 0:
            self.class1_txt,ok = QInputDialog.getText(MainWindow,"Class 1","Enter Class Name")
            if ok:
                self.class1_txt = self.class1_txt
                
                self.actionClass_1.setText(self.class1_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c1_cnt = self.c1_cnt + 1
                self.cur_txt = self.class1_txt
                
        elif self.c1_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class1_txt
        
        
        
    def class_2_img(self):
        self.cur_class = 2
        self.brush = 226, 230, 11, 100
        if self.c2_cnt == 0:
            self.class2_txt,ok = QInputDialog.getText(MainWindow,"Class 2","Enter Class Name")
            if ok:
                self.class2_txt = self.class2_txt
                
                self.actionClass_2.setText(self.class2_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c2_cnt = self.c2_cnt + 1
                self.cur_txt = self.class2_txt
                
        elif self.c2_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class2_txt
    def class_3_img(self):
        self.cur_class = 3
        self.brush = 110, 11, 230, 100
        if self.c3_cnt == 0:
            self.class3_txt,ok = QInputDialog.getText(MainWindow,"Class 3","Enter Class Name")
            if ok:
                self.class3_txt = self.class3_txt
                
                self.actionClass_3.setText(self.class3_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c3_cnt = self.c3_cnt + 1
                self.cur_txt = self.class3_txt
                
        elif self.c3_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class3_txt
    def class_4_img(self):
        self.cur_class = 4
        self.brush = 11, 211, 230, 100
        if self.c4_cnt == 0:
            self.class4_txt,ok = QInputDialog.getText(MainWindow,"Class 4","Enter Class Name")
            if ok:
                self.class4_txt = self.class4_txt
                
                self.actionClass_4.setText(self.class4_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c4_cnt = self.c4_cnt + 1
                self.cur_txt = self.class4_txt
                
        elif self.c4_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class4_txt
    def class_5_img(self):
        self.cur_class = 5
        self.brush = 11, 230, 131, 100
        if self.c5_cnt == 0:
            self.class5_txt,ok = QInputDialog.getText(MainWindow,"Class 5","Enter Class Name")
            if ok:
                self.class5_txt = self.class5_txt
                
                self.actionClass_5.setText(self.class5_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c5_cnt = self.c5_cnt + 1
                self.cur_txt = self.class5_txt
                
        elif self.c5_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class5_txt
    def class_6_img(self):
        self.cur_class = 6
        self.brush = 128, 51, 74, 100
        if self.c6_cnt == 0:
            self.class6_txt,ok = QInputDialog.getText(MainWindow,"Class 6","Enter Class Name")
            if ok:
                self.class6_txt = self.class6_txt
                
                self.actionClass_6.setText(self.class6_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c6_cnt = self.c6_cnt + 1
                self.cur_txt = self.class6_txt
                
        elif self.c6_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class6_txt
    def class_7_img(self):
        self.cur_class = 7
        self.brush = 51, 128,92, 100
        if self.c7_cnt == 0:
            self.class7_txt,ok = QInputDialog.getText(MainWindow,"Class 7","Enter Class Name")
            if ok:
                self.class7_txt = self.class7_txt
                
                self.actionClass_7.setText(self.class7_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c7_cnt = self.c7_cnt + 1
                self.cur_txt = self.class7_txt
                
        elif self.c7_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class7_txt
    def class_8_img(self):
        self.cur_class = 8
        self.brush = 217, 163,207, 100
        if self.c8_cnt == 0:
            self.class8_txt,ok = QInputDialog.getText(MainWindow,"Class 8","Enter Class Name")
            if ok:
                self.class8_txt = self.class8_txt
                
                self.actionClass_8.setText(self.class8_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c8_cnt = self.c8_cnt + 1
                self.cur_txt = self.class8_txt
                
        elif self.c8_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class8_txt
    def class_9_img(self):
        self.cur_class = 9
        self.brush = 191, 204, 94, 100
        if self.c9_cnt == 0:
            self.class9_txt,ok = QInputDialog.getText(MainWindow,"Class 9","Enter Class Name")
            if ok:
                self.class9_txt = self.class9_txt
                
                self.actionClass_9.setText(self.class9_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c9_cnt = self.c9_cnt + 1
                self.cur_txt = self.class9_txt
                
        elif self.c9_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class9_txt
    def class_10_img(self):
        self.cur_class = 10
        self.brush = 188, 195, 204, 100
        if self.c10_cnt == 0:
            self.class10_txt,ok = QInputDialog.getText(MainWindow,"Class 10","Enter Class Name")
            if ok:
                self.class10_txt = self.class10_txt
                
                self.actionClass_10.setText(self.class10_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c10_cnt = self.c10_cnt + 1
                self.cur_txt = self.class10_txt
                
        elif self.c10_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class10_txt
    def class_11_img(self):
        self.cur_class = 11
        self.brush = 245, 59, 255, 100
        if self.c11_cnt == 0:
            self.class11_txt,ok = QInputDialog.getText(MainWindow,"Class 11","Enter Class Name")
            if ok:
                self.class11_txt = self.class11_txt
                
                self.actionClass_11.setText(self.class11_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c11_cnt = self.c11_cnt + 1
                self.cur_txt = self.class11_txt
                
        elif self.c11_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class11_txt
    def class_12_img(self):
        self.cur_class = 12
        self.brush = 151, 147, 194, 100
        if self.c12_cnt == 0:
            self.class12_txt,ok = QInputDialog.getText(MainWindow,"Class 12","Enter Class Name")
            if ok:
                self.class12_txt = self.class12_txt
                
                self.actionClass_12.setText(self.class12_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c12_cnt = self.c12_cnt + 1
                self.cur_txt = self.class12_txt
                
        elif self.c12_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class12_txt
    def class_13_img(self):
        self.cur_class = 13
        self.brush = 0, 255, 34, 100
        if self.c13_cnt == 0:
            self.class13_txt,ok = QInputDialog.getText(MainWindow,"Class 13","Enter Class Name")
            if ok:
                self.class13_txt = self.class13_txt
                
                self.actionClass_13.setText(self.class13_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c13_cnt = self.c13_cnt + 1
                self.cur_txt = self.class13_txt
                
        elif self.c13_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class13_txt
    def class_14_img(self):
        self.cur_class = 14
        self.brush = 255, 234, 71, 100
        if self.c14_cnt == 0:
            self.class14_txt,ok = QInputDialog.getText(MainWindow,"Class 14","Enter Class Name")
            if ok:
                self.class14_txt = self.class14_txt
                
                self.actionClass_14.setText(self.class14_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c14_cnt = self.c14_cnt + 1
                self.cur_txt = self.class14_txt
                
        elif self.c14_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class14_txt
    def class_15_img(self):
        self.cur_class = 15
        self.brush = 148, 53, 118, 100
        if self.c15_cnt == 0:
            self.class15_txt,ok = QInputDialog.getText(MainWindow,"Class 15","Enter Class Name")
            if ok:
                self.class15_txt = self.class15_txt
                
                self.actionClass_15.setText(self.class15_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c15_cnt = self.c15_cnt + 1
                self.cur_txt = self.class15_txt
                
        elif self.c15_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class15_txt
    def class_16_img(self):
        self.cur_class = 16
        self.brush = 226, 230, 11, 100
        if self.c16_cnt == 0:
            self.class16_txt,ok = QInputDialog.getText(MainWindow,"Class 16","Enter Class Name")
            if ok:
                self.class16_txt = self.class16_txt
                
                self.actionClass_16.setText(self.class16_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c16_cnt = self.c16_cnt + 1
                self.cur_txt = self.class16_txt
                
        elif self.c16_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class16_txt
    def class_17_img(self):
        self.cur_class = 17
        self.brush = 110, 11, 230, 100
        if self.c17_cnt == 0:
            self.class17_txt,ok = QInputDialog.getText(MainWindow,"Class 17","Enter Class Name")
            if ok:
                self.class17_txt = self.class17_txt
                
                self.actionClass_17.setText(self.class17_txt)
                self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)],brush = self.brush)  # This is a mouse-draggable window on the plot
                self.lr.setBounds([0, len(self.signal_df.index.values)])
                self.signalWidget.addItem(self.lr)
                self.c17_cnt = self.c17_cnt + 1
                self.cur_txt = self.class17_txt
                
        elif self.c17_cnt > 0:
            self.lr = pg.LinearRegionItem([0, len(self.signal_df.index.values)], brush = self.brush)  # This is a mouse-draggable window on the plot
            self.lr.setBounds([0, len(self.signal_df.index.values)])
            self.signalWidget.addItem(self.lr)
            self.cur_txt = self.class17_txt

    def export_data(self):
        self.saved_annotations, _ = QFileDialog.getSaveFileName()
        self.signal_df.to_csv(self.saved_annotations + ".csv")
    def load_project(self):
        self.loaded_signal_file, _ = QFileDialog.getOpenFileName()
        print(self.loaded_signal_file)
        self.signal_df = pd.read_csv(self.loaded_signal_file)
        self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df["Accelerometer X"], pen = "b")
        self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df["Accelerometer Y"], pen = "r")
        self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df["Accelerometer Z"], pen = 'g')
        self.signalWidget.plot(x= self.signal_df.index.values, y=self.signal_df["class"], pen = 'k', symbol = 'o')
        self.actionExport_Annotations.setEnabled(True)
        self.actionLoad_Signal_Data.setEnabled(False)
        self.actionClassKey.setEnabled(True)
        self.signalWidget.setMouseEnabled(y=False)
        self.actionConfirm_Annotation_Area.setEnabled(True)
        self.actionConfirm_Annotation_Area.setVisible(True)
        self.actionTime.setVisible(True)
    def change_data(self):
        self.signal_df.loc[self.lr_range, 'class'] = 0
        self.signal_df.loc[self.lr_range, 'anno_key'] = "NaN"
        self.lr_region = list(self.lr.getRegion())
        self.lr_region_max = int(max(self.lr_region)) 
        self.lr_region_min = int(min(self.lr_region))
        self.lr_range = range(self.lr_region_min, self.lr_region_max)

        print(self.signal_df)
    def replace_data(self):
        self.lr_region = list(self.lr.getRegion())
        self.lr_region_max = int(max(self.lr_region)) 
        self.lr_region_min = int(min(self.lr_region))
        self.lr_range = range(self.lr_region_min, self.lr_region_max)
        self.signal_df.loc[self.lr_range, 'class'] = self.cur_class
        self.signal_df.loc[self.lr_range, 'anno_key'] = self.cur_txt
        print(self.signal_df)
        self.lr.setMovable(False)

    def time_tool(self):
        self.time_l = pg.InfiniteLine(pos=0, pen = 'k', markers = '>|<')
        self.signalWidget.addItem(self.time_l)
        self.time_l.setMovable(True)

        #self.pos = self.signal_df.iloc(self.inf_num, 2)
        self.time_l.sigPositionChangeFinished.connect(self.value)
        self.actionTime.setVisible(False)
    def value(self):
        self.inf_num = self.time_l.value()
        print(self.inf_num)
        self.time_num = self.signal_df.iloc[int(self.inf_num), 2]
        print(self.time_num)
        #self.time_l = pg.InfiniteLine(pos= self.inf_num, label= str(self.time_num))
        msg = QMessageBox()
        msg.setText("Timestamp: " + str(self.time_num))
        msg.setWindowTitle("Time Tool")
        msg.setDetailedText(str(self.signal_df.iloc[int(self.inf_num), :]))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	
        msg.exec_()
    def helpsy(self):
        webbrowser.open('https://github.com/chags1313/QualAI-Signal/wiki')
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    palette = QPalette()
    """palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")"""
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
