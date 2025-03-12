import pytest

import helpers
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name, books_count', [(['Сияние'], 1), (['Сияние', 'Доктор Айболит'], 2), ([], 0)])
    def test_add_new_book_add_one_two_zero_books(self, book, name, books_count):
        for book_name in name:
            book.add_new_book(book_name)
        assert len(book.get_books_genre()) == books_count

    def test_set_book_genre_set_genre_to_new_book(self, book):
        book.add_new_book('Сияние')
        book.set_book_genre('Сияние', 'Ужасы')
        assert book.get_book_genre('Сияние') == 'Ужасы'

