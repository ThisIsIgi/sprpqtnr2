import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.zamow)
        self.show()


    def zamow(self):
        cenap = 1
        los = random.randint(10,100)
        email = self.ui.email.text()
        adres = self.ui.adress.text()


        if self.ui.hawajska.isChecked():
            cenap = 30
            cenap = str(cenap)
            los = str(los)
            self.ui.cena.setText("Użytkownik "+email+ "zamówił w pizzę hawajska. Cena: "+cenap+". Przewidywany czas dostawy: " + los + "min. Dostawa pod adres " + adres)
        elif self.ui.caprisiosa.isChecked():
            cenap = 32
            cenap = str(cenap)
            los = str(los)
            self.ui.cena.setText("Użytkownik "+email+ "zamówił w pizzę hawajska. Cena:"+cenap+".\n Przewidywany czas dostawy: " + los + "\nmin. Dostawa pod adres  " + adres)
        elif self.ui.margarita.isChecked():
            cenap = 28
            cenap = str(cenap)
            los = str(los)
            self.ui.cena.setText("Użytkownik "+email+ "zamówił w pizzę hawajska. Cena: "+cenap+"\n. Przewidywany czas dostawy: " + los + "\nmin. Dostawa pod adres  " + adres)
        elif self.ui.quatrosery.isChecked():
            cenap = 34
            cenap = str(cenap)
            los = str(los)
            self.ui.cena.setText("Użytkownik "+email+ "zamówił w pizzę hawajska. Cena:"+cenap+"\n. Przewidywany czas dostawy: " + los + "\nmin. Dostawa pod adres " + adres)
        cenap = str(cenap)
        los = str(los)
        self.ui.cena.setText("Użytkownik "+email+ "zamówił w pizzę hawajska. Cena:"+cenap+". \nPrzewidywany czas dostawy: " + los + "\nmin. Dostawa pod adres " + adres)

        if '@' in email:
            a = 0
        else:
            self.ui.cena.setText('zly mail')






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())