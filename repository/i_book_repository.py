from abc import ABC, abstractmethod
from typing import List

from model.book import Book


class IBookRepository(ABC):
  @abstractmethod
  def add(self, book:Book):
    pass

  @abstractmethod
  def update(self, book: Book):
    pass

  @abstractmethod
  def delete(self, id: int):
    pass

  @abstractmethod
  def all(self) -> List[Book]:
    pass


