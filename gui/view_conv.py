# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/conv_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_convolution(object):
    def setupUi(self, view_convolution):
        view_convolution.setObjectName("view_convolution")
        view_convolution.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(view_convolution.sizePolicy().hasHeightForWidth())
        view_convolution.setSizePolicy(sizePolicy)
        view_convolution.setMinimumSize(QtCore.QSize(400, 200))
        view_convolution.setMaximumSize(QtCore.QSize(400, 200))
        icon = QtGui.QIcon.fromTheme("insert-image")
        view_convolution.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(view_convolution)
        self.gridLayout.setObjectName("gridLayout")
        self.conv_select_filters = QtWidgets.QComboBox(view_convolution)
        self.conv_select_filters.setObjectName("conv_select_filters")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.conv_select_filters.addItem("")
        self.gridLayout.addWidget(self.conv_select_filters, 0, 0, 1, 1)
        self.conv_bt_load = QtWidgets.QPushButton(view_convolution)
        self.conv_bt_load.setObjectName("conv_bt_load")
        self.gridLayout.addWidget(self.conv_bt_load, 0, 1, 1, 1)
        self.conv_bt_reset = QtWidgets.QPushButton(view_convolution)
        self.conv_bt_reset.setObjectName("conv_bt_reset")
        self.gridLayout.addWidget(self.conv_bt_reset, 0, 2, 1, 1)
        self.__doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_4.setDecimals(3)
        self.__doubleSpinBox_4.setMinimum(-99.99)
        self.__doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.__doubleSpinBox_4, 3, 0, 1, 1)
        self.__doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_6.setDecimals(3)
        self.__doubleSpinBox_6.setMinimum(-99.99)
        self.__doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.__doubleSpinBox_6, 3, 2, 1, 1)
        self.__doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_5.setDecimals(3)
        self.__doubleSpinBox_5.setMinimum(-99.99)
        self.__doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.__doubleSpinBox_5, 3, 1, 1, 1)
        self.__doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_8.setDecimals(3)
        self.__doubleSpinBox_8.setMinimum(-99.99)
        self.__doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.__doubleSpinBox_8, 4, 1, 1, 1)
        self.__doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_1.setDecimals(3)
        self.__doubleSpinBox_1.setMinimum(-99.99)
        self.__doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.gridLayout.addWidget(self.__doubleSpinBox_1, 2, 0, 1, 1)
        self.__doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_7.setDecimals(3)
        self.__doubleSpinBox_7.setMinimum(-99.99)
        self.__doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.__doubleSpinBox_7, 4, 0, 1, 1)
        self.conv_line_1 = QtWidgets.QFrame(view_convolution)
        self.conv_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.conv_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.conv_line_1.setObjectName("conv_line_1")
        self.gridLayout.addWidget(self.conv_line_1, 1, 0, 1, 3)
        self.line = QtWidgets.QFrame(view_convolution)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)
        self.__doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_3.setDecimals(3)
        self.__doubleSpinBox_3.setMinimum(-99.99)
        self.__doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.__doubleSpinBox_3, 2, 2, 1, 1)
        self.__doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_9.setDecimals(3)
        self.__doubleSpinBox_9.setMinimum(-99.99)
        self.__doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout.addWidget(self.__doubleSpinBox_9, 4, 2, 1, 1)
        self.__doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(view_convolution)
        self.__doubleSpinBox_2.setDecimals(3)
        self.__doubleSpinBox_2.setMinimum(-99.99)
        self.__doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.__doubleSpinBox_2, 2, 1, 1, 1)
        self.conv_bt_convolute = QtWidgets.QPushButton(view_convolution)
        self.conv_bt_convolute.setObjectName("conv_bt_convolute")
        self.gridLayout.addWidget(self.conv_bt_convolute, 6, 0, 1, 3)

        self.retranslateUi(view_convolution)
        QtCore.QMetaObject.connectSlotsByName(view_convolution)

        self.kernel_spins = []

        self.kernel_spins.append([
            self.__doubleSpinBox_1,
            self.__doubleSpinBox_2,
            self.__doubleSpinBox_3,
        ])

        self.kernel_spins.append([
            self.__doubleSpinBox_4,
            self.__doubleSpinBox_5,
            self.__doubleSpinBox_6,
        ])

        self.kernel_spins.append([
            self.__doubleSpinBox_7,
            self.__doubleSpinBox_8,
            self.__doubleSpinBox_9,
        ])

    def retranslateUi(self, view_convolution):
        _translate = QtCore.QCoreApplication.translate
        view_convolution.setWindowTitle(_translate("view_convolution", "Convolute"))
        self.conv_select_filters.setItemText(0, _translate("view_convolution", "Gaussian"))
        self.conv_select_filters.setItemText(1, _translate("view_convolution", "Laplacian"))
        self.conv_select_filters.setItemText(2, _translate("view_convolution", "Highpass"))
        self.conv_select_filters.setItemText(3, _translate("view_convolution", "Prewitt Hx"))
        self.conv_select_filters.setItemText(4, _translate("view_convolution", "Prewitt Hy"))
        self.conv_select_filters.setItemText(5, _translate("view_convolution", "Sobel Hx"))
        self.conv_select_filters.setItemText(6, _translate("view_convolution", "Sobel Hy"))
        self.conv_bt_load.setText(_translate("view_convolution", "Load kernel"))
        self.conv_bt_reset.setText(_translate("view_convolution", "Reset"))
        self.conv_bt_convolute.setText(_translate("view_convolution", "Convolute"))

