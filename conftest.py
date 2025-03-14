import pytest

import helpers
from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book

@pytest.fixture
def book_with_1_favorite_book(book):
    book.add_new_book('Сияние')
    book.add_book_in_favorites('Сияние')
    return book
