# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 488)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 190, 47, 13))
        self.label_4.setObjectName("label_4")
        self.cena = QtWidgets.QLabel(parent=Dialog)
        self.cena.setGeometry(QtCore.QRect(160, 230, 361, 171))
        self.cena.setText("")
        self.cena.setObjectName("cena")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 23, 291, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(parent=self.widget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 0, 1, 1, 1)
        self.adress = QtWidgets.QLineEdit(parent=self.widget)
        self.adress.setObjectName("adress")
        self.gridLayout.addWidget(self.adress, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(20, 180, 107, 211))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hawajska = QtWidgets.QRadioButton(parent=self.widget1)
        self.hawajska.setObjectName("hawajska")
        self.verticalLayout.addWidget(self.hawajska)
        self.margarita = QtWidgets.QRadioButton(parent=self.widget1)
        self.margarita.setObjectName("margarita")
        self.verticalLayout.addWidget(self.margarita)
        self.quatrosery = QtWidgets.QRadioButton(parent=self.widget1)
        self.quatrosery.setObjectName("quatrosery")
        self.verticalLayout.addWidget(self.quatrosery)
        self.caprisiosa = QtWidgets.QRadioButton(parent=self.widget1)
        self.caprisiosa.setObjectName("caprisiosa")
        self.verticalLayout.addWidget(self.caprisiosa)
        self.serdod = QtWidgets.QCheckBox(parent=self.widget1)
        self.serdod.setObjectName("serdod")
        self.verticalLayout.addWidget(self.serdod)
        self.button = QtWidgets.QPushButton(parent=self.widget1)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Rodzaj pizzy"))
        self.label_4.setText(_translate("Dialog", "Cena"))
        self.label_2.setText(_translate("Dialog", "adres"))
        self.label.setText(_translate("Dialog", "e-mail"))
        self.hawajska.setText(_translate("Dialog", "hawajska"))
        self.margarita.setText(_translate("Dialog", "margarita"))
        self.quatrosery.setText(_translate("Dialog", "quatro formagi"))
        self.caprisiosa.setText(_translate("Dialog", "caprisiosa"))
        self.serdod.setText(_translate("Dialog", "+ dodatkowy ser"))
        self.button.setText(_translate("Dialog", "zamów"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())