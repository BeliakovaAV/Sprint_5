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
        book.books_genre = data.BOOK_GENRE
        books_with_specific_genre = book.get_books_with_specific_genre(genre)
        assert len(books_with_specific_genre) > 0
        for name in books_with_specific_genre:
            assert book.books_genre[name] == genre

    @pytest.mark.parametrize('genre', ['', 'Фэнтези', 468])
    def test_get_books_with_specific_genre_negative(self, book, genre):
        book.books_genre = data.BOOK_GENRE
        books_with_specific_genre = book.get_books_with_specific_genre(genre)
        assert len(books_with_specific_genre) == 0

    def test_get_books_for_children_positive_and_negative(self, book):
        book.books_genre = data.BOOK_GENRE
        books_for_children = book.get_books_for_children()
        expected_result = ['Доктор Айболит', 'Вино из одуванчиков', 'Калоша']
        assert len(books_for_children) > 1
        assert books_for_children == expected_result

    @pytest.mark.parametrize('name, books_count', [(['Сияние'], 1), (['Сияние', 'Доктор Айболит'], 2), ([], 0)])
    def test_add_book_in_favorites_add_one_two_zero_books(self, book, name, books_count):
        book.books_genre = data.BOOK_GENRE
        for book_name in name:
            book.add_book_in_favorites(book_name)
        assert len(book.get_list_of_favorites_books()) == books_count

    def test_add_book_in_favorites_if_book_already_in_favorites(self, book, book_with_1_favorite_book):
        book_with_1_favorite_book.add_book_in_favorites('Сияние')
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == 1

    def test_delete_book_from_favorites(self, book, book_with_1_favorite_book):
        book_with_1_favorite_book.favorites.remove('Сияние')
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == 0

    @pytest.mark.parametrize('name, actual_genre', [('Сияние', 'Ужасы'), ('Доктор Айболит', 'Мультфильмы'), ('Калоша', 'Комедии')])
    def test_get_book_genre_book_in_books_genre_dict(self, book, name, actual_genre):
        book.books_genre = data.BOOK_GENRE
        genre = book.get_book_genre(name)
        assert genre == actual_genre

    def test_get_books_genre_filled(self, book):
        book.books_genre = data.BOOK_GENRE
        books_list = book.get_books_genre()
        assert books_list == data.BOOK_GENRE

    def test_get_books_genre_empty(self, book):
        book.books_genre = {}
        books_list = book.get_books_genre()
        assert books_list == {}