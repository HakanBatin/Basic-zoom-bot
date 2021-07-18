from datetime import datetime
import webbrowser
import time
import tkinter as tk
from PyQt5 import QtCore, QtGui, QtWidgets


pencere = tk.Tk()
pencere.title("Ders Bot")
pencere.geometry("250x80+600+300")
etiket = tk.Label(text="Ders saatleri dışındasın!", font="Verdana 12")
etiket.pack()

zaman = time.localtime()
zmn = datetime.now()
saat = zmn.hour
dakika = zmn.minute
link = "https://us04web.zoom.us/j/4842079044?pwd=ODNMOFZ1MjFaSHRoREt0UXVzMjJTUT09"
#print(zaman)
matematik = "zoom_link"     #define zoom links
fizik = "zoom_link"
kimya = "zoom_link"
biyoloji = "zoom_link"
ingilizce = "zoom_link"
almanca = "zoom_link"
din = "zoom_link"
tarih = "zoom_link"
edebiyat = "zoom_link"
beden = "zoom_link"
felsefe = "zoom_link"
muzik = "zoom_link"
rehberlik = "zoom_link"
def saat_disi():
    while True:
        pencere.mainloop() #warning window when entering at wrong time
def saaat(): #print the clock
    if len(str(dakika))==1:
        print("Saat: "+str(saat)+":"+"0"+str(dakika))
    else:
        print("Saat: "+str(saat)+":"+str(dakika))


def reh():  #choosing between two different teachers in the guidance lesson
    class Ui_dialog(object):
        def setupUi(self, dialog):
            dialog.setObjectName("dialog")
            dialog.resize(400, 109)
            font = QtGui.QFont()
            font.setFamily("Malgun Gothic")
            font.setBold(True)
            font.setWeight(75)
            dialog.setFont(font)
            self.label = QtWidgets.QLabel(dialog)
            self.label.setGeometry(QtCore.QRect(20, 30, 361, 31))
            font = QtGui.QFont()
            font.setFamily("Malgun Gothic Semilight")
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStrikeOut(False)
            font.setKerning(False)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(dialog)
            self.pushButton.setGeometry(QtCore.QRect(100, 70, 81, 23))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(self.asu)
            self.pushButton_2 = QtWidgets.QPushButton(dialog)
            self.pushButton_2.setGeometry(QtCore.QRect(220, 70, 81, 23))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_2.clicked.connect(self.ferdy)

            self.retranslateUi(dialog)
            QtCore.QMetaObject.connectSlotsByName(dialog)

        def asu(self):
            webbrowser.open(edebiyat)

        def ferdy(self):
            webbrowser.open(rehberlik)

        def retranslateUi(self, dialog):
            _translate = QtCore.QCoreApplication.translate
            dialog.setWindowTitle(_translate("dialog", "Öğretmen seçimi"))
            self.label.setText(_translate("dialog", "Rehberlik dersinde hangi hocanın dersine girmek istiyorsun?"))
            self.pushButton.setText(_translate("dialog", "Asuman Hoca"))
            self.pushButton_2.setText(_translate("dialog", "Ferdi Hoca"))

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_dialog()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

#main program
def sistem():
    if zaman.tm_wday == 0:
        print("Pazartesi")
        saaat()
        if saat == 8 and 59 >= dakika >= 20:
            webbrowser.open(din)
            print("1.ders")
        elif saat == 9 and 41 >= dakika >= 0:
            webbrowser.open(din)
            print("2.ders")
        elif saat == 9 and 59 >= dakika >= 40:
            webbrowser.open(matematik)
            print("3.ders")
        elif saat == 10 and 0 <= dakika <= 19:
            webbrowser.open(matematik)
            print("3.ders")
        elif saat == 10 and 20 <= dakika <= 59:
            webbrowser.open(matematik)
            print("4.ders")
        elif saat == 11 and 0 <= dakika <= 40:
            webbrowser.open(almanca)
            print("5.ders")
        elif saat == 11 and 41 <= dakika <= 59:
            webbrowser.open(almanca)
            print("6.ders")
        elif saat == 12 and 0 <= dakika <= 20:
            webbrowser.open(almanca)
            print("6.ders")
        elif saat == 12 and 21 <= dakika <= 59:
            webbrowser.open(muzik)
            print("7.ders")
        elif saat == 13 and 0 <= dakika <= 20:
            webbrowser.open(muzik)
            print("7.ders")
        elif saat == 13 and 21 <= dakika <= 59:
            webbrowser.open(muzik)
            print("8.ders")
        else:
            saat_disi()

    elif zaman.tm_wday == 1:
        print("Salı")
        saaat()
        if saat == 8 and 59 >= dakika >= 20:
            webbrowser.open(kimya)
            print("1.ders")
        elif saat == 9 and 41 >= dakika >= 0:
            webbrowser.open(kimya)
            print("2.ders")
        elif saat == 9 and 59 >= dakika >= 40:
            webbrowser.open(tarih)
            print("3.ders")
        elif saat == 10 and 0 <= dakika <= 19:
            webbrowser.open(tarih)
            print("3.ders")
        elif saat == 10 and 20 <= dakika <= 59:
            webbrowser.open(tarih)
            print("4.ders")
        elif saat == 11 and 0 <= dakika <= 40:
            reh()
            print("5.ders")
        elif saat == 11 and 41 <= dakika <= 59:
            reh()
            print("6.ders")
        elif saat == 12 and 0 <= dakika <= 20:
            reh()
            print("6.ders")
        elif saat == 12 and 21 <= dakika <= 59:
            webbrowser.open(ingilizce)
            print("7.ders")
        elif saat == 13 and 0 <= dakika <= 19:
            webbrowser.open(ingilizce)
            print("7.ders")
        elif saat == 13 and 20 <= dakika <= 59:
            webbrowser.open(ingilizce)
            print("8.ders")
        else:
            saat_disi()

    elif zaman.tm_wday == 2:
        print("Çarşamba")
        saaat()
        if saat == 8 and 59 >= dakika >= 20:
            webbrowser.open(biyoloji)
            print("1.ders")
        elif saat == 9 and 41 >= dakika >= 0:
            webbrowser.open(biyoloji)
            print("2.ders")
        elif saat == 9 and 59 >= dakika >= 40:
            webbrowser.open(ingilizce)
            print("3.ders")
        elif saat == 10 and 0 <= dakika <= 19:
            webbrowser.open(ingilizce)
            print("3.ders")
        elif saat == 10 and 20 <= dakika <= 59:
            webbrowser.open(ingilizce)
            print("4.ders")
        elif saat == 11 and 0 <= dakika <= 40:
            webbrowser.open(felsefe)
            print("5.ders")
        elif saat == 11 and 41 <= dakika <= 59:
            webbrowser.open(felsefe)
            print("6.ders")
        elif saat == 12 and 0 <= dakika <= 20:
            webbrowser.open(felsefe)
            print("6.ders")
        elif saat == 12 and 21 <= dakika <= 59:
            webbrowser.open(beden)
            print("7.ders")
        elif saat == 13 and 0 <= dakika <= 19:
            webbrowser.open(beden)
            print("7.ders")
        elif saat == 13 and 20 <= dakika <= 59:
            webbrowser.open(beden)
            print("8.ders")
        else:
            saat_disi()

    elif zaman.tm_wday == 3:
        print("Perşembe")
        saaat()
        if saat == 8 and 59 >= dakika >= 20:
            webbrowser.open(fizik)
            print("1.ders")
        elif saat == 9 and 41 >= dakika >= 0:
            webbrowser.open(fizik)
            print("2.ders")
        elif saat == 9 and 59 >= dakika >= 40:
            webbrowser.open(edebiyat)
            print("3.ders")
        elif saat == 10 and 0 <= dakika <= 19:
            webbrowser.open(edebiyat)
            print("3.ders")
        elif saat == 10 and 20 <= dakika <= 59:
            webbrowser.open(edebiyat)
            print("4.ders")
        elif saat == 11 and 0 <= dakika <= 40:
            webbrowser.open(matematik)
            print("5.ders")
        elif saat == 11 and 41 <= dakika <= 59:
            webbrowser.open(matematik)
            print("6.ders")
        elif saat == 12 and 0 <= dakika <= 20:
            webbrowser.open(matematik)
            print("6.ders")
        elif saat == 12 and 21 <= dakika <= 59:
            webbrowser.open(biyoloji)
            print("7.ders")
        elif saat == 13 and 0 <= dakika <= 19:
            webbrowser.open(biyoloji)
            print("7.ders")
        elif saat == 13 and 20 <= dakika <= 59:
            webbrowser.open(biyoloji)
            print("8.ders")
        else:
            saat_disi()

    elif zaman.tm_wday == 4:
        print("Cuma")
        saaat()
        if saat == 8 and 59 >= dakika >= 20:
            webbrowser.open(matematik)
            print("1.ders")
        elif saat == 9 and 41 >= dakika >= 0:
            webbrowser.open(matematik)
            print("2.ders")
        elif saat == 9 and 59 >= dakika >= 40:
            webbrowser.open(fizik)
            print("3.ders")
        elif saat == 10 and 0 <= dakika <= 19:
            webbrowser.open(fizik)
            print("3.ders")
        elif saat == 10 and 20 <= dakika <= 59:
            webbrowser.open(fizik)
            print("4.ders")
        elif saat == 11 and 0 <= dakika <= 40:
            webbrowser.open(kimya)
            print("5.ders")
        elif saat == 11 and 41 <= dakika <= 59:
            webbrowser.open(kimya)
            print("6.ders")
        elif saat == 12 and 0 <= dakika <= 20:
            webbrowser.open(kimya)
            print("6.ders")
        elif saat == 12 and 21 <= dakika <= 59:
            webbrowser.open(edebiyat)
            print("7.ders")
        elif saat == 13 and 0 <= dakika <= 19:
            webbrowser.open(edebiyat)
            print("7.ders")
        elif saat == 13 and 20 <= dakika <= 59:
            webbrowser.open(edebiyat)
            print("8.ders")
        else:
            saat_disi()
    else:
        saat_disi()

sistem()




