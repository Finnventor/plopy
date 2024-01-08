# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_parserpciYvT.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ParserOptionsDialog(object):
    def setupUi(self, ParserOptionsDialog):
        if not ParserOptionsDialog.objectName():
            ParserOptionsDialog.setObjectName(u"ParserOptionsDialog")
        ParserOptionsDialog.resize(184, 118)
        self.verticalLayout_2 = QVBoxLayout(ParserOptionsDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.date_format_frame = QGroupBox(ParserOptionsDialog)
        self.date_format_frame.setObjectName(u"date_format_frame")
        self.verticalLayout = QVBoxLayout(self.date_format_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.date_format = QComboBox(self.date_format_frame)
        self.date_format.addItem("")
        self.date_format.addItem("")
        self.date_format.addItem("")
        self.date_format.addItem("")
        self.date_format.setObjectName(u"date_format")

        self.verticalLayout.addWidget(self.date_format)


        self.verticalLayout_2.addWidget(self.date_format_frame)

        self.buttonBox = QDialogButtonBox(ParserOptionsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ParserOptionsDialog)
        self.buttonBox.accepted.connect(ParserOptionsDialog.accept)
        self.buttonBox.rejected.connect(ParserOptionsDialog.reject)

        QMetaObject.connectSlotsByName(ParserOptionsDialog)
    # setupUi

    def retranslateUi(self, ParserOptionsDialog):
        ParserOptionsDialog.setWindowTitle(QCoreApplication.translate("ParserOptionsDialog", u"Plo.Py", None))
        self.date_format_frame.setTitle(QCoreApplication.translate("ParserOptionsDialog", u"Date Format", None))
        self.date_format.setItemText(0, QCoreApplication.translate("ParserOptionsDialog", u"Year Month Day", None))
        self.date_format.setItemText(1, QCoreApplication.translate("ParserOptionsDialog", u"Day Month Year", None))
        self.date_format.setItemText(2, QCoreApplication.translate("ParserOptionsDialog", u"Month Day Year", None))
        self.date_format.setItemText(3, QCoreApplication.translate("ParserOptionsDialog", u"Year Day Month", None))

    # retranslateUi

