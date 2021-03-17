# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/histogram_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_histogram(object):
    def setupUi(self, view_histogram):
        view_histogram.setObjectName("view_histogram")
        view_histogram.resize(400, 300)
        icon = QtGui.QIcon.fromTheme("insert-image")
        view_histogram.setWindowIcon(icon)
        view_histogram.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(view_histogram)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(view_histogram)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)

        self.retranslateUi(view_histogram)
        QtCore.QMetaObject.connectSlotsByName(view_histogram)

    def retranslateUi(self, view_histogram):
        _translate = QtCore.QCoreApplication.translate
        view_histogram.setWindowTitle(_translate("view_histogram", "Photochopp - Working image histogram"))
        self.image.setText(_translate("view_histogram", "Placeholder for the working image"))

