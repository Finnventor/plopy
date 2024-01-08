# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_axes_limXZDUFZ.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_AxesLimOptions(object):
    def setupUi(self, AxesLimOptions):
        if not AxesLimOptions.objectName():
            AxesLimOptions.setObjectName(u"AxesLimOptions")
        AxesLimOptions.resize(408, 310)
        AxesLimOptions.setModal(True)
        self.gridLayout = QGridLayout(AxesLimOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.xmin = QDoubleSpinBox(AxesLimOptions)
        self.xmin.setObjectName(u"xmin")
        self.xmin.setDecimals(6)
        self.xmin.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.xmin, 3, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(AxesLimOptions)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.ymax = QDoubleSpinBox(AxesLimOptions)
        self.ymax.setObjectName(u"ymax")
        self.ymax.setDecimals(6)
        self.ymax.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.ymax, 0, 0, 1, 1)

        self.xmax = QDoubleSpinBox(AxesLimOptions)
        self.xmax.setObjectName(u"xmax")
        self.xmax.setDecimals(6)
        self.xmax.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.xmax, 3, 3, 1, 1)

        self.ymin = QDoubleSpinBox(AxesLimOptions)
        self.ymin.setObjectName(u"ymin")
        self.ymin.setDecimals(6)
        self.ymin.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.ymin, 2, 0, 1, 1)

        self.widget = QWidget(AxesLimOptions)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.load_previous = QPushButton(self.widget)
        self.load_previous.setObjectName(u"load_previous")
        self.load_previous.setEnabled(False)
        self.load_previous.setCheckable(False)
        self.load_previous.setChecked(False)

        self.horizontalLayout.addWidget(self.load_previous)

        self.load_current = QPushButton(self.widget)
        self.load_current.setObjectName(u"load_current")

        self.horizontalLayout.addWidget(self.load_current)


        self.gridLayout.addWidget(self.widget, 4, 0, 1, 4)

        self.axes_box = QLabel(AxesLimOptions)
        self.axes_box.setObjectName(u"axes_box")
        self.axes_box.setFrameShape(QFrame.Panel)
        self.axes_box.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.axes_box, 0, 1, 3, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        QWidget.setTabOrder(self.ymax, self.ymin)
        QWidget.setTabOrder(self.ymin, self.xmin)
        QWidget.setTabOrder(self.xmin, self.xmax)
        QWidget.setTabOrder(self.xmax, self.load_previous)
        QWidget.setTabOrder(self.load_previous, self.load_current)

        self.retranslateUi(AxesLimOptions)
        self.buttonBox.accepted.connect(AxesLimOptions.accept)
        self.buttonBox.rejected.connect(AxesLimOptions.reject)

        QMetaObject.connectSlotsByName(AxesLimOptions)
    # setupUi

    def retranslateUi(self, AxesLimOptions):
        AxesLimOptions.setWindowTitle(QCoreApplication.translate("AxesLimOptions", u"Configure Axes Limits", None))
        self.load_previous.setText(QCoreApplication.translate("AxesLimOptions", u"Load Previous", None))
        self.load_current.setText(QCoreApplication.translate("AxesLimOptions", u"Load Current", None))
    # retranslateUi

