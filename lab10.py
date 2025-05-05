
def create_question_file(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Прізвище: Кобзар\n")
            file.write("Питання: Як у Python реалізувати обробку виключень?\n")
        print(f"Файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")

create_question_file("question.txt")
