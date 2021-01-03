# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowMXpSju.ui'
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
        icon = QIcon()
        iconThemeName = u"plopy_16x16.png"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.action_load_data_file = QAction(MainWindow)
        self.action_load_data_file.setObjectName(u"action_load_data_file")
        self.action_save_plot = QAction(MainWindow)
        self.action_save_plot.setObjectName(u"action_save_plot")
        self.action_plot_options_load_data_file = QAction(MainWindow)
        self.action_plot_options_load_data_file.setObjectName(u"action_plot_options_load_data_file")
        self.action_figure_options = QAction(MainWindow)
        self.action_figure_options.setObjectName(u"action_figure_options")
        self.action_copy_plot = QAction(MainWindow)
        self.action_copy_plot.setObjectName(u"action_copy_plot")
        self.action_whatsthis = QAction(MainWindow)
        self.action_whatsthis.setObjectName(u"action_whatsthis")
        self.action_website = QAction(MainWindow)
        self.action_website.setObjectName(u"action_website")
        self.action_load_data_file_set_format = QAction(MainWindow)
        self.action_load_data_file_set_format.setObjectName(u"action_load_data_file_set_format")
        self.action_docs = QAction(MainWindow)
        self.action_docs.setObjectName(u"action_docs")
        self.action_load_data_file_advanced = QAction(MainWindow)
        self.action_load_data_file_advanced.setObjectName(u"action_load_data_file_advanced")
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
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_plot_options = QMenu(self.menu_edit)
        self.menu_plot_options.setObjectName(u"menu_plot_options")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_load_data_file)
        self.menu_file.addAction(self.action_load_data_file_set_format)
        self.menu_file.addAction(self.action_load_data_file_advanced)
        self.menu_file.addAction(self.action_save_plot)
        self.menu_file.addAction(self.action_copy_plot)
        self.menu_edit.addAction(self.action_figure_options)
        self.menu_edit.addAction(self.menu_plot_options.menuAction())
        self.menu_plot_options.addAction(self.action_plot_options_load_data_file)
        self.menu_help.addAction(self.action_whatsthis)
        self.menu_help.addAction(self.action_website)
        self.menu_help.addAction(self.action_docs)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plo.Py", None))
        self.action_load_data_file.setText(QCoreApplication.translate("MainWindow", u"Load Data File...", None))
#if QT_CONFIG(statustip)
        self.action_load_data_file.setStatusTip(QCoreApplication.translate("MainWindow", u"Add one or more data files to be plotted, each with their own options pane", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_load_data_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_plot.setText(QCoreApplication.translate("MainWindow", u"Save Plot...", None))
#if QT_CONFIG(statustip)
        self.action_save_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the current plot as an image, PDF, or similar format", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_save_plot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_plot_options_load_data_file.setText(QCoreApplication.translate("MainWindow", u"Load a Data File first...", None))
        self.action_figure_options.setText(QCoreApplication.translate("MainWindow", u"Figure + Axes Options", None))
#if QT_CONFIG(statustip)
        self.action_figure_options.setStatusTip(QCoreApplication.translate("MainWindow", u"Options relating to the whole figure or to an axes, such as the title or scale", None))
#endif // QT_CONFIG(statustip)
        self.action_copy_plot.setText(QCoreApplication.translate("MainWindow", u"Copy Plot to Clipboard", None))
#if QT_CONFIG(statustip)
        self.action_copy_plot.setStatusTip(QCoreApplication.translate("MainWindow", u"Copy the current plot as an image to the clipboard", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_copy_plot.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_whatsthis.setText(QCoreApplication.translate("MainWindow", u"WhatsThis", None))
#if QT_CONFIG(tooltip)
        self.action_whatsthis.setToolTip(QCoreApplication.translate("MainWindow", u"Get detailed info by clicking on a GUI element", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_whatsthis.setStatusTip(QCoreApplication.translate("MainWindow", u"Get detailed info by clicking on a GUI element", None))
#endif // QT_CONFIG(statustip)
        self.action_website.setText(QCoreApplication.translate("MainWindow", u"Plo.Py Website", None))
#if QT_CONFIG(tooltip)
        self.action_website.setToolTip(QCoreApplication.translate("MainWindow", u"https://finnventor.github.io/python/#plopy", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_website.setStatusTip(QCoreApplication.translate("MainWindow", u"https://finnventor.github.io/python/#plopy", None))
#endif // QT_CONFIG(statustip)
        self.action_load_data_file_set_format.setText(QCoreApplication.translate("MainWindow", u"Choose Input Date Format...", None))
#if QT_CONFIG(statustip)
        self.action_load_data_file_set_format.setStatusTip(QCoreApplication.translate("MainWindow", u"Change the date format for reading input files (default: Year Month Day)", None))
#endif // QT_CONFIG(statustip)
        self.action_docs.setText(QCoreApplication.translate("MainWindow", u"Plo.Py Docs", None))
#if QT_CONFIG(tooltip)
        self.action_docs.setToolTip(QCoreApplication.translate("MainWindow", u"https://plopy.readthedocs.io/", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_docs.setStatusTip(QCoreApplication.translate("MainWindow", u"https://plopy.readthedocs.io/", None))
#endif // QT_CONFIG(statustip)
        self.action_load_data_file_advanced.setText(QCoreApplication.translate("MainWindow", u"Load Data File with Fast Date Processing...", None))
#if QT_CONFIG(statustip)
        self.action_load_data_file_advanced.setStatusTip(QCoreApplication.translate("MainWindow", u"Advanced Add Data File dialog to process dates faster by manually specifying the format", None))
#endif // QT_CONFIG(statustip)
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(statustip)
        self.menu_plot_options.setStatusTip(QCoreApplication.translate("MainWindow", u"Options relating to a specific file or line, including the color or legend label", None))
#endif // QT_CONFIG(statustip)
        self.menu_plot_options.setTitle(QCoreApplication.translate("MainWindow", u"Plot + Line Options", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

