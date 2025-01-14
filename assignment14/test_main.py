from main import greet 

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Gulnara") == "Hello, Gulnara!"
    # test_main.py

# import pytest

# # Определение фикстуры
# @pytest.fixture
# def greet():
#     return "Hello, World!"

# # Тест, использующий фикстуру
# def test_greet(greet):
#     assert greet == "Hello, World!"
# test_main.py

# import pytest
# from main import greet  # Импортируем функцию greet из main.py

# # Определение фикстуры
# @pytest.fixture
# def greet_fixture():
#     return greet  # Фикстура возвращает функцию greet

# # Тест, использующий фикстуру
# def test_greet(greet_fixture):
#     assert greet_fixture("World") == "Hello, World!"
#     assert greet_fixture("Gulnara") == "Hello, Gulnara!"
