import pytest

import helpers
from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


