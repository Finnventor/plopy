# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_figurenIkflI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDockWidget, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_FigureOptions(object):
    def setupUi(self, FigureOptions):
        if not FigureOptions.objectName():
            FigureOptions.setObjectName(u"FigureOptions")
        FigureOptions.resize(320, 140)
        FigureOptions.setFloating(True)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.axes_button = QPushButton(self.dockWidgetContents)
        self.axes_button.setObjectName(u"axes_button")

        self.gridLayout.addWidget(self.axes_button, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(226, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.tab_widget = QTabWidget(self.dockWidgetContents)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.setTabsClosable(True)

        self.gridLayout.addWidget(self.tab_widget, 1, 0, 1, 3)

        self.title_frame = QFrame(self.dockWidgetContents)
        self.title_frame.setObjectName(u"title_frame")
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout.addWidget(self.title_label)

        self.title = QLineEdit(self.title_frame)
        self.title.setObjectName(u"title")
        self.title.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.title)


        self.gridLayout.addWidget(self.title_frame, 0, 0, 1, 3)

        self.tight_layout = QCheckBox(self.dockWidgetContents)
        self.tight_layout.setObjectName(u"tight_layout")

        self.gridLayout.addWidget(self.tight_layout, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(3, 1)
        FigureOptions.setWidget(self.dockWidgetContents)

        self.retranslateUi(FigureOptions)

        self.tab_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(FigureOptions)
    # setupUi

    def retranslateUi(self, FigureOptions):
        FigureOptions.setWindowTitle(QCoreApplication.translate("FigureOptions", u"Figure + Axes Options", None))
        self.axes_button.setText(QCoreApplication.translate("FigureOptions", u"Add Axes", None))
        self.title_label.setText(QCoreApplication.translate("FigureOptions", u"Figure Title:", None))
        self.tight_layout.setText(QCoreApplication.translate("FigureOptions", u"Auto Layout", None))
    # retranslateUi

