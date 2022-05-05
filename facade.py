from main import sparsetable
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import sys
from sql import SqlDB

class prog:
    # Объявляем классы
    def __init__(self):
        self.sptable = sparsetable()
        self.sql = SqlDB()
        self.nlist = []

    # Указывваем текущее окно, чтобы фасад знал, с каким окном работаем
    def WinSel(self, curwin):
        self.window = curwin

    # Обновляем таблицу
    def tUpd(self):
        while self.window.table.rowCount() > 0:
            self.window.table.removeRow(0)

        for i in range(len(self.nlist)):
            self.window.table.insertRow(i)
            self.window.table.setItem(i, 0, QTableWidgetItem(str(self.nlist[i])))

    # Стираем таблицу
    def Clear(self):
        self.nlist.clear()
        self.tUpd()

    # Добавляем элемент
    def Add(self):
        if self.window.lineEdit.text().isdigit():
            num = int(self.window.lineEdit.text())
            self.nlist.append(num)
            self.tUpd()

    # Ищем минамальный элемент
    def Min_sparse(self):
        self.sptable.buildSparseTable(self.nlist)
        n1 = int(self.window.LE_From.text()) - 1
        n2 = int(self.window.LE_To.text()) - 1
        result = str(self.sptable.query(n1, n2))
        self.window.ResultTxt.setText(result)

    # Сохраняем структуру в БД
    def SaveDB(self):
        SqlDB().save(self.nlist, self.window.FileLine.text())

    # Загружаем структуру в БД
    def LoadDB(self):
        tbl = SqlDB().load(self.window.FileLine.text())

        self.nlist.clear()
        for row in tbl:
            self.nlist.append(row[1])

        self.tUpd()
