import random

def generate_numbers():
    numbers = []
    print("Программа генерации чисел. Введите '0', чтобы остановиться.")
    
    while True:
        user_input = input("Нажмите Enter для генерации или введите '0' для выхода: ")
        if user_input == '0':
            break
        
        # Генерируем случайное число от 1 до 100
        new_number = random.randint(1, 100)
        numbers.append(new_number)
        print(f"Сгенерировано: {new_number}")

    # Выводим все сгенерированные числа, кроме последнего
    if len(numbers) > 1:
        print("\nВсе числа, кроме последнего:", numbers[:-1])
    else:
        print("\nСгенерировано недостаточно чисел для вывода (нужно минимум 2).")

if __name__ == "__main__":
    generate_numbers()