# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SRC_V.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_srcv(object):
    def setupUi(self, srcv):
        srcv.setObjectName("srcv")
        srcv.resize(511, 384)
        self.start = QtWidgets.QPushButton(srcv)
        self.start.setGeometry(QtCore.QRect(60, 240, 400, 23))
        self.start.setObjectName("start")
        self.period = QtWidgets.QLineEdit(srcv)
        self.period.setGeometry(QtCore.QRect(61, 202, 95, 20))
        self.period.setObjectName("period")
        self.layoutWidget = QtWidgets.QWidget(srcv)
        self.layoutWidget.setGeometry(QtCore.QRect(116, 60, 274, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.dir.setObjectName("dir")
        self.gridLayout.addWidget(self.dir, 1, 0, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.layoutWidget)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.stop = QtWidgets.QPushButton(srcv)
        self.stop.setGeometry(QtCore.QRect(60, 273, 401, 23))
        self.stop.setObjectName("stop")
        self.layoutWidget_2 = QtWidgets.QWidget(srcv)
        self.layoutWidget_2.setGeometry(QtCore.QRect(61, 122, 402, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.high = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.high.setObjectName("high")
        self.gridLayout_2.addWidget(self.high, 1, 1, 1, 1)
        self.low = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.low.setObjectName("low")
        self.gridLayout_2.addWidget(self.low, 1, 2, 1, 1)
        self.compliance = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.compliance.setObjectName("compliance")
        self.gridLayout_2.addWidget(self.compliance, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.width = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.width.setObjectName("width")
        self.gridLayout_2.addWidget(self.width, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(srcv)
        self.label_8.setGeometry(QtCore.QRect(61, 182, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(srcv)
        self.label_9.setGeometry(QtCore.QRect(266, 181, 91, 16))
        self.label_9.setObjectName("label_9")
        self.rate = QtWidgets.QLineEdit(srcv)
        self.rate.setGeometry(QtCore.QRect(266, 201, 95, 20))
        self.rate.setObjectName("rate")
        self.tips = QtWidgets.QPushButton(srcv)
        self.tips.setGeometry(QtCore.QRect(14, 13, 31, 31))
        self.tips.setObjectName("tips")
        self.progressBar = QtWidgets.QProgressBar(srcv)
        self.progressBar.setGeometry(QtCore.QRect(60, 340, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.radioButton = QtWidgets.QRadioButton(srcv)
        self.radioButton.setGeometry(QtCore.QRect(120, 20, 271, 16))
        self.radioButton.setObjectName("radioButton")
        self.label_6.setBuddy(self.dir)
        self.label_7.setBuddy(self.filename)
        self.label_4.setBuddy(self.width)
        self.label.setBuddy(self.high)
        self.label_5.setBuddy(self.compliance)
        self.label_2.setBuddy(self.low)
        self.label_8.setBuddy(self.period)
        self.label_9.setBuddy(self.period)

        self.retranslateUi(srcv)
        QtCore.QMetaObject.connectSlotsByName(srcv)
        srcv.setTabOrder(self.radioButton, self.dir)
        srcv.setTabOrder(self.dir, self.filename)
        srcv.setTabOrder(self.filename, self.high)
        srcv.setTabOrder(self.high, self.low)
        srcv.setTabOrder(self.low, self.width)
        srcv.setTabOrder(self.width, self.compliance)
        srcv.setTabOrder(self.compliance, self.period)
        srcv.setTabOrder(self.period, self.rate)
        srcv.setTabOrder(self.rate, self.start)
        srcv.setTabOrder(self.start, self.stop)
        srcv.setTabOrder(self.stop, self.tips)

    def retranslateUi(self, srcv):
        _translate = QtCore.QCoreApplication.translate
        srcv.setWindowTitle(_translate("srcv", "Dialog"))
        self.start.setText(_translate("srcv", "START"))
        self.label_6.setText(_translate("srcv", "FileDir"))
        self.label_7.setText(_translate("srcv", "FileName"))
        self.stop.setText(_translate("srcv", "STOP"))
        self.label_4.setText(_translate("srcv", "Width"))
        self.label.setText(_translate("srcv", "High"))
        self.label_5.setText(_translate("srcv", "Compliance"))
        self.label_2.setText(_translate("srcv", "Low"))
        self.label_8.setText(_translate("srcv", "Period Number"))
        self.label_9.setText(_translate("srcv", "Increasing Rate"))
        self.tips.setText(_translate("srcv", "?"))
        self.radioButton.setText(_translate("srcv", "Mode select(defult->source v mode) "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    srcv = QtWidgets.QDialog()
    ui = Ui_srcv()
    ui.setupUi(srcv)
    srcv.show()
    sys.exit(app.exec_())