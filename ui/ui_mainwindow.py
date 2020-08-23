# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowLBnTqT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.actionOpen_Data_File = QAction(MainWindow)
        self.actionOpen_Data_File.setObjectName(u"actionOpen_Data_File")
        self.actionSave_Plot = QAction(MainWindow)
        self.actionSave_Plot.setObjectName(u"actionSave_Plot")
        self.actionGrid = QAction(MainWindow)
        self.actionGrid.setObjectName(u"actionGrid")
        self.actionGrid.setCheckable(True)
        self.actionGrid.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionPlot_Options_Open_Data_File = QAction(MainWindow)
        self.actionPlot_Options_Open_Data_File.setObjectName(u"actionPlot_Options_Open_Data_File")
        self.actionAuto = QAction(MainWindow)
        self.actionAuto.setObjectName(u"actionAuto")
        self.actionAuto.setCheckable(True)
        self.actionTop_Right = QAction(MainWindow)
        self.actionTop_Right.setObjectName(u"actionTop_Right")
        self.actionTop_Right.setCheckable(True)
        self.actionTop_Left = QAction(MainWindow)
        self.actionTop_Left.setObjectName(u"actionTop_Left")
        self.actionTop_Left.setCheckable(True)
        self.actionBottom_Right = QAction(MainWindow)
        self.actionBottom_Right.setObjectName(u"actionBottom_Right")
        self.actionBottom_Right.setCheckable(True)
        self.actionBottom_Left = QAction(MainWindow)
        self.actionBottom_Left.setObjectName(u"actionBottom_Left")
        self.actionBottom_Left.setCheckable(True)
        self.actionLeft = QAction(MainWindow)
        self.actionLeft.setObjectName(u"actionLeft")
        self.actionLeft.setCheckable(True)
        self.actionRight = QAction(MainWindow)
        self.actionRight.setObjectName(u"actionRight")
        self.actionRight.setCheckable(True)
        self.actionTop = QAction(MainWindow)
        self.actionTop.setObjectName(u"actionTop")
        self.actionTop.setCheckable(True)
        self.actionBottom = QAction(MainWindow)
        self.actionBottom.setObjectName(u"actionBottom")
        self.actionBottom.setCheckable(True)
        self.actionCenter = QAction(MainWindow)
        self.actionCenter.setObjectName(u"actionCenter")
        self.actionCenter.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuPlot_Options = QMenu(self.menuEdit)
        self.menuPlot_Options.setObjectName(u"menuPlot_Options")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen_Data_File)
        self.menuFile.addAction(self.actionSave_Plot)
        self.menuEdit.addAction(self.menuPlot_Options.menuAction())
        self.menuPlot_Options.addAction(self.actionPlot_Options_Open_Data_File)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plo.Py", None))
        self.actionOpen_Data_File.setText(QCoreApplication.translate("MainWindow", u"Add Data File...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Data_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Plot.setText(QCoreApplication.translate("MainWindow", u"Save Plot...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Plot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.actionPlot_Options_Open_Data_File.setText(QCoreApplication.translate("MainWindow", u"Choose a file first...", None))
        self.actionAuto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.actionTop_Right.setText(QCoreApplication.translate("MainWindow", u"Top Right", None))
        self.actionTop_Left.setText(QCoreApplication.translate("MainWindow", u"Top Left", None))
        self.actionBottom_Right.setText(QCoreApplication.translate("MainWindow", u"Bottom Right", None))
        self.actionBottom_Left.setText(QCoreApplication.translate("MainWindow", u"Bottom Left", None))
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.actionTop.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.actionBottom.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.actionCenter.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuPlot_Options.setTitle(QCoreApplication.translate("MainWindow", u"Plot Options", None))
    # retranslateUi

