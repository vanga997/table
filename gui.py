from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from  facade import prog
import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.func = prog()
        self.initUI()

    def initUI(self):
        #Загружаем форму
        uic.loadUi('window.ui', self)
        self.setWindowTitle('Прога')
        # Указываем текущую окно фасаду
        self.func.WinSel(self)
        # Назначем кнопки к функциям фасадам
        self.pushButton.clicked.connect(self.func.Add)
        self.pushButton_2.clicked.connect(self.func.Clear)
        self.pushButton_3.clicked.connect(self.func.Min_sparse)
        self.save_btn.clicked.connect(self.func.SaveDB)
        self.load_btn.clicked.connect(self.func.LoadDB)
        self.ResultTxt.setFont(QFont('Arial', 20))
        # настраиваем таблицу
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Число"])
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # Показываем окно
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec_())