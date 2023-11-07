import pytest
from FruitGame import FruitGame

# Тесты для класса FruitGame
def test_check_guess():
    game = FruitGame()
    assert game.check_guess(game.random_fruit) == True
    assert game.check_guess("манго") == False
def test_get_hint():
    game = FruitGame()
    assert game.get_hint() == game.random_fruit[0]
def test_reset_game():
    game = FruitGame()
    initial_fruit = game.random_fruit
    initial_attempts = game.attempts
    game.reset_game()
    assert game.random_fruit != initial_fruit
    assert game.attempts == 0
def test_get_all_fruits():
    game = FruitGame()
    assert game.get_all_fruits() == ["яблоко", "банан", "груша", "апельсин", "ананас"]
def test_set_difficulty():
    game = FruitGame()
    game.set_difficulty("easy")
    assert game.get_all_fruits() == ["яблоко", "банан", "груша"]
    game.set_difficulty("medium")
    assert game.get_all_fruits() == ["яблоко", "банан", "груша", "апельсин", "ананас"]
    game.set_difficulty("hard")
    assert game.get_all_fruits() == ["яблоко", "банан", "груша", "апельсин", "ананас", "манго", "киви"]