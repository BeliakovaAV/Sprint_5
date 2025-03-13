import pytest

import data
import helpers
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name, books_count', [(['Сияние'], 1), (['Сияние', 'Доктор Айболит'], 2), ([], 0)])
    def test_add_new_book_add_one_two_zero_books(self, book, name, books_count):
        for book_name in name:
            book.add_new_book(book_name)
        assert len(book.get_books_genre()) == books_count

    def test_set_book_genre_set_genre_to_new_book(self, book):
        book_name = helpers.generate_random_book()
        book_genre = helpers.generate_random_genre()
        book.add_new_book(book_name)
        book.set_book_genre(book_name, book_genre)
        assert book.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre (self, book, genre):
        books_with_specific_genre = []
        for name, book_genre in data.BOOK_GENRE.items():
            if book_genre == genre:
                books_with_specific_genre.append(name)
                assert books_with_specific_genre == [name]
