
def create_question_file(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Прізвище: Кобзар\n")
            file.write("Питання: Як у Python реалізувати обробку виключень?\n")
        print(f"Файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")

create_question_file("question.txt")

#Сема
def add_answer_to_file(filename):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write("\nПрізвище: Сема\n")

            file.write("Відповідь: У Python обробку виключень реалізують за допомогою конструкції try-except.\n")
            file.write("Основні блоки:\n")
            file.write("1. try - виконує код, який може викликати виняток\n")
            file.write("2. except - обробляє виняток, якщо він виник\n")
            file.write("3. else - виконується, якщо винятку не було\n")
            file.write("4. finally - виконується завжди, незалежно від винятків\n")
            file.write("Приклад:\n")
            file.write("try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Ділення на нуль!')\n")

            file.write("\nПитання: Що таке генератори у Python та як їх використовувати?\n")

        print(f"Відповідь успішно додано до файлу '{filename}'")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

add_answer_to_file("question.txt")
