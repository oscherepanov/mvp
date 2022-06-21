from typing import Dict, List

from mapper.book_mapper import BookMapper
from repository.i_book_repository import IBookRepository
from services.i_book_service import IBookService


class BookService(IBookService):
  def __init__(self, repository: IBookRepository):
    self.repository = repository

  def add(self, book_dto: Dict):
    self.repository.add(BookMapper.to_entity(book_dto))

  def update(self, book_dto: Dict):
    self.repository.update(BookMapper.to_entity(book_dto))

  def delete(self, book_dto: Dict):
    self.repository.delete(book_dto['id'])

  def all(self) -> List[Dict]:
    return [BookMapper.to_dto(i) for i in self.repository.all()]
