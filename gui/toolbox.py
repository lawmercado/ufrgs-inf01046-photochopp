# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc/toolbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_toolbox(object):
    def setupUi(self, toolbox):
        toolbox.setObjectName("toolbox")
        toolbox.resize(300, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toolbox.sizePolicy().hasHeightForWidth())
        toolbox.setSizePolicy(sizePolicy)
        toolbox.setMinimumSize(QtCore.QSize(300, 500))
        toolbox.setMaximumSize(QtCore.QSize(300, 500))
        icon = QtGui.QIcon.fromTheme("insert-image")
        toolbox.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(toolbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(toolbox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -334, 266, 1198))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.io_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.io_group.sizePolicy().hasHeightForWidth())
        self.io_group.setSizePolicy(sizePolicy)
        self.io_group.setMinimumSize(QtCore.QSize(0, 100))
        self.io_group.setObjectName("io_group")
        self.gridLayout = QtWidgets.QGridLayout(self.io_group)
        self.gridLayout.setObjectName("gridLayout")
        self.io_bt_load = QtWidgets.QPushButton(self.io_group)
        self.io_bt_load.setObjectName("io_bt_load")
        self.gridLayout.addWidget(self.io_bt_load, 0, 0, 1, 1)
        self.io_bt_save = QtWidgets.QPushButton(self.io_group)
        self.io_bt_save.setEnabled(False)
        self.io_bt_save.setObjectName("io_bt_save")
        self.gridLayout.addWidget(self.io_bt_save, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.io_group)
        self.image_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_group.sizePolicy().hasHeightForWidth())
        self.image_group.setSizePolicy(sizePolicy)
        self.image_group.setMinimumSize(QtCore.QSize(0, 100))
        self.image_group.setObjectName("image_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.image_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image_bt_show_original = QtWidgets.QPushButton(self.image_group)
        self.image_bt_show_original.setEnabled(False)
        self.image_bt_show_original.setObjectName("image_bt_show_original")
        self.gridLayout_2.addWidget(self.image_bt_show_original, 0, 0, 1, 1)
        self.image_bt_reset = QtWidgets.QPushButton(self.image_group)
        self.image_bt_reset.setEnabled(False)
        self.image_bt_reset.setObjectName("image_bt_reset")
        self.gridLayout_2.addWidget(self.image_bt_reset, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.image_group)
        self.transform_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transform_group.sizePolicy().hasHeightForWidth())
        self.transform_group.setSizePolicy(sizePolicy)
        self.transform_group.setMinimumSize(QtCore.QSize(0, 350))
        self.transform_group.setObjectName("transform_group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.transform_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.transform_bt_h_flip = QtWidgets.QPushButton(self.transform_group)
        self.transform_bt_h_flip.setEnabled(False)
        self.transform_bt_h_flip.setObjectName("transform_bt_h_flip")
        self.verticalLayout_4.addWidget(self.transform_bt_h_flip)
        self.transform_bt_v_flip = QtWidgets.QPushButton(self.transform_group)
        self.transform_bt_v_flip.setEnabled(False)
        self.transform_bt_v_flip.setObjectName("transform_bt_v_flip")
        self.verticalLayout_4.addWidget(self.transform_bt_v_flip)
        self.transform_line_1 = QtWidgets.QFrame(self.transform_group)
        self.transform_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.transform_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.transform_line_1.setObjectName("transform_line_1")
        self.verticalLayout_4.addWidget(self.transform_line_1)
        self.transform_bt_rotate_cw = QtWidgets.QPushButton(self.transform_group)
        self.transform_bt_rotate_cw.setEnabled(False)
        self.transform_bt_rotate_cw.setObjectName("transform_bt_rotate_cw")
        self.verticalLayout_4.addWidget(self.transform_bt_rotate_cw)
        self.transform_bt_rotate_ccw = QtWidgets.QPushButton(self.transform_group)
        self.transform_bt_rotate_ccw.setEnabled(False)
        self.transform_bt_rotate_ccw.setObjectName("transform_bt_rotate_ccw")
        self.verticalLayout_4.addWidget(self.transform_bt_rotate_ccw)
        self.transform_line_2 = QtWidgets.QFrame(self.transform_group)
        self.transform_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.transform_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.transform_line_2.setObjectName("transform_line_2")
        self.verticalLayout_4.addWidget(self.transform_line_2)
        self.zoom_group = QtWidgets.QGroupBox(self.transform_group)
        self.zoom_group.setMinimumSize(QtCore.QSize(0, 150))
        self.zoom_group.setObjectName("zoom_group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.zoom_group)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.zoom_spin_vf = QtWidgets.QSpinBox(self.zoom_group)
        self.zoom_spin_vf.setMinimum(1)
        self.zoom_spin_vf.setObjectName("zoom_spin_vf")
        self.gridLayout_3.addWidget(self.zoom_spin_vf, 3, 1, 1, 1)
        self.zoom_bt_zo = QtWidgets.QPushButton(self.zoom_group)
        self.zoom_bt_zo.setEnabled(False)
        self.zoom_bt_zo.setObjectName("zoom_bt_zo")
        self.gridLayout_3.addWidget(self.zoom_bt_zo, 4, 0, 1, 2)
        self.zoom_line_1 = QtWidgets.QFrame(self.zoom_group)
        self.zoom_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.zoom_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zoom_line_1.setObjectName("zoom_line_1")
        self.gridLayout_3.addWidget(self.zoom_line_1, 1, 0, 1, 2)
        self.zoom_label_vf = QtWidgets.QLabel(self.zoom_group)
        self.zoom_label_vf.setObjectName("zoom_label_vf")
        self.gridLayout_3.addWidget(self.zoom_label_vf, 3, 0, 1, 1)
        self.zoom_spin_hf = QtWidgets.QSpinBox(self.zoom_group)
        self.zoom_spin_hf.setMinimum(1)
        self.zoom_spin_hf.setObjectName("zoom_spin_hf")
        self.gridLayout_3.addWidget(self.zoom_spin_hf, 2, 1, 1, 1)
        self.zoom_label_hf = QtWidgets.QLabel(self.zoom_group)
        self.zoom_label_hf.setObjectName("zoom_label_hf")
        self.gridLayout_3.addWidget(self.zoom_label_hf, 2, 0, 1, 1)
        self.zoom_bt_zi = QtWidgets.QPushButton(self.zoom_group)
        self.zoom_bt_zi.setEnabled(False)
        self.zoom_bt_zi.setObjectName("zoom_bt_zi")
        self.gridLayout_3.addWidget(self.zoom_bt_zi, 0, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.zoom_group)
        self.verticalLayout_2.addWidget(self.transform_group)
        self.color_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_group.sizePolicy().hasHeightForWidth())
        self.color_group.setSizePolicy(sizePolicy)
        self.color_group.setMinimumSize(QtCore.QSize(0, 200))
        self.color_group.setObjectName("color_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.color_group)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.color_bt_neg = QtWidgets.QPushButton(self.color_group)
        self.color_bt_neg.setEnabled(False)
        self.color_bt_neg.setObjectName("color_bt_neg")
        self.gridLayout_4.addWidget(self.color_bt_neg, 1, 0, 1, 2)
        self.color_bt_bright = QtWidgets.QPushButton(self.color_group)
        self.color_bt_bright.setEnabled(False)
        self.color_bt_bright.setObjectName("color_bt_bright")
        self.gridLayout_4.addWidget(self.color_bt_bright, 3, 1, 1, 1)
        self.color_spin_bright = QtWidgets.QSpinBox(self.color_group)
        self.color_spin_bright.setMinimum(-255)
        self.color_spin_bright.setMaximum(255)
        self.color_spin_bright.setObjectName("color_spin_bright")
        self.gridLayout_4.addWidget(self.color_spin_bright, 3, 0, 1, 1)
        self.color_bt_cont = QtWidgets.QPushButton(self.color_group)
        self.color_bt_cont.setEnabled(False)
        self.color_bt_cont.setObjectName("color_bt_cont")
        self.gridLayout_4.addWidget(self.color_bt_cont, 4, 1, 1, 1)
        self.color_bt_luminance = QtWidgets.QPushButton(self.color_group)
        self.color_bt_luminance.setEnabled(False)
        self.color_bt_luminance.setObjectName("color_bt_luminance")
        self.gridLayout_4.addWidget(self.color_bt_luminance, 0, 0, 1, 2)
        self.color_line_1 = QtWidgets.QFrame(self.color_group)
        self.color_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.color_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.color_line_1.setObjectName("color_line_1")
        self.gridLayout_4.addWidget(self.color_line_1, 2, 0, 1, 2)
        self.color_spin_cont = QtWidgets.QDoubleSpinBox(self.color_group)
        self.color_spin_cont.setMinimum(0.01)
        self.color_spin_cont.setMaximum(255.0)
        self.color_spin_cont.setSingleStep(0.01)
        self.color_spin_cont.setObjectName("color_spin_cont")
        self.gridLayout_4.addWidget(self.color_spin_cont, 4, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.color_group)
        self.conv_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.conv_group.setObjectName("conv_group")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.conv_group)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.conv_bt_show = QtWidgets.QPushButton(self.conv_group)
        self.conv_bt_show.setEnabled(False)
        self.conv_bt_show.setObjectName("conv_bt_show")
        self.verticalLayout_5.addWidget(self.conv_bt_show)
        self.verticalLayout_2.addWidget(self.conv_group)
        self.hist_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.hist_group.setMinimumSize(QtCore.QSize(0, 200))
        self.hist_group.setObjectName("hist_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.hist_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hist_bt_show = QtWidgets.QPushButton(self.hist_group)
        self.hist_bt_show.setEnabled(False)
        self.hist_bt_show.setObjectName("hist_bt_show")
        self.verticalLayout_3.addWidget(self.hist_bt_show)
        self.hist_bt_show_original = QtWidgets.QPushButton(self.hist_group)
        self.hist_bt_show_original.setEnabled(False)
        self.hist_bt_show_original.setObjectName("hist_bt_show_original")
        self.verticalLayout_3.addWidget(self.hist_bt_show_original)
        self.hist_line_1 = QtWidgets.QFrame(self.hist_group)
        self.hist_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hist_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hist_line_1.setObjectName("hist_line_1")
        self.verticalLayout_3.addWidget(self.hist_line_1)
        self.hist_bt_eq = QtWidgets.QPushButton(self.hist_group)
        self.hist_bt_eq.setEnabled(False)
        self.hist_bt_eq.setObjectName("hist_bt_eq")
        self.verticalLayout_3.addWidget(self.hist_bt_eq)
        self.hist_bt_lab_eq = QtWidgets.QPushButton(self.hist_group)
        self.hist_bt_lab_eq.setEnabled(False)
        self.hist_bt_lab_eq.setObjectName("hist_bt_lab_eq")
        self.verticalLayout_3.addWidget(self.hist_bt_lab_eq)
        self.hist_line_2 = QtWidgets.QFrame(self.hist_group)
        self.hist_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hist_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hist_line_2.setObjectName("hist_line_2")
        self.verticalLayout_3.addWidget(self.hist_line_2)
        self.hist_bt_show_match = QtWidgets.QPushButton(self.hist_group)
        self.hist_bt_show_match.setEnabled(False)
        self.hist_bt_show_match.setObjectName("hist_bt_show_match")
        self.verticalLayout_3.addWidget(self.hist_bt_show_match)
        self.verticalLayout_2.addWidget(self.hist_group)
        self.quantization_group = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.quantization_group.setMinimumSize(QtCore.QSize(0, 125))
        self.quantization_group.setObjectName("quantization_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.quantization_group)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.quantization_spin_tones = QtWidgets.QSpinBox(self.quantization_group)
        self.quantization_spin_tones.setMinimum(1)
        self.quantization_spin_tones.setMaximum(256)
        self.quantization_spin_tones.setProperty("value", 256)
        self.quantization_spin_tones.setObjectName("quantization_spin_tones")
        self.gridLayout_5.addWidget(self.quantization_spin_tones, 0, 1, 1, 1)
        self.quantization_spin_label_tones = QtWidgets.QLabel(self.quantization_group)
        self.quantization_spin_label_tones.setObjectName("quantization_spin_label_tones")
        self.gridLayout_5.addWidget(self.quantization_spin_label_tones, 0, 0, 1, 1)
        self.quantization_bt_quantize = QtWidgets.QPushButton(self.quantization_group)
        self.quantization_bt_quantize.setEnabled(False)
        self.quantization_bt_quantize.setObjectName("quantization_bt_quantize")
        self.gridLayout_5.addWidget(self.quantization_bt_quantize, 2, 0, 1, 2)
        self.quantization_radio_random = QtWidgets.QRadioButton(self.quantization_group)
        self.quantization_radio_random.setChecked(True)
        self.quantization_radio_random.setObjectName("quantization_radio_random")
        self.gridLayout_5.addWidget(self.quantization_radio_random, 1, 0, 1, 1)
        self.quantization_radio_kmeans = QtWidgets.QRadioButton(self.quantization_group)
        self.quantization_radio_kmeans.setObjectName("quantization_radio_kmeans")
        self.gridLayout_5.addWidget(self.quantization_radio_kmeans, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.quantization_group)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(toolbox)
        QtCore.QMetaObject.connectSlotsByName(toolbox)

    def retranslateUi(self, toolbox):
        _translate = QtCore.QCoreApplication.translate
        toolbox.setWindowTitle(_translate("toolbox", "Photochopp - Toolbox"))
        self.io_group.setTitle(_translate("toolbox", "IO"))
        self.io_bt_load.setText(_translate("toolbox", "Load image"))
        self.io_bt_save.setText(_translate("toolbox", "Save working image"))
        self.image_group.setTitle(_translate("toolbox", "Image"))
        self.image_bt_show_original.setText(_translate("toolbox", "Show/hide original image"))
        self.image_bt_reset.setText(_translate("toolbox", "Reset working image"))
        self.transform_group.setTitle(_translate("toolbox", "Transform"))
        self.transform_bt_h_flip.setText(_translate("toolbox", "Flip Horizontally"))
        self.transform_bt_v_flip.setText(_translate("toolbox", "Flip Vertically"))
        self.transform_bt_rotate_cw.setText(_translate("toolbox", "Rotate clockwise"))
        self.transform_bt_rotate_ccw.setText(_translate("toolbox", "Rotate counterclockwise"))
        self.zoom_group.setTitle(_translate("toolbox", "Zoom"))
        self.zoom_bt_zo.setText(_translate("toolbox", "Zoom out"))
        self.zoom_label_vf.setText(_translate("toolbox", "Ver. factor"))
        self.zoom_label_hf.setText(_translate("toolbox", "Hor. factor"))
        self.zoom_bt_zi.setText(_translate("toolbox", "Zoom in (2x2)"))
        self.color_group.setTitle(_translate("toolbox", "Color"))
        self.color_bt_neg.setText(_translate("toolbox", "Negative"))
        self.color_bt_bright.setText(_translate("toolbox", "Set brightness"))
        self.color_bt_cont.setText(_translate("toolbox", "Set contrast"))
        self.color_bt_luminance.setText(_translate("toolbox", "Luminance"))
        self.conv_group.setTitle(_translate("toolbox", "Filters"))
        self.conv_bt_show.setText(_translate("toolbox", "Convolute..."))
        self.hist_group.setTitle(_translate("toolbox", "Histogram"))
        self.hist_bt_show.setText(_translate("toolbox", "Show/hide histogram"))
        self.hist_bt_show_original.setText(_translate("toolbox", "Show/hide original histogram"))
        self.hist_bt_eq.setText(_translate("toolbox", "Equalize histogram"))
        self.hist_bt_lab_eq.setText(_translate("toolbox", "Equalize histogram (L*a*b)"))
        self.hist_bt_show_match.setText(_translate("toolbox", "Histogram matching..."))
        self.quantization_group.setTitle(_translate("toolbox", "Quantization"))
        self.quantization_spin_label_tones.setText(_translate("toolbox", "# of tones"))
        self.quantization_bt_quantize.setText(_translate("toolbox", "Quantize"))
        self.quantization_radio_random.setText(_translate("toolbox", "Random"))
        self.quantization_radio_kmeans.setText(_translate("toolbox", "KMeans"))

