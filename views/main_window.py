from typing import List, Dict

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUI()

  def setupUI(self):
    uic.loadUi("views/main.ui", self)

  def connect_add(self, method):
    self.addBtn.clicked.connect(method)

  def connect_edit(self, method):
    self.editBtn.clicked.connect(method)

  def connect_delete(self, method):
    self.delBtn.clicked.connect(method)

  def set_books(self, books: List[Dict]):
    self.bookTbl.clear()
    self.bookTbl.setColumnCount(2)
    self.bookTbl.setHorizontalHeaderLabels(['Название', "Авторы"])
    self.bookTbl.setRowCount(len(books))
    for i, book in enumerate(books):
      item = QTableWidgetItem(book['name'])
      item.setData(Qt.UserRole, book['id'])
      self.bookTbl.setItem(i, 0, item)
      self.bookTbl.setItem(i, 1, QTableWidgetItem(book['authors']))

  def get_current_id(self):
    selected_row =  self.bookTbl.selectedIndexes()[0].row()
    return self.bookTbl.item(selected_row, 0).data(Qt.UserRole)

if __name__ == '__main__':
    app = QApplication([])

    main = MainWindow()
    main.show()

    app.exec()
