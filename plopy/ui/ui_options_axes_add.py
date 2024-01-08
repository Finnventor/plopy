# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_axes_addlmRXje.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_AddAxesOptions(object):
    def setupUi(self, AddAxesOptions):
        if not AddAxesOptions.objectName():
            AddAxesOptions.setObjectName(u"AddAxesOptions")
        AddAxesOptions.resize(322, 229)
        AddAxesOptions.setModal(True)
        self.gridLayout_2 = QGridLayout(AddAxesOptions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.index_box = QWidget(AddAxesOptions)
        self.index_box.setObjectName(u"index_box")
        self.verticalLayout = QVBoxLayout(self.index_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.index_label = QLabel(self.index_box)
        self.index_label.setObjectName(u"index_label")
        self.index_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.index_label)

        self.index = QSpinBox(self.index_box)
        self.index.setObjectName(u"index")
        self.index.setWrapping(True)
        self.index.setMinimum(1)
        self.index.setMaximum(999)

        self.verticalLayout.addWidget(self.index)


        self.gridLayout_2.addWidget(self.index_box, 0, 1, 1, 1)

        self.dimensions_box = QGroupBox(AddAxesOptions)
        self.dimensions_box.setObjectName(u"dimensions_box")
        self.gridLayout = QGridLayout(self.dimensions_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 3, -1, -1)
        self.nrows_label = QLabel(self.dimensions_box)
        self.nrows_label.setObjectName(u"nrows_label")

        self.gridLayout.addWidget(self.nrows_label, 0, 0, 1, 1)

        self.ncols_label = QLabel(self.dimensions_box)
        self.ncols_label.setObjectName(u"ncols_label")

        self.gridLayout.addWidget(self.ncols_label, 0, 1, 1, 1)

        self.nrows = QSpinBox(self.dimensions_box)
        self.nrows.setObjectName(u"nrows")
        self.nrows.setMinimum(1)

        self.gridLayout.addWidget(self.nrows, 1, 0, 1, 1)

        self.ncols = QSpinBox(self.dimensions_box)
        self.ncols.setObjectName(u"ncols")
        self.ncols.setMinimum(1)

        self.gridLayout.addWidget(self.ncols, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.dimensions_box, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddAxesOptions)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.radio_twiny = QRadioButton(AddAxesOptions)
        self.radio_twiny.setObjectName(u"radio_twiny")
        self.radio_twiny.setEnabled(False)

        self.gridLayout_2.addWidget(self.radio_twiny, 3, 0, 1, 2)

        self.radio_twinx = QRadioButton(AddAxesOptions)
        self.radio_twinx.setObjectName(u"radio_twinx")
        self.radio_twinx.setEnabled(False)

        self.gridLayout_2.addWidget(self.radio_twinx, 2, 0, 1, 2)

        self.radio_new = QRadioButton(AddAxesOptions)
        self.radio_new.setObjectName(u"radio_new")
        self.radio_new.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_new, 1, 0, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        QWidget.setTabOrder(self.nrows, self.ncols)
        QWidget.setTabOrder(self.ncols, self.index)
        QWidget.setTabOrder(self.index, self.radio_new)
        QWidget.setTabOrder(self.radio_new, self.radio_twinx)
        QWidget.setTabOrder(self.radio_twinx, self.radio_twiny)

        self.retranslateUi(AddAxesOptions)
        self.buttonBox.accepted.connect(AddAxesOptions.accept)
        self.buttonBox.rejected.connect(AddAxesOptions.reject)

        QMetaObject.connectSlotsByName(AddAxesOptions)
    # setupUi

    def retranslateUi(self, AddAxesOptions):
        AddAxesOptions.setWindowTitle(QCoreApplication.translate("AddAxesOptions", u"Plo.Py - Add Axes", None))
        self.index_label.setText(QCoreApplication.translate("AddAxesOptions", u"Index of\n"
"the new Axes", None))
        self.dimensions_box.setTitle(QCoreApplication.translate("AddAxesOptions", u"Grid dimensions (all axes)", None))
        self.nrows_label.setText(QCoreApplication.translate("AddAxesOptions", u"Rows", None))
        self.ncols_label.setText(QCoreApplication.translate("AddAxesOptions", u"Columns", None))
#if QT_CONFIG(tooltip)
        self.radio_twiny.setToolTip(QCoreApplication.translate("AddAxesOptions", u"Add a new Axes with a shared y axis and a unique x axis", None))
#endif // QT_CONFIG(tooltip)
        self.radio_twiny.setText(QCoreApplication.translate("AddAxesOptions", u"Add Twin Y", None))
#if QT_CONFIG(tooltip)
        self.radio_twinx.setToolTip(QCoreApplication.translate("AddAxesOptions", u"Add a new Axes with a shared x axis and a unique y axis", None))
#endif // QT_CONFIG(tooltip)
        self.radio_twinx.setText(QCoreApplication.translate("AddAxesOptions", u"Add Twin X", None))
        self.radio_new.setText(QCoreApplication.translate("AddAxesOptions", u"New", None))
    # retranslateUi

