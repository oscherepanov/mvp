from typing import List

from data_access.db import DB
from model.book import Book
from repository.i_book_repository import IBookRepository


class BookRepositoryImpl(IBookRepository):
  def __init__(self, db: DB):
    self._db = db

  def add(self, book:Book):
    self._db.insert(book)

  def update(self, book: Book):
    self._db.update(book)

  def delete(self, id: int):
    self._db.delete(id)

  def all(self) -> List[Book]:
    return self._db.all()
