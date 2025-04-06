# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slm_controller_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(33, 43, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 50, 480, 288))
        # remove scrollBar
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(570, 50, 480, 288))
        self.graphicsView_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView_2.setObjectName("graphicsView_2")
        # add graphicsScene
        self.scene1 = QtWidgets.QGraphicsScene(0, 0, 480, 288)
        self.graphicsView.setScene(self.scene1)
        self.scene2 = QtWidgets.QGraphicsScene(0, 0, 480, 288)
        self.graphicsView_2.setScene(self.scene2)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 350, 190, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 350, 190, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.btn_browse_slm1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse_slm1.setGeometry(QtCore.QRect(430, 350, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_browse_slm1.setFont(font)
        self.btn_browse_slm1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(61, 80, 95);\n"
                                           "border-radius: 5px;\n"
                                           "pressed: {background-color: rgb(180, 120, 90)};")
        self.btn_browse_slm1.setObjectName("btn_browse_slm1")
        self.btn_browse_slm2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse_slm2.setGeometry(QtCore.QRect(950, 350, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_browse_slm2.setFont(font)
        self.btn_browse_slm2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(61, 80, 95);\n"
                                           "border-radius: 5px;\n"
                                           "pressed: {background-color: rgb(180, 120, 90)};")
        self.btn_browse_slm2.setObjectName("btn_browse_slm2")
        self.line_edit_path1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_path1.setGeometry(QtCore.QRect(50, 390, 481, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.line_edit_path1.setFont(font)
        self.line_edit_path1.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_edit_path1.setText("")
        self.line_edit_path1.setObjectName("line_edit_path1")
        self.line_edit_path2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_path2.setGeometry(QtCore.QRect(570, 390, 481, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.line_edit_path2.setFont(font)
        self.line_edit_path2.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_edit_path2.setText("")
        self.line_edit_path2.setObjectName("line_edit_path2")
        self.btn_update_slm1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update_slm1.setGeometry(QtCore.QRect(380, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_update_slm1.setFont(font)
        self.btn_update_slm1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(61, 80, 95);\n"
                                           "border-radius: 5px;\n"
                                           "pressed: {background-color: rgb(180, 120, 90)};")
        self.btn_update_slm1.setObjectName("btn_update_slm1")
        self.btn_update_slm2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update_slm2.setGeometry(QtCore.QRect(900, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_update_slm2.setFont(font)
        self.btn_update_slm2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(61, 80, 95);\n"
                                           "border-radius: 5px;\n"
                                           "pressed: {background-color: rgb(180, 120, 90)};")
        self.btn_update_slm2.setObjectName("btn_update_slm2")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_browse_slm1.clicked.connect(MainWindow.browse_slm1)
        self.btn_browse_slm2.clicked.connect(MainWindow.browse_slm2)
        self.btn_update_slm1.clicked.connect(MainWindow.update_slm1)
        self.btn_update_slm2.clicked.connect(MainWindow.update_slm2)
        self.line_edit_path1.returnPressed.connect(MainWindow.line1_input)
        self.line_edit_path2.returnPressed.connect(MainWindow.line2_input)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hologram File"))
        self.label_2.setText(_translate("MainWindow", "Hologram File"))
        self.label_3.setText(_translate("MainWindow", "SLM1"))
        self.label_4.setText(_translate("MainWindow", "SLM2"))
        self.btn_browse_slm1.setText(_translate("MainWindow", "Browse"))
        self.btn_browse_slm2.setText(_translate("MainWindow", "Browse"))
        self.btn_update_slm1.setText(_translate("MainWindow", "Update_SLM1"))
        self.btn_update_slm2.setText(_translate("MainWindow", "Update_SLM2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
