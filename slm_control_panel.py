from PyQt5.Qt import QWidget, QApplication, pyqtSignal, QFileDialog, QMainWindow
from ui_slm_controller_v1 import Ui_MainWindow
import numpy as np


class Window(QWidget, Ui_MainWindow):
    '''define signal'''
    browse1_signal = pyqtSignal(str)
    browse2_signal = pyqtSignal(str)
    update1_signal = pyqtSignal(str)
    update2_signal = pyqtSignal(str)
    line1_input_signal = pyqtSignal(str)
    line2_input_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def browse_slm1(self):
        options = QFileDialog.Options()
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.*);;Text Files (*.txt)",
                                                options=options)
        print(file_path[0])
        self.line_edit_path1.setText(file_path[0])
        self.browse1_signal.emit(file_path[0])

    def browse_slm2(self):
        options = QFileDialog.Options()
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
                                                options=options)
        print(file_path)
        self.line_edit_path2.setText(file_path[0])
        self.browse2_signal.emit(file_path[0])

    def line1_input(self):
        path = str(self.line_edit_path1.text())
        self.line1_input_signal.emit(path)

    def line2_input(self):
        path = str(self.line_edit_path2.text())
        self.line2_input_signal.emit(path)

    def update_slm1(self):
        ''''''
        path = str(self.line_edit_path1.text())
        self.update1_signal.emit(path)
        pass

    def update_slm2(self):
        path = str(self.line_edit_path2.text())
        self.update2_signal.emit(path)
        ''''''
        pass


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    my_window = Window()
    my_window.show()
    sys.exit(app.exec_())
