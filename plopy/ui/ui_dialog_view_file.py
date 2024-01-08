# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_view_filePkArRQ.ui'
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
    QDialogButtonBox, QGridLayout, QHeaderView, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ViewFileDialog(object):
    def setupUi(self, ViewFileDialog):
        if not ViewFileDialog.objectName():
            ViewFileDialog.setObjectName(u"ViewFileDialog")
        ViewFileDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ViewFileDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ViewFileDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.gridLayout_2 = QGridLayout(self.tab_data)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.data_load_all = QPushButton(self.tab_data)
        self.data_load_all.setObjectName(u"data_load_all")

        self.gridLayout_2.addWidget(self.data_load_all, 1, 1, 1, 1)

        self.data_table = QTableWidget(self.tab_data)
        self.data_table.setObjectName(u"data_table")
        self.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_2.addWidget(self.data_table, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_data, "")
        self.tab_raw = QWidget()
        self.tab_raw.setObjectName(u"tab_raw")
        self.gridLayout = QGridLayout(self.tab_raw)
        self.gridLayout.setObjectName(u"gridLayout")
        self.raw_load_all = QPushButton(self.tab_raw)
        self.raw_load_all.setObjectName(u"raw_load_all")

        self.gridLayout.addWidget(self.raw_load_all, 1, 1, 1, 1)

        self.raw_text = QPlainTextEdit(self.tab_raw)
        self.raw_text.setObjectName(u"raw_text")
        self.raw_text.setUndoRedoEnabled(False)
        self.raw_text.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.raw_text.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.raw_text, 0, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_raw, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(ViewFileDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ViewFileDialog)
        self.buttonBox.rejected.connect(ViewFileDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ViewFileDialog)
    # setupUi

    def retranslateUi(self, ViewFileDialog):
#if QT_CONFIG(whatsthis)
        self.tab_data.setWhatsThis(QCoreApplication.translate("ViewFileDialog", u"A table of the first [20, 20] of data values read from the file.\n"
"Click Load All to show the whole array.", None))
#endif // QT_CONFIG(whatsthis)
        self.data_load_all.setText(QCoreApplication.translate("ViewFileDialog", u"Load All", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), QCoreApplication.translate("ViewFileDialog", u"Data (processed)", None))
#if QT_CONFIG(whatsthis)
        self.tab_raw.setWhatsThis(QCoreApplication.translate("ViewFileDialog", u"The first 20 lines of the file. Click Load All to load the whole file, though this may be slow if the file is large.", None))
#endif // QT_CONFIG(whatsthis)
        self.raw_load_all.setText(QCoreApplication.translate("ViewFileDialog", u"Load All", None))
        self.raw_text.setPlaceholderText(QCoreApplication.translate("ViewFileDialog", u"Loading...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_raw), QCoreApplication.translate("ViewFileDialog", u"File (raw)", None))
        pass
    # retranslateUi

