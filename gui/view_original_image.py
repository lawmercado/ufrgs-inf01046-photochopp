# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/original_image_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_original_image(object):
    def setupUi(self, view_original_image):
        view_original_image.setObjectName("view_original_image")
        view_original_image.resize(400, 300)
        icon = QtGui.QIcon.fromTheme("insert-image")
        view_original_image.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(view_original_image)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(view_original_image)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(view_original_image)
        QtCore.QMetaObject.connectSlotsByName(view_original_image)

    def retranslateUi(self, view_original_image):
        _translate = QtCore.QCoreApplication.translate
        view_original_image.setWindowTitle(_translate("view_original_image", "Photochopp - Original image"))
        self.image.setText(_translate("view_original_image", "Placeholder for the original image"))

