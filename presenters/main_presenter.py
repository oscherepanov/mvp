from typing import Dict

from services.i_book_service import IBookService
from views.book_form import BookForm
from views.main_window import MainWindow


class MainPresenter:
  def __init__(self, main_window: MainWindow, service: IBookService):
    self.service = service
    self.main_window = main_window
    self.books = []
    self.connect()
    self.get_all_books()

  def connect(self):
    self.main_window.connect_add(self.add_book)
    self.main_window.connect_edit(self.edit_book)
    self.main_window.connect_delete(self.delete_book)

  def get_all_books(self):
    self.books = self.service.all()
    self.main_window.set_books(self.books)

  def show_book_form(self, book: Dict):
    book_form = BookForm()
    book_form.set_name(book['name'])
    book_form.set_authors(book['authors'])
    if book_form.exec():
      book['name'] = book_form.get_name()
      book['authors'] = book_form.get_authors()
      return True
    return False

  def add_book(self):
    new_book = {"name": "", "authors": "", "id": 0}
    if self.show_book_form(new_book):
      self.service.add(new_book)
    self.get_all_books()

  def current_book(self):
    book_id = self.main_window.get_current_id()
    for i in self.books:
      if i['id'] == book_id:
        return i
    return None

  def edit_book(self):
    book = self.current_book()
    if book:
      if self.show_book_form(book):
        self.service.update(book)
        self.get_all_books()

  def delete_book(self):
    book = self.current_book()
    if book:
      self.service.delete(book)
      self.get_all_books()

