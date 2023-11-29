#1
def are_characters_hidden(word, combination):
    word = word.lower()  # перетворюємо слово у нижній регістр для незалежності від регістру
    combination = combination.lower()  # те ж саме робимо з комбінацією символів

    index = -1  # починаємо з індексу -1, щоб шукати символи слова з самого початку
    for char in word:
        index = combination.find(char, index + 1)  # шукаємо кожен символ слова в комбінації, починаючи з наступного індексу

        if index == -1:
            return False  # якщо який-небудь символ слова не знайдено, відповідь - No

    return True  # якщо всі символи слова знайдено, відповідь - Yes

# Приклад використання:
word_example = "dog"
combination_example_1 = "vcxzxduybfdsobywuefgas"
combination_example_2 = "vcxzxdcybfdstbywuefsas"

result_1 = are_characters_hidden(word_example, combination_example_1)
result_2 = are_characters_hidden(word_example, combination_example_2)

print("Відповідь для комбінації 1:", "Yes" if result_1 else "No")
print("Відповідь для комбінації 2:", "Yes" if result_2 else "No")

#2
def calculate_life_number(date):
    try:
        # Видалення всіх символів, окрім цифр
        digits = ''.join(filter(str.isdigit, date))

        # Вирахування суми цифр
        digit_sum = sum(int(d) for d in digits)

        # Повторення додавання, якщо результат містить більше однієї цифри
        while digit_sum > 9:
            digit_sum = sum(int(d) for d in str(digit_sum))

        return digit_sum
    except Exception as e:
        print(f"Помилка: {e}")
        return None

# Запит дати народження користувача
while True:
    try:
        date = input("Введіть дату народження у форматі YYYYMMDD, РРРРДДММ або ММДДРРРР: ")
        life_number = calculate_life_number(date)

        if life_number is not None:
            print(f"Цифра життя для дати {date}: {life_number}")
            break
    except Exception as e:
        print(f"Помилка: {e}")

#3
def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))

            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
        except ValueError:
            print("Error: wrong input. Please enter an integer.")

# Приклад використання:
try:
    user_value = get_integer_input("Введіть ціле число: ", 1, 10)
    print(f"Ви ввели: {user_value}")
except KeyboardInterrupt:
    print("\nВведення перервано.")