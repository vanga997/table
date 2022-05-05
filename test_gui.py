from unittest import TestCase

import sys
from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QWidget

from gui import MainWindow


class MyTestCase(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()

    def test_add(self):
        QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineEdit.setText("trash")
        QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineEdit.setText("69")
        QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        self.assertEqual(self.window.table.item(0, 0).text(), '69')

    def test_clear(self):
        self.window.lineEdit.setText("123")
        for i in range(20):
            QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.pushButton_2, QtCore.Qt.MouseButton.LeftButton)
        self.window.lineEdit.setText("1")
        QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        self.assertEqual(self.window.table.item(0, 0).text(), '1')

    def test_min(self):
        ls = [3, 2, 8, 5, 11, 4]
        for i in ls:
            self.window.lineEdit.setText(str(i))
            QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        self.window.LE_From.setText("2")
        self.window.LE_To.setText("5")
        QTest.mouseClick(self.window.pushButton_3, QtCore.Qt.MouseButton.LeftButton)
        self.assertEqual(self.window.ResultTxt.text(),'2')

    def test_saveload(self):
        ls = [10, 5, 6, 8, 3, 4]
        for i in ls:
            self.window.lineEdit.setText(str(i))
            QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)

        self.window.FileLine.setText("temp.db")
        QTest.mouseClick(self.window.save_btn, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.pushButton_2, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.pushButton, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.load_btn, QtCore.Qt.MouseButton.LeftButton)

        n=0
        for i in ls:
            self.assertEqual(self.window.table.item(n, 0).text(), str(i))
            n+=1
        os.remove("temp.db")
