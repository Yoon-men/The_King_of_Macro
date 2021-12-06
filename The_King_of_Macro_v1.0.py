# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KOMmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# ====================================================================================================
"""
<The_King_of_Macro_v1.0> - 21.12.6.월 11:46
* Made by Yoonmen *
"""

from urllib.request import DataHandler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import csv
import keyboard
import mouse
import pyautogui
import time


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 565)
        self.Add_Button = QtWidgets.QPushButton(Form)
        self.Add_Button.setGeometry(QtCore.QRect(280, 100, 51, 21))
        self.Add_Button.setObjectName("Add_Button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 241, 71))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 64, 15))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_Name = QtWidgets.QLineEdit(Form)
        self.lineEdit_Name.setGeometry(QtCore.QRect(20, 100, 251, 20))
        self.lineEdit_Name.setClearButtonEnabled(True)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(130, 540, 101, 16))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 131, 20))
        self.label_9.setObjectName("label_9")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 450, 311, 81))
        self.listWidget.setDragEnabled(False)
        self.listWidget.setObjectName("listWidget")
        self.Start_spinBox = QtWidgets.QSpinBox(Form)
        self.Start_spinBox.setGeometry(QtCore.QRect(210, 410, 42, 22))
        self.Start_spinBox.setObjectName("Start_spinBox")
        self.Start_comboBox = QtWidgets.QComboBox(Form)
        self.Start_comboBox.setGeometry(QtCore.QRect(20, 410, 141, 22))
        self.Start_comboBox.setObjectName("Start_comboBox")
        self.Start_Button = QtWidgets.QPushButton(Form)
        self.Start_Button.setGeometry(QtCore.QRect(280, 410, 51, 21))
        self.Start_Button.setObjectName("Start_Button")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 380, 101, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(170, 410, 41, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(260, 410, 16, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(20, 140, 101, 20))
        self.label_13.setObjectName("label_13")
        self.Click_Button = QtWidgets.QPushButton(Form)
        self.Click_Button.setGeometry(QtCore.QRect(280, 170, 51, 21))
        self.Click_Button.setObjectName("Click_Button")
        self.Add_comboBox = QtWidgets.QComboBox(Form)
        self.Add_comboBox.setGeometry(QtCore.QRect(20, 170, 101, 22))
        self.Add_comboBox.setObjectName("Add_comboBox")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(130, 170, 16, 20))
        self.label_16.setObjectName("label_16")
        self.Delete_comboBox = QtWidgets.QComboBox(Form)
        self.Delete_comboBox.setGeometry(QtCore.QRect(20, 300, 211, 22))
        self.Delete_comboBox.setObjectName("Delete_comboBox")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(20, 270, 101, 20))
        self.label_14.setObjectName("label_14")
        self.Delete_Button = QtWidgets.QPushButton(Form)
        self.Delete_Button.setGeometry(QtCore.QRect(280, 300, 51, 21))
        self.Delete_Button.setObjectName("Delete_Button")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(80, 200, 191, 20))
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(110, 250, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(110, 360, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(240, 300, 41, 20))
        self.label_19.setObjectName("label_19")
        self.Load_Button = QtWidgets.QToolButton(Form)
        self.Load_Button.setGeometry(QtCore.QRect(280, 10, 61, 20))
        self.Load_Button.setObjectName("Load_Button")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(210, 170, 71, 20))
        self.label_17.setObjectName("label_17")
        self.Delay_doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.Delay_doubleSpinBox.setGeometry(QtCore.QRect(150, 170, 51, 22))
        self.Delay_doubleSpinBox.setObjectName("Delay_doubleSpinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # ====================================================================================================
        """Button 클릭 시 발동"""
        self.Load_Button.clicked.connect(self.Load_CSV)
        self.Add_Button.clicked.connect(self.Add_MACRO)
        self.Click_Button.clicked.connect(self.Add_CLICK)
        self.Delete_Button.clicked.connect(self.Delete_MACRO)
        self.Start_Button.clicked.connect(self.Start_MACRO)
        # ----------------------------------------------------------------------------------------------------
        """실행되자마자"""
        global Load_status
        Load_status = 0         # 아직 CSV 파일을 불러오지 않은 상태
        self.listWidget.addItem('[system] 환영합니다.')
        # ====================================================================================================



    # ====================================================================================================
    # <<<매크로 프로그램 화면>>>
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "The_King_of_Macro_v1.0"))
        self.Add_Button.setText(_translate("Form", "추가"))
        self.label.setText(_translate("Form", "The King of Macro"))
        self.label_4.setText(_translate("Form", "v1.0"))
        self.label_8.setText(_translate("Form", "by. Yoonmen"))
        self.label_9.setText(_translate("Form", "<Add Macro\'s Name>"))
        self.Start_Button.setText(_translate("Form", "실행"))
        self.label_10.setText(_translate("Form", "<Start Macro>"))
        self.label_11.setText(_translate("Form", "을(를)"))
        self.label_12.setText(_translate("Form", "번"))
        self.label_13.setText(_translate("Form", "<Add Click>"))
        self.Click_Button.setText(_translate("Form", "클릭"))
        self.label_16.setText(_translate("Form", "에"))
        self.label_14.setText(_translate("Form", "<Delete Macro>"))
        self.Delete_Button.setText(_translate("Form", "삭제"))
        self.label_18.setText(_translate("Form", "(순서에 맞게 클릭을 진행하세요.)"))
        self.label_19.setText(_translate("Form", "을(를)"))
        self.Load_Button.setText(_translate("Form", "불러오기"))
        self.label_17.setText(_translate("Form", "초 간격으로"))
    # ====================================================================================================



    # ====================================================================================================
    # <<<불러오기>>>
    """클릭 → CSV 파일 - 불러오기 & 경로 저장"""
    def Load_CSV(self) : 
        global Load_status
        global CSV_road
        CSV_road = str(QFileDialog.getOpenFileName()[0])
        CSV_name = os.path.basename(CSV_road)
        
        if CSV_name == 'DATA.csv' : 
            self.listWidget.addItem('[system] DATA.csv를 불러오는데 성공했습니다.')
            # ----------------------------------------------------------------------------------------------------
            """불러온 CSV 읽기"""
            global CSV_data
            CSV_file = open(CSV_road, 'r', encoding = 'utf-8', newline='')
            # CSV_read = csv.reader(CSV_file)
            CSV_read = csv.reader(CSV_file)
            CSV_data = []

            for row in CSV_read : 
                CSV_data.append(row)

            for i in range(1, len(CSV_data)) : 
                self.Add_comboBox.addItem(CSV_data[i][0])
                self.Delete_comboBox.addItem(CSV_data[i][0])
                self.Start_comboBox.addItem(CSV_data[i][0])
            
            Load_status = 1         # CSV 파일을 불러온 상태
            # ----------------------------------------------------------------------------------------------------

        elif CSV_name != 'DATA.csv' : 
            self.listWidget.addItem('[system] DATA.csv를 불러오는데 실패했습니다.')
    # ====================================================================================================



    # ====================================================================================================
    # <<<Add Macro's Name>>>
    """클릭 → CSV에 매크로 리스트 추가"""
    def Add_MACRO(self) : 
        if Load_status == 1 : 
            MACRO_name = [self.lineEdit_Name.text()]
            
            if MACRO_name[0] == '' : 
                self.listWidget.addItem('[system] 공백을 이름으로 사용할 수 없습니다.')
            else : 
                self.Add_comboBox.addItem(MACRO_name[0])
                self.Delete_comboBox.addItem(MACRO_name[0])
                self.Start_comboBox.addItem(MACRO_name[0])

                CSV_data.append(MACRO_name)

                CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                writer = csv.writer(CSV_file)
                writer.writerows(CSV_data)

                self.listWidget.addItem('[system] 매크로를 추가했습니다.')
        else : 
            self.listWidget.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')
    # ====================================================================================================



    # ====================================================================================================
    # <<<Add Click>>>
    def Add_CLICK(self) : 
        if Load_status == 1 : 
            object = self.Add_comboBox.currentIndex()

            if len(CSV_data[object + 1]) == 1 : 
                CSV_data[object + 1].append(self.Delay_doubleSpinBox.value())

            while True : 
                if mouse.is_pressed('left') : 
                    x, y = pyautogui.position()
                    CSV_data[object + 1].append(x)
                    CSV_data[object + 1].append(y)

                    CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
                    writer = csv.writer(CSV_file)
                    writer.writerows(CSV_data)

                    self.listWidget.addItem('[system] 클릭 좌표가 설정되었습니다.')
                    break

                elif keyboard.is_pressed('ESC') : 
                    self.listWidget.addItem('[system] 클릭 추가가 중지되었습니다.')
                    break
        else : 
            self.listWidget.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')
    # ====================================================================================================



    # ====================================================================================================
    # <<<Delete Macro>>>
    def Delete_MACRO(self) : 
        if Load_status == 1 : 
            object = self.Delete_comboBox.currentIndex()

            self.Add_comboBox.removeItem(object)
            self.Start_comboBox.removeItem(object)
            self.Delete_comboBox.removeItem(object)
            del CSV_data[object + 1]

            CSV_file = open(CSV_road, 'w', encoding = 'utf-8', newline='')
            writer = csv.writer(CSV_file)
            writer.writerows(CSV_data)

            self.listWidget.addItem('[system] 매크로를 삭제했습니다.')
        else : 
            self.listWidget.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')
    # ====================================================================================================



    # ====================================================================================================
    # <<<Start Macro>>>
    def Start_MACRO(self) : 
        if Load_status == 1 :
            object = self.Start_comboBox.currentIndex()
            position_num = int((len(CSV_data[object + 1])-2)/2)
            delay = float(CSV_data[object + 1][1])
            for i in range(self.Start_spinBox.value()) : 
                for j in range(position_num) : 
                    position = int(CSV_data[object + 1][(j+1)*2]), int(CSV_data[object + 1][(j+1)*2 + 1])
                    pyautogui.moveTo(position)      # 바로 클릭하지 못하는 상황 고려해서 클릭 전에 미리 올려놓기
                    time.sleep(0.05)
                    pyautogui.click(position)
                    time.sleep(delay)
        else : 
            self.listWidget.addItem('[system] 아직 DATA.csv를 불러오지 않았습니다.')
    # ====================================================================================================



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())