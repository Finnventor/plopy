# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_view_arrayhpuZPs.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ViewArrayDialog(object):
    def setupUi(self, ViewArrayDialog):
        if not ViewArrayDialog.objectName():
            ViewArrayDialog.setObjectName(u"ViewArrayDialog")
        ViewArrayDialog.resize(400, 300)
        self.gridLayout = QGridLayout(ViewArrayDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.data_load_all = QPushButton(ViewArrayDialog)
        self.data_load_all.setObjectName(u"data_load_all")

        self.gridLayout.addWidget(self.data_load_all, 1, 1, 1, 1)

        self.data_table = QTableWidget(ViewArrayDialog)
        self.data_table.setObjectName(u"data_table")
        self.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout.addWidget(self.data_table, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ViewArrayDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)


        self.retranslateUi(ViewArrayDialog)
        self.buttonBox.rejected.connect(ViewArrayDialog.reject)

        QMetaObject.connectSlotsByName(ViewArrayDialog)
    # setupUi

    def retranslateUi(self, ViewArrayDialog):
#if QT_CONFIG(whatsthis)
        ViewArrayDialog.setWhatsThis(QCoreApplication.translate("ViewArrayDialog", u"A table of the first [20, 20] of data values read from the file.\n"
"Click Load All to show the whole array.", None))
#endif // QT_CONFIG(whatsthis)
        self.data_load_all.setText(QCoreApplication.translate("ViewArrayDialog", u"Load All", None))
    # retranslateUi

