import random

class FruitGame:
    def __init__(self):
        self.fruits = ["яблоко", "банан", "груша", "апельсин", "ананас"]
        self.random_fruit = self.get_random_fruit()
        self.attempts = 0

    def get_random_fruit(self):
        """Выбирает случайный фрукт из списка фруктов."""
        return random.choice(self.fruits)

    def check_guess(self, guess):
        """Проверяет, совпадает ли угаданный фрукт с загаданным фруктом."""
        self.attempts += 1
        if guess.lower() == self.random_fruit:
            return True
        else:
            return False

    def get_hint(self):
        """Возвращает подсказку - первую букву загаданного фрукта."""
        return self.random_fruit[0]

    def get_score(self):
        """Возвращает текущий счет игры."""
        return self.attempts

    def reset_game(self):
        """Сбрасывает состояние игры, выбирает новый случайный фрукт и сбрасывает счетчик попыток."""
        self.random_fruit = self.get_random_fruit()
        self.attempts = 0

    def get_all_fruits(self):
        """Возвращает список всех доступных фруктов."""
        return self.fruits

    def set_difficulty(self, difficulty):
        """Устанавливает уровень сложности, изменяя список фруктов в зависимости от выбранного уровня."""
        if difficulty == "easy":
            self.fruits = ["яблоко", "банан", "груша"]
        elif difficulty == "medium":
            self.fruits = ["яблоко", "банан", "груша", "апельсин", "ананас"]
        elif difficulty == "hard":
            self.fruits = ["яблоко", "банан", "груша", "апельсин", "ананас", "манго", "киви"]