import random


def generate_random_book():
    titles = ['Сияние', 'Доктор Айболит', 'Смерть на Ниле', 'Калоша', 'Вино из одуванчиков', 'Оно', 'Лисьи броды']
    return random.choice(titles)

def generate_random_genre():
    genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    return random.choice(genres)


def generate_books_genre_dictionary(number_of_books):
    books_genre = {}

    for i in range(number_of_books):
        book_title = generate_random_book()
        book_genre = generate_random_genre()
        books_genre[book_title] = book_genre

    return books_genre