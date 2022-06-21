from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QWidget, QApplication


class BookForm(QDialog):
  def __init__(self, parent: QWidget = None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.setupUI()

  def setupUI(self):
    uic.loadUi("views/book_form.ui", self)

  def get_name(self):
    return self.nameEdit.text()

  def set_name(self, name :str):
    self.nameEdit.setText(name)

  def get_authors(self):
    return self.authorsEdit.text()

  def set_authors(self, name: str):
    self.authorsEdit.setText(name)


if __name__ == '__main__':

    def ok():
      print("ok")

    app = QApplication([])

    book_form = BookForm()
    book_form.set_authors("Толстой")
    book_form.set_name("Война и мир")

    book_form.connect_ok(ok)
    book_form.show()

    app.exec()
