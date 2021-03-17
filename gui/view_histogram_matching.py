# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/histogram_matching_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_histogram_matching(object):
    def setupUi(self, view_histogram_matching):
        view_histogram_matching.setObjectName("view_histogram_matching")
        view_histogram_matching.resize(400, 300)
        icon = QtGui.QIcon.fromTheme("insert-image")
        view_histogram_matching.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(view_histogram_matching)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QLabel(view_histogram_matching)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        self.match_bt_io_load = QtWidgets.QPushButton(view_histogram_matching)
        self.match_bt_io_load.setObjectName("match_bt_io_load")
        self.gridLayout.addWidget(self.match_bt_io_load, 1, 0, 1, 1)
        self.match_bt_match = QtWidgets.QPushButton(view_histogram_matching)
        self.match_bt_match.setEnabled(False)
        self.match_bt_match.setObjectName("match_bt_match")
        self.gridLayout.addWidget(self.match_bt_match, 1, 1, 1, 1)
        self.hist = QtWidgets.QLabel(view_histogram_matching)
        self.hist.setAlignment(QtCore.Qt.AlignCenter)
        self.hist.setObjectName("hist")
        self.gridLayout.addWidget(self.hist, 0, 1, 1, 1)

        self.retranslateUi(view_histogram_matching)
        QtCore.QMetaObject.connectSlotsByName(view_histogram_matching)

    def retranslateUi(self, view_histogram_matching):
        _translate = QtCore.QCoreApplication.translate
        view_histogram_matching.setWindowTitle(_translate("view_histogram_matching", "Photochopp - Histogram Matching"))
        self.image.setText(_translate("view_histogram_matching", "Placeholder for image"))
        self.match_bt_io_load.setText(_translate("view_histogram_matching", "Load image"))
        self.match_bt_match.setText(_translate("view_histogram_matching", "Match"))
        self.hist.setText(_translate("view_histogram_matching", "Placeholder for histogram"))

