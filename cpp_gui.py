# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpp_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridFrame = GridFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setAutoFillBackground(False)
        self.gridFrame.setStyleSheet("background-color: white;")
        self.gridFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.gridFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridFrame.setObjectName("gridFrame")
        self.verticalLayout_2.addWidget(self.gridFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnDraw.setObjectName("btnDraw")
        self.horizontalLayout.addWidget(self.btnDraw)
        self.btnErase = QtWidgets.QPushButton(self.centralwidget)
        self.btnErase.setObjectName("btnErase")
        self.horizontalLayout.addWidget(self.btnErase)
        self.btnSetStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetStart.setObjectName("btnSetStart")
        self.horizontalLayout.addWidget(self.btnSetStart)
        self.btnCalculatePath = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculatePath.setObjectName("btnCalculatePath")
        self.horizontalLayout.addWidget(self.btnCalculatePath)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent = QtWidgets.QMenu(self.menuFile)
        self.menuRecent.setObjectName("menuRecent")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPrefrences = QtWidgets.QAction(MainWindow)
        self.actionPrefrences.setObjectName("actionPrefrences")
        self.actionDraw = QtWidgets.QAction(MainWindow)
        self.actionDraw.setObjectName("actionDraw")
        self.actionSet_Start_Point = QtWidgets.QAction(MainWindow)
        self.actionSet_Start_Point.setObjectName("actionSet_Start_Point")
        self.actionErase = QtWidgets.QAction(MainWindow)
        self.actionErase.setObjectName("actionErase")
        self.actionPan = QtWidgets.QAction(MainWindow)
        self.actionPan.setObjectName("actionPan")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actiontest_path = QtWidgets.QAction(MainWindow)
        self.actiontest_path.setObjectName("actiontest_path")
        self.menuRecent.addAction(self.actiontest_path)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionDraw)
        self.menuEdit.addAction(self.actionErase)
        self.menuEdit.addAction(self.actionSet_Start_Point)
        self.menuSetting.addAction(self.actionPrefrences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coverage Path Planner v0.1"))
        self.btnDraw.setText(_translate("MainWindow", "Draw"))
        self.btnErase.setText(_translate("MainWindow", "Erase"))
        self.btnSetStart.setText(_translate("MainWindow", "Set Start Point"))
        self.btnCalculatePath.setText(_translate("MainWindow", "Calculate Path"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRecent.setTitle(_translate("MainWindow", "Recent"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSetting.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save As..."))
        self.actionPrefrences.setText(_translate("MainWindow", "Preferences..."))
        self.actionDraw.setText(_translate("MainWindow", "Draw"))
        self.actionSet_Start_Point.setText(_translate("MainWindow", "Set Start Point"))
        self.actionErase.setText(_translate("MainWindow", "Erase"))
        self.actionPan.setText(_translate("MainWindow", "Pan"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actiontest_path.setText(_translate("MainWindow", "test.path"))
from grid_frame import GridFrame