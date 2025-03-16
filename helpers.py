import random


def generate_random_book():
    titles = ['Сияние', 'Доктор Айболит', 'Смерть на Ниле', 'Калоша', 'Вино из одуванчиков', 'Оно', 'Лисьи броды']
    return random.choice(titles)

def generate_random_genre():
    genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    return random.choice(genres)

