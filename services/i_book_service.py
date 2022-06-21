from abc import ABC, abstractmethod
from typing import List, Dict


class IBookService(ABC):
  @abstractmethod
  def add(self, book_dto: Dict):
    pass

  @abstractmethod
  def update(self, book_dto: Dict):
    pass

  @abstractmethod
  def delete(self, book_dto: Dict):
    pass

  @abstractmethod
  def all(self) -> List[Dict]:
    pass

