from typing import Dict

from model.book import Book


class BookMapper:
  @staticmethod
  def to_dto(book: Book) -> Dict:
    return {
      "name": book.get_name(),
      "authors": book.get_author(),
      "id": book.get_id()
    }

  @staticmethod
  def to_entity(dto: Dict) -> Book:
    return Book(dto["name"], dto['authors'], dto['id'])
