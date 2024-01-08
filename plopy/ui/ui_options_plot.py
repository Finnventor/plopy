# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_plotMEziAb.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_PlotOptions(object):
    def setupUi(self, PlotOptions):
        if not PlotOptions.objectName():
            PlotOptions.setObjectName(u"PlotOptions")
        PlotOptions.resize(220, 127)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlotOptions.sizePolicy().hasHeightForWidth())
        PlotOptions.setSizePolicy(sizePolicy)
        PlotOptions.setFloating(True)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(self.dockWidgetContents)
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

        self.button_box = QWidget(self.dockWidgetContents)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(2, 1)
        PlotOptions.setWidget(self.dockWidgetContents)

        self.retranslateUi(PlotOptions)

        self.tab_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(PlotOptions)
    # setupUi

    def retranslateUi(self, PlotOptions):
        self.line_button.setText(QCoreApplication.translate("PlotOptions", u"Add Line Plot", None))
        self.detail_button.setText(QCoreApplication.translate("PlotOptions", u"View Data", None))
        pass
    # retranslateUi

