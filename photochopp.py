import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QFileDialog, QMessageBox, QRadioButton
from skimage import io

import imglib
from gui.toolbox import Ui_toolbox as Toolbox
from gui.view_original_image import Ui_view_original_image as OriginalImage
from gui.view_working_image import Ui_view_working_image as WorkingImage


class Photochopp:

    def __init__(self):
        self.toolbox_window = QWidget()
        self.toolbox_widgets = Toolbox()

        self.original_image_window = QWidget()
        self.original_image_widgets = OriginalImage()

        self.working_image_window = QWidget()
        self.working_image_widgets = WorkingImage()

        self.__setup_ui()
        self.__setup_events()

        self.original_image = None
        self.original_image_extension = None
        self.working_image = None

        self.toolbox_window.show()

    def __setup_ui(self):
        self.toolbox_widgets.setupUi(self.toolbox_window)

        self.original_image_widgets.setupUi(self.original_image_window)

        self.working_image_widgets.setupUi(self.working_image_window)

        center = QDesktopWidget().availableGeometry().center()

        rect_toolbox = self.toolbox_window.frameGeometry()
        rect_toolbox.moveCenter(center)
        self.toolbox_window.move(rect_toolbox.topLeft())

    def __setup_events(self):
        self.toolbox_window.closeEvent = self.on_window_close
        self.working_image_window.closeEvent = self.on_window_close

        self.toolbox_widgets.io_bt_load.clicked.connect(self.on_io_bt_load_click)
        self.toolbox_widgets.io_bt_save.clicked.connect(self.on_io_bt_save_click)

        self.toolbox_widgets.image_bt_show_original.clicked.connect(self.on_image_bt_show_original_click)
        self.toolbox_widgets.image_bt_reset.clicked.connect(self.on_image_bt_reset_click)

        self.toolbox_widgets.transform_bt_h_flip.clicked.connect(self.on_transform_bt_h_flip_click)
        self.toolbox_widgets.transform_bt_v_flip.clicked.connect(self.on_transform_bt_v_flip_click)

        self.toolbox_widgets.color_bt_luminance.clicked.connect(self.on_color_bt_luminance_click)

        self.toolbox_widgets.quantization_bt_quantize.clicked.connect(self.on_quantization_bt_quantize_click)

    def __reload_working_image(self):
        pixmap = QPixmap(self.__as_qimg(self.working_image))

        self.working_image_widgets.image.setPixmap(pixmap)

    def __as_qimg(self, image: np.ndarray):
        shape = image.shape

        if len(shape) == 3:
            height, width, _ = shape
            bytes_per_line = 3 * width

            return QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        else:
            height, width = shape

            return QImage(image.data, width, height, QImage.Format_Grayscale8)

    def on_io_bt_load_click(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.toolbox_window, "Load an image", "",
                                                   "Image Files (*.jpg *.jpeg *.png)", options=options)
        if file_name:
            self.original_image = io.imread(file_name)
            self.original_image_extension = file_name.split(".")[-1]

            self.working_image = self.original_image.copy()

            pixmap = QPixmap(self.__as_qimg(self.working_image))

            self.original_image_widgets.image.setPixmap(pixmap)
            self.original_image_window.resize(pixmap.width(), pixmap.height())
            self.original_image_window.setFixedSize(pixmap.width(), pixmap.height())

            self.working_image_widgets.image.resize(pixmap.width(), pixmap.height())
            self.working_image_widgets.image.setPixmap(pixmap)
            self.working_image_window.resize(pixmap.width(), pixmap.height())
            self.working_image_window.setFixedSize(pixmap.width(), pixmap.height())

            self.working_image_window.show()

            self.__on_image_loaded()

    def __on_image_loaded(self):
        self.toolbox_widgets.io_bt_save.setEnabled(True)

        self.toolbox_widgets.image_bt_show_original.setEnabled(True)
        self.toolbox_widgets.image_bt_reset.setEnabled(True)

        self.toolbox_widgets.transform_bt_h_flip.setEnabled(True)
        self.toolbox_widgets.transform_bt_v_flip.setEnabled(True)

        self.toolbox_widgets.color_bt_luminance.setEnabled(True)

        self.toolbox_widgets.quantization_bt_quantize.setEnabled(True)

        center = QDesktopWidget().availableGeometry().center()

        rect_original_image = self.original_image_window.frameGeometry()
        rect_original_image.moveCenter(center)
        self.original_image_window.move(rect_original_image.topLeft())

        rect_working_image = self.working_image_window.frameGeometry()
        rect_working_image.moveCenter(center)
        self.working_image_window.move(rect_working_image.topLeft())

    def on_io_bt_save_click(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self.toolbox_window, "Save working image", "",
                                                   "Image Files (*.jpg *.jpeg *.png)", options=options)
        if file_name:
            try:
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    io.imsave(file_name, self.working_image)
                else:
                    io.imsave(file_name + "." + self.original_image_extension, self.working_image)

                QMessageBox.information(self.toolbox_window, "Message", "Image saved", QMessageBox.Ok)
            except IOError:
                QMessageBox.critical(self.toolbox_window, "Message", "Image could not be saved", QMessageBox.Ok)

    def on_image_bt_show_original_click(self):
        if self.original_image_window.isVisible():
            self.original_image_window.close()
        else:
            self.original_image_window.show()

    def on_image_bt_reset_click(self):
        self.working_image = self.original_image.copy()

        self.__reload_working_image()

    def on_transform_bt_h_flip_click(self):
        self.working_image = imglib.transform_h_flip(self.working_image)

        self.__reload_working_image()

    def on_transform_bt_v_flip_click(self):
        self.working_image = imglib.transform_v_flip(self.working_image)

        self.__reload_working_image()

    def on_color_bt_luminance_click(self):
        self.working_image = imglib.color_as_gray_scale(self.working_image)

        self.__reload_working_image()

    def on_quantization_bt_quantize_click(self):
        n_colors = self.toolbox_widgets.quantization_spin_tones.value()

        button_text = self.toolbox_widgets.quantization_bt_quantize.text()
        self.toolbox_widgets.quantization_bt_quantize.setText("Processing...")
        self.toolbox_widgets.quantization_bt_quantize.setEnabled(False)
        self.toolbox_widgets.quantization_bt_quantize.repaint()

        if self.toolbox_widgets.quantization_radio_random.isChecked():
            self.working_image = imglib.quantization_random(self.working_image, n_colors)

        elif self.toolbox_widgets.quantization_radio_kmeans.isChecked():
            self.working_image = imglib.quantization_kmeans(self.working_image, n_colors)

        self.toolbox_widgets.quantization_bt_quantize.setText(button_text)
        self.toolbox_widgets.quantization_bt_quantize.setEnabled(True)

        self.__reload_working_image()

    def on_window_close(self, event):
        reply = QMessageBox.question(self.toolbox_window, "Message",
                                     "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Photochopp()
    sys.exit(app.exec_())
