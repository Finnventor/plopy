# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_axesYiOVzz.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AxesOptions(object):
    def setupUi(self, AxesOptions):
        if not AxesOptions.objectName():
            AxesOptions.setObjectName(u"AxesOptions")
        AxesOptions.resize(528, 205)
        self.gridLayout = QGridLayout(AxesOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.y_gbox = QGroupBox(AxesOptions)
        self.y_gbox.setObjectName(u"y_gbox")
        self.formLayout_4 = QFormLayout(self.y_gbox)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.y_label_label = QLabel(self.y_gbox)
        self.y_label_label.setObjectName(u"y_label_label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.y_label_label)

        self.y_label = QLineEdit(self.y_gbox)
        self.y_label.setObjectName(u"y_label")
        self.y_label.setClearButtonEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.y_label)

        self.y_tick_type_label = QLabel(self.y_gbox)
        self.y_tick_type_label.setObjectName(u"y_tick_type_label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.y_tick_type_label)

        self.y_tick_type = QComboBox(self.y_gbox)
        self.y_tick_type.addItem("")
        self.y_tick_type.addItem("")
        self.y_tick_type.addItem("")
        self.y_tick_type.addItem("")
        self.y_tick_type.addItem("")
        self.y_tick_type.addItem("")
        self.y_tick_type.setObjectName(u"y_tick_type")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.y_tick_type)


        self.gridLayout.addWidget(self.y_gbox, 1, 2, 1, 2)

        self.title_frame = QFrame(AxesOptions)
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


        self.gridLayout.addWidget(self.title_frame, 0, 0, 1, 4)

        self.legend_loc_label = QLabel(AxesOptions)
        self.legend_loc_label.setObjectName(u"legend_loc_label")

        self.gridLayout.addWidget(self.legend_loc_label, 3, 0, 1, 1)

        self.equal_aspect = QCheckBox(AxesOptions)
        self.equal_aspect.setObjectName(u"equal_aspect")

        self.gridLayout.addWidget(self.equal_aspect, 3, 3, 1, 1)

        self.x_gbox = QGroupBox(AxesOptions)
        self.x_gbox.setObjectName(u"x_gbox")
        self.formLayout = QFormLayout(self.x_gbox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 3, -1, -1)
        self.x_label_label = QLabel(self.x_gbox)
        self.x_label_label.setObjectName(u"x_label_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.x_label_label)

        self.x_label = QLineEdit(self.x_gbox)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_label)

        self.x_tick_type_label = QLabel(self.x_gbox)
        self.x_tick_type_label.setObjectName(u"x_tick_type_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.x_tick_type_label)

        self.x_tick_type = QComboBox(self.x_gbox)
        self.x_tick_type.addItem("")
        self.x_tick_type.addItem("")
        self.x_tick_type.addItem("")
        self.x_tick_type.addItem("")
        self.x_tick_type.addItem("")
        self.x_tick_type.addItem("")
        self.x_tick_type.setObjectName(u"x_tick_type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.x_tick_type)


        self.gridLayout.addWidget(self.x_gbox, 1, 0, 1, 2)

        self.legend_loc = QComboBox(AxesOptions)
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.addItem("")
        self.legend_loc.setObjectName(u"legend_loc")

        self.gridLayout.addWidget(self.legend_loc, 3, 1, 1, 1)

        self.frame = QCheckBox(AxesOptions)
        self.frame.setObjectName(u"frame")
        self.frame.setChecked(True)

        self.gridLayout.addWidget(self.frame, 2, 2, 1, 1)

        self.grid = QCheckBox(AxesOptions)
        self.grid.setObjectName(u"grid")
        self.grid.setFocusPolicy(Qt.TabFocus)

        self.gridLayout.addWidget(self.grid, 3, 2, 1, 1)

        self.configure_limits = QPushButton(AxesOptions)
        self.configure_limits.setObjectName(u"configure_limits")

        self.gridLayout.addWidget(self.configure_limits, 2, 3, 1, 1)

        self.tick_direction_label = QLabel(AxesOptions)
        self.tick_direction_label.setObjectName(u"tick_direction_label")

        self.gridLayout.addWidget(self.tick_direction_label, 2, 0, 1, 1)

        self.tick_direction = QComboBox(AxesOptions)
        self.tick_direction.addItem("")
        self.tick_direction.addItem("")
        self.tick_direction.addItem("")
        self.tick_direction.setObjectName(u"tick_direction")

        self.gridLayout.addWidget(self.tick_direction, 2, 1, 1, 1)

#if QT_CONFIG(shortcut)
        self.y_label_label.setBuddy(self.y_label)
        self.y_tick_type_label.setBuddy(self.y_tick_type)
        self.title_label.setBuddy(self.title)
        self.legend_loc_label.setBuddy(self.legend_loc)
        self.x_label_label.setBuddy(self.x_label)
        self.x_tick_type_label.setBuddy(self.x_tick_type)
        self.tick_direction_label.setBuddy(self.tick_direction)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.title, self.x_label)
        QWidget.setTabOrder(self.x_label, self.y_label)
        QWidget.setTabOrder(self.y_label, self.x_tick_type)
        QWidget.setTabOrder(self.x_tick_type, self.y_tick_type)
        QWidget.setTabOrder(self.y_tick_type, self.tick_direction)
        QWidget.setTabOrder(self.tick_direction, self.frame)
        QWidget.setTabOrder(self.frame, self.configure_limits)
        QWidget.setTabOrder(self.configure_limits, self.legend_loc)
        QWidget.setTabOrder(self.legend_loc, self.grid)
        QWidget.setTabOrder(self.grid, self.equal_aspect)

        self.retranslateUi(AxesOptions)

        QMetaObject.connectSlotsByName(AxesOptions)
    # setupUi

    def retranslateUi(self, AxesOptions):
        self.y_gbox.setTitle(QCoreApplication.translate("AxesOptions", u"Y-Axis", None))
        self.y_label_label.setText(QCoreApplication.translate("AxesOptions", u"Label", None))
        self.y_tick_type_label.setText(QCoreApplication.translate("AxesOptions", u"Type", None))
        self.y_tick_type.setItemText(0, QCoreApplication.translate("AxesOptions", u"Normal", None))
        self.y_tick_type.setItemText(1, QCoreApplication.translate("AxesOptions", u"Normal, minor ticks", None))
        self.y_tick_type.setItemText(2, QCoreApplication.translate("AxesOptions", u"Date", None))
        self.y_tick_type.setItemText(3, QCoreApplication.translate("AxesOptions", u"Symmetric Logarithmic", None))
        self.y_tick_type.setItemText(4, QCoreApplication.translate("AxesOptions", u"Logarithmic", None))
        self.y_tick_type.setItemText(5, QCoreApplication.translate("AxesOptions", u"Blank", None))

        self.title_label.setText(QCoreApplication.translate("AxesOptions", u"Axes Title:", None))
        self.legend_loc_label.setText(QCoreApplication.translate("AxesOptions", u"Legend Location:", None))
        self.equal_aspect.setText(QCoreApplication.translate("AxesOptions", u"1:1 Aspect Ratio", None))
        self.x_gbox.setTitle(QCoreApplication.translate("AxesOptions", u"X-Axis", None))
        self.x_label_label.setText(QCoreApplication.translate("AxesOptions", u"Label", None))
        self.x_tick_type_label.setText(QCoreApplication.translate("AxesOptions", u"Type", None))
        self.x_tick_type.setItemText(0, QCoreApplication.translate("AxesOptions", u"Normal", None))
        self.x_tick_type.setItemText(1, QCoreApplication.translate("AxesOptions", u"Normal, minor ticks", None))
        self.x_tick_type.setItemText(2, QCoreApplication.translate("AxesOptions", u"Date", None))
        self.x_tick_type.setItemText(3, QCoreApplication.translate("AxesOptions", u"Symmetric Logarithmic", None))
        self.x_tick_type.setItemText(4, QCoreApplication.translate("AxesOptions", u"Logarithmic", None))
        self.x_tick_type.setItemText(5, QCoreApplication.translate("AxesOptions", u"Blank", None))

        self.legend_loc.setItemText(0, QCoreApplication.translate("AxesOptions", u"Auto", None))
        self.legend_loc.setItemText(1, QCoreApplication.translate("AxesOptions", u"Top Right", None))
        self.legend_loc.setItemText(2, QCoreApplication.translate("AxesOptions", u"Top Left", None))
        self.legend_loc.setItemText(3, QCoreApplication.translate("AxesOptions", u"Bottom Right", None))
        self.legend_loc.setItemText(4, QCoreApplication.translate("AxesOptions", u"Bottom Left", None))
        self.legend_loc.setItemText(5, QCoreApplication.translate("AxesOptions", u"Top", None))
        self.legend_loc.setItemText(6, QCoreApplication.translate("AxesOptions", u"Bottom", None))
        self.legend_loc.setItemText(7, QCoreApplication.translate("AxesOptions", u"Right", None))
        self.legend_loc.setItemText(8, QCoreApplication.translate("AxesOptions", u"Left", None))
        self.legend_loc.setItemText(9, QCoreApplication.translate("AxesOptions", u"Center", None))

        self.frame.setText(QCoreApplication.translate("AxesOptions", u"Frame", None))
        self.grid.setText(QCoreApplication.translate("AxesOptions", u"Grid", None))
        self.configure_limits.setText(QCoreApplication.translate("AxesOptions", u"Configure Limits", None))
        self.tick_direction_label.setText(QCoreApplication.translate("AxesOptions", u"Tick Direction:", None))
        self.tick_direction.setItemText(0, QCoreApplication.translate("AxesOptions", u"Outwards", None))
        self.tick_direction.setItemText(1, QCoreApplication.translate("AxesOptions", u"Inwards", None))
        self.tick_direction.setItemText(2, QCoreApplication.translate("AxesOptions", u"Both", None))

        pass
    # retranslateUi

