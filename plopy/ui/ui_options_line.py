# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_lineCTpCwK.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_LineOptions(object):
    def setupUi(self, LineOptions):
        if not LineOptions.objectName():
            LineOptions.setObjectName(u"LineOptions")
        LineOptions.resize(461, 137)
        self.gridLayout = QGridLayout(LineOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.x_column = QComboBox(LineOptions)
        self.x_column.setObjectName(u"x_column")

        self.gridLayout.addWidget(self.x_column, 1, 1, 1, 1)

        self.label_6 = QLabel(LineOptions)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.marker_format = QComboBox(LineOptions)
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.addItem("")
        self.marker_format.setObjectName(u"marker_format")

        self.gridLayout.addWidget(self.marker_format, 3, 3, 1, 1)

        self.line_format = QComboBox(LineOptions)
        self.line_format.addItem("")
        self.line_format.addItem("")
        self.line_format.addItem("")
        self.line_format.addItem("")
        self.line_format.addItem("")
        self.line_format.setObjectName(u"line_format")

        self.gridLayout.addWidget(self.line_format, 3, 1, 1, 1)

        self.label_5 = QLabel(LineOptions)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.marker_size_widget = QWidget(LineOptions)
        self.marker_size_widget.setObjectName(u"marker_size_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.marker_size_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.marker_size_widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.marker_size = QSpinBox(self.marker_size_widget)
        self.marker_size.setObjectName(u"marker_size")
        self.marker_size.setWrapping(False)
        self.marker_size.setFrame(True)
        self.marker_size.setReadOnly(False)
        self.marker_size.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.marker_size.setSingleStep(2)
        self.marker_size.setValue(1)

        self.horizontalLayout_3.addWidget(self.marker_size)


        self.gridLayout.addWidget(self.marker_size_widget, 4, 2, 1, 2)

        self.label_2 = QLabel(LineOptions)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(LineOptions)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label = QLabel(LineOptions)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.legend_label = QLineEdit(LineOptions)
        self.legend_label.setObjectName(u"legend_label")
        self.legend_label.setReadOnly(False)
        self.legend_label.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.legend_label, 0, 1, 1, 4)

        self.color_frame = QFrame(LineOptions)
        self.color_frame.setObjectName(u"color_frame")
        self.color_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.color_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.set_color = QPushButton(self.color_frame)
        self.set_color.setObjectName(u"set_color")

        self.verticalLayout.addWidget(self.set_color)


        self.gridLayout.addWidget(self.color_frame, 3, 4, 1, 1)

        self.y_column = QComboBox(LineOptions)
        self.y_column.setObjectName(u"y_column")

        self.gridLayout.addWidget(self.y_column, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.line_width_widget = QWidget(LineOptions)
        self.line_width_widget.setObjectName(u"line_width_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.line_width_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.line_width_widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.line_width = QDoubleSpinBox(self.line_width_widget)
        self.line_width.setObjectName(u"line_width")
        self.line_width.setWrapping(False)
        self.line_width.setFrame(True)
        self.line_width.setReadOnly(False)
        self.line_width.setDecimals(1)
        self.line_width.setSingleStep(0.500000000000000)
        self.line_width.setStepType(QAbstractSpinBox.DefaultStepType)
        self.line_width.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.line_width)


        self.gridLayout.addWidget(self.line_width_widget, 4, 0, 1, 2)

        self.axes_select = QComboBox(LineOptions)
        self.axes_select.setObjectName(u"axes_select")

        self.gridLayout.addWidget(self.axes_select, 1, 4, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_6.setBuddy(self.marker_format)
        self.label_5.setBuddy(self.line_format)
        self.label_7.setBuddy(self.marker_size)
        self.label_2.setBuddy(self.x_column)
        self.label_3.setBuddy(self.y_column)
        self.label.setBuddy(self.legend_label)
        self.label_4.setBuddy(self.line_width)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.legend_label, self.x_column)
        QWidget.setTabOrder(self.x_column, self.y_column)
        QWidget.setTabOrder(self.y_column, self.line_format)
        QWidget.setTabOrder(self.line_format, self.marker_format)
        QWidget.setTabOrder(self.marker_format, self.set_color)
        QWidget.setTabOrder(self.set_color, self.line_width)
        QWidget.setTabOrder(self.line_width, self.marker_size)

        self.retranslateUi(LineOptions)

        self.marker_format.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(LineOptions)
    # setupUi

    def retranslateUi(self, LineOptions):
        LineOptions.setWindowTitle(QCoreApplication.translate("LineOptions", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("LineOptions", u"Marker:", None))
        self.marker_format.setItemText(0, QCoreApplication.translate("LineOptions", u"Circle          \u2b24", None))
        self.marker_format.setItemText(1, QCoreApplication.translate("LineOptions", u"Triangle      \u25b2", None))
        self.marker_format.setItemText(2, QCoreApplication.translate("LineOptions", u"Square        \u25a0", None))
        self.marker_format.setItemText(3, QCoreApplication.translate("LineOptions", u"Pentagon    \u2b1f", None))
        self.marker_format.setItemText(4, QCoreApplication.translate("LineOptions", u"Hexagon     \u2b22", None))
        self.marker_format.setItemText(5, QCoreApplication.translate("LineOptions", u"Star            \u2605", None))
        self.marker_format.setItemText(6, QCoreApplication.translate("LineOptions", u"Cross          +", None))
        self.marker_format.setItemText(7, QCoreApplication.translate("LineOptions", u"Point           \u25cf", None))
        self.marker_format.setItemText(8, QCoreApplication.translate("LineOptions", u"Pixel            \u00b7", None))
        self.marker_format.setItemText(9, QCoreApplication.translate("LineOptions", u"None", None))

        self.marker_format.setCurrentText(QCoreApplication.translate("LineOptions", u"None", None))
        self.line_format.setItemText(0, QCoreApplication.translate("LineOptions", u"Solid           \u2014", None))
        self.line_format.setItemText(1, QCoreApplication.translate("LineOptions", u"Dashed      - -", None))
        self.line_format.setItemText(2, QCoreApplication.translate("LineOptions", u"Dotted       \u00b7\u00b7", None))
        self.line_format.setItemText(3, QCoreApplication.translate("LineOptions", u"Dash-dot   -\u00b7", None))
        self.line_format.setItemText(4, QCoreApplication.translate("LineOptions", u"None", None))

        self.label_5.setText(QCoreApplication.translate("LineOptions", u"Line:", None))
        self.label_7.setText(QCoreApplication.translate("LineOptions", u"Marker Size", None))
        self.label_2.setText(QCoreApplication.translate("LineOptions", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("LineOptions", u"Y:", None))
        self.label.setText(QCoreApplication.translate("LineOptions", u"Label", None))
#if QT_CONFIG(whatsthis)
        self.legend_label.setWhatsThis(QCoreApplication.translate("LineOptions", u"The label the line has in the legend.\n"
"Leave blank to prevent this line from appearing in the legend.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.color_frame.setWhatsThis(QCoreApplication.translate("LineOptions", u"Sets the line color.\n"
"The current color should appear as\n"
"an outline surrounding the button.", None))
#endif // QT_CONFIG(whatsthis)
        self.set_color.setText(QCoreApplication.translate("LineOptions", u"Set Color", None))
        self.label_4.setText(QCoreApplication.translate("LineOptions", u"Line Width", None))
    # retranslateUi

