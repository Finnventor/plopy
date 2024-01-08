# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_load_advancedHfPAfv.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_AdvancedLoadDialog(object):
    def setupUi(self, AdvancedLoadDialog):
        if not AdvancedLoadDialog.objectName():
            AdvancedLoadDialog.setObjectName(u"AdvancedLoadDialog")
        AdvancedLoadDialog.resize(447, 254)
        self.gridLayout = QGridLayout(AdvancedLoadDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.date_format_label = QLabel(AdvancedLoadDialog)
        self.date_format_label.setObjectName(u"date_format_label")
        self.date_format_label.setTextFormat(Qt.RichText)
        self.date_format_label.setWordWrap(True)
        self.date_format_label.setOpenExternalLinks(True)
        self.date_format_label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.gridLayout.addWidget(self.date_format_label, 0, 0, 1, 1)

        self.date_format = QComboBox(AdvancedLoadDialog)
        self.date_format.addItem("")
        self.date_format.addItem("")
        self.date_format.setObjectName(u"date_format")
        self.date_format.setEditable(True)

        self.gridLayout.addWidget(self.date_format, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AdvancedLoadDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.date_format_table = QTableWidget(AdvancedLoadDialog)
        if (self.date_format_table.columnCount() < 2):
            self.date_format_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.date_format_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.date_format_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.date_format_table.rowCount() < 6):
            self.date_format_table.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.date_format_table.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.date_format_table.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.date_format_table.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.date_format_table.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.date_format_table.setItem(3, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.date_format_table.setItem(4, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.date_format_table.setItem(5, 0, __qtablewidgetitem13)
        self.date_format_table.setObjectName(u"date_format_table")
        self.date_format_table.setMinimumSize(QSize(231, 205))
        self.date_format_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.date_format_table, 0, 1, 3, 1)


        self.retranslateUi(AdvancedLoadDialog)
        self.buttonBox.accepted.connect(AdvancedLoadDialog.accept)
        self.buttonBox.rejected.connect(AdvancedLoadDialog.reject)

        QMetaObject.connectSlotsByName(AdvancedLoadDialog)
    # setupUi

    def retranslateUi(self, AdvancedLoadDialog):
        AdvancedLoadDialog.setWindowTitle(QCoreApplication.translate("AdvancedLoadDialog", u"Specify Date Format", None))
        self.date_format_label.setText(QCoreApplication.translate("AdvancedLoadDialog", u"<html><head/><body><p>Enter date format using <a href=\"https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes\"><span style=\" text-decoration: underline; color:#0000ff;\">strptime format codes</span></a></p></body></html>", None))
        self.date_format.setItemText(0, QCoreApplication.translate("AdvancedLoadDialog", u"%Y-%m-%dT%H:%M:%S", None))
        self.date_format.setItemText(1, QCoreApplication.translate("AdvancedLoadDialog", u"%Y-%m-%d-%H:%M:%S", None))

        ___qtablewidgetitem = self.date_format_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Translation", None));
        ___qtablewidgetitem1 = self.date_format_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdvancedLoadDialog", u"System Time", None));
        ___qtablewidgetitem2 = self.date_format_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%Y", None));
        ___qtablewidgetitem3 = self.date_format_table.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%m", None));
        ___qtablewidgetitem4 = self.date_format_table.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%d", None));
        ___qtablewidgetitem5 = self.date_format_table.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%H", None));
        ___qtablewidgetitem6 = self.date_format_table.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%M", None));
        ___qtablewidgetitem7 = self.date_format_table.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdvancedLoadDialog", u"%S", None));

        __sortingEnabled = self.date_format_table.isSortingEnabled()
        self.date_format_table.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.date_format_table.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Year", None));
        ___qtablewidgetitem9 = self.date_format_table.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Month", None));
        ___qtablewidgetitem10 = self.date_format_table.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Day", None));
        ___qtablewidgetitem11 = self.date_format_table.item(3, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Hour", None));
        ___qtablewidgetitem12 = self.date_format_table.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Minute", None));
        ___qtablewidgetitem13 = self.date_format_table.item(5, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AdvancedLoadDialog", u"Second", None));
        self.date_format_table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

