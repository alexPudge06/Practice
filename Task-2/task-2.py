import math

class ArrayFilter:
    def __init__(self, array_data):
        self.array_data = array_data

    def get_greater_than_b_stats(self, b):
        filtered = [x for x in self.array_data if x > b]
        count_greater = len(filtered)
        product_greater = math.prod(filtered) if count_greater > 0 else 0
        return count_greater, product_greater

# Исходные данные
A = [2, 7, 4, 9, 1]
B = 5

# Использование
array_filter = ArrayFilter(A)
count, product = array_filter.get_greater_than_b_stats(B)

print(f"Массив А: {A}, Число В: {B}")
print(f"Количество элементов > B: {count}")
print(f"Произведение элементов > B: {product}")