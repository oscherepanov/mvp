class Book:
  def __init__(self, name: str, author: str, id: int = 0):
    self._name = name
    self._author = author
    self._id = id

  def set_name(self, name: str) -> None:
    self._name = name

  def get_name(self) -> str:
    return self._name

  def set_author(self, author: str) -> None:
    self._name = author

  def get_author(self) -> str:
    return self._author

  def set_id(self, id: int) -> None:
    self._id = id

  def get_id(self) -> int:
    return self._id

  def __repr__(self):
    return f'Book: name={self._name}, authors={self._author}, id={self._id}'
