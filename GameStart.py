from FruitGame import FruitGame
def play_fruit_game():
    game = FruitGame()

    # Выбор уровня сложности
    print("Добро пожаловать в игру 'Угадай фрукт'!")
    print("Выберите уровень сложности:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Тяжелый")
    difficulty_choice = input("Введите номер уровня сложности (1, 2 или 3): ")
    print()

    if difficulty_choice == "1":
        game.set_difficulty("easy")
    elif difficulty_choice == "2":
        game.set_difficulty("medium")
    elif difficulty_choice == "3":
        game.set_difficulty("hard")

    all_fruits = game.get_all_fruits()
    print("Список фруктов:", ", ".join(all_fruits))
    print()

    print("Я загадаю случайный фрукт, а вы должны попытаться его угадать.")
    print("Для выхода из игры введите 'exit'.")
    print()

    while True:
        guess = input("Введите название фрукта: ")
        if guess.lower() == "exit":
            print("Спасибо за игру! До свидания!")
            break

        if game.check_guess(guess):
            print("Вы угадали! Поздравляю!")
            print("Загаданный фрукт был:", game.random_fruit)
            print("Количество попыток:", game.get_score())
            print()
            game.reset_game()
        else:
            hint = game.get_hint()
            print("Вы не угадали. Попробуйте еще раз.")
            print("Подсказка: первая буква фрукта -", hint)
            print()

play_fruit_game()