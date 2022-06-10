# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_rcVYtEBc.ui'
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


class Ui_RCOptions(object):
    def setupUi(self, RCOptions):
        if not RCOptions.objectName():
            RCOptions.setObjectName(u"RCOptions")
        RCOptions.resize(400, 300)
        self.verticalLayout = QVBoxLayout(RCOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_frame = QFrame(RCOptions)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.search_frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.search_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.search_frame)

        self.treeView = QTreeView(RCOptions)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)

        self.buttonBox = QDialogButtonBox(RCOptions)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RCOptions)
        self.buttonBox.accepted.connect(RCOptions.accept)
        self.buttonBox.rejected.connect(RCOptions.reject)
        self.lineEdit.returnPressed.connect(self.pushButton.click)

        QMetaObject.connectSlotsByName(RCOptions)
    # setupUi

    def retranslateUi(self, RCOptions):
        RCOptions.setWindowTitle(QCoreApplication.translate("RCOptions", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("RCOptions", u"Search", None))
    # retranslateUi

