from PyQt5.QtWidgets import QApplication

from data_access.db import DB
from presenters.main_presenter import MainPresenter
from repository.book_repository_impl import BookRepositoryImpl
from services.book_service import BookService
from views.main_window import MainWindow

app = QApplication([])

db = DB()
repository = BookRepositoryImpl(db)
service = BookService(repository)
main = MainWindow()
presenter = MainPresenter(main, service)
main.show()

app.exec()
