from typing import List

from model.book import Book


class DB:
  books = {}
  current_id = 1

  def insert(self, book: Book) -> None:
    DB.books[DB.current_id] = book
    book.set_id(DB.current_id)
    DB.current_id += 1

  def update(self, book: Book) -> None:
    if book.get_id() in DB.books:
      DB.books[book.get_id()] = book

  def delete(self, id: int) -> None:
    if id in DB.books:
      del DB.books[id]

  def all(self) -> List[Book]:
    return list(DB.books.values())


if __name__ == '__main__':
  db = DB()
  print(db.all())

  db.insert(Book("asdasd", "asdads"))
  print(db.all())

  db.update(Book("asdasd1", "asdads1", 1))
  print(db.all())

  db.delete(1)
  print(db.all())

