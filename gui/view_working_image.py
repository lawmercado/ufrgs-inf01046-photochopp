# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/working_image_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_working_image(object):
    def setupUi(self, view_working_image):
        view_working_image.setObjectName("view_working_image")
        view_working_image.resize(400, 300)
        icon = QtGui.QIcon.fromTheme("insert-image")
        view_working_image.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(view_working_image)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(view_working_image)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)

        self.retranslateUi(view_working_image)
        QtCore.QMetaObject.connectSlotsByName(view_working_image)

    def retranslateUi(self, view_working_image):
        _translate = QtCore.QCoreApplication.translate
        view_working_image.setWindowTitle(_translate("view_working_image", "Photochopp - Working image"))
        self.image.setText(_translate("view_working_image", "Placeholder for the working image"))

