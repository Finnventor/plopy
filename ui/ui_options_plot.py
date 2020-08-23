# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_plotCrSAfP.ui'
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


class Ui_PlotOptions(object):
    def setupUi(self, PlotOptions):
        if not PlotOptions.objectName():
            PlotOptions.setObjectName(u"PlotOptions")
        PlotOptions.resize(460, 279)
        PlotOptions.setSizeGripEnabled(False)
        PlotOptions.setModal(False)
        self.verticalLayout = QVBoxLayout(PlotOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(PlotOptions)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setAutoFillBackground(False)
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.setTabShape(QTabWidget.Rounded)
        self.tab_widget.setElideMode(Qt.ElideNone)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.setTabBarAutoHide(False)

        self.verticalLayout.addWidget(self.tab_widget)

        self.button_box = QWidget(PlotOptions)
        self.button_box.setObjectName(u"button_box")
        self.horizontalLayout = QHBoxLayout(self.button_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.line_button = QPushButton(self.button_box)
        self.line_button.setObjectName(u"line_button")

        self.horizontalLayout.addWidget(self.line_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.detail_button = QPushButton(self.button_box)
        self.detail_button.setObjectName(u"detail_button")

        self.horizontalLayout.addWidget(self.detail_button)


        self.verticalLayout.addWidget(self.button_box)

        self.dialog_button_box = QDialogButtonBox(PlotOptions)
        self.dialog_button_box.setObjectName(u"dialog_button_box")
        self.dialog_button_box.setOrientation(Qt.Horizontal)
        self.dialog_button_box.setStandardButtons(QDialogButtonBox.Close)
        self.dialog_button_box.setCenterButtons(False)

        self.verticalLayout.addWidget(self.dialog_button_box)

        QWidget.setTabOrder(self.tab_widget, self.line_button)
        QWidget.setTabOrder(self.line_button, self.detail_button)

        self.retranslateUi(PlotOptions)
        self.dialog_button_box.rejected.connect(PlotOptions.reject)

        self.tab_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(PlotOptions)
    # setupUi

    def retranslateUi(self, PlotOptions):
        self.line_button.setText(QCoreApplication.translate("PlotOptions", u"Add Line Plot", None))
        self.detail_button.setText(QCoreApplication.translate("PlotOptions", u"Details", None))
        pass
    # retranslateUi

