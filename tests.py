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

    def test_add_new_book_add_already_added_book(self, book):
        book.add_new_book('Сияние')
        book.add_new_book('Сияние')
        new_books = book.get_books_genre()
        assert len(new_books) == 1

    def test_set_book_genre_set_genre_to_new_book(self, book):
        book_name = helpers.generate_random_book()
        book_genre = helpers.generate_random_genre()
        book.add_new_book(book_name)
        book.set_book_genre(book_name, book_genre)
        assert book.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_positive(self, book, genre):
        books_with_specific_genre = []
        for name, book_genre in data.BOOK_GENRE.items():
            if book_genre == genre:
                books_with_specific_genre.append(name)
        assert len(books_with_specific_genre) > 0

    @pytest.mark.parametrize('genre', ['', 'Фэнтези', 468])
    def test_get_books_with_specific_genre_negative(self, book, genre):
        books_with_specific_genre = []
        if data.BOOK_GENRE and genre in book.genre:
            for name, book_genre in data.BOOK_GENRE.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        assert len(books_with_specific_genre) == 0

    def test_get_books_for_children_positive_and_negative(self, book):
        books_for_children = []
        for name, genre in data.BOOK_GENRE.items():
            if genre not in book.genre_age_rating and genre in book.genre:
                books_for_children.append(name)
        assert len(books_for_children) > 1

    @pytest.mark.parametrize('name, books_count', [(['Сияние'], 1), (['Сияние', 'Доктор Айболит'], 2), ([], 0)])
    def test_add_book_in_favorites_add_one_two_zero_books(self, book, name, books_count):
        for book_name in name:
            if book_name in data.BOOK_GENRE:
                book.favorites.append(book_name)
        assert len(book.get_list_of_favorites_books()) == books_count
        for book_name in name:
            if book_name in data.BOOK_GENRE:
                assert book_name in book.get_list_of_favorites_books()

    def test_add_book_in_favorites_if_book_already_in_favorites(self, book, book_with_1_favorite_book):
        book_with_1_favorite_book.add_book_in_favorites('Сияние')
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == 1

    def test_delete_book_from_favorites(self, book, book_with_1_favorite_book):
        book_with_1_favorite_book.favorites.remove('Сияние')
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == 0



