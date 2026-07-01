class ArrayAnalyzer:
    def __init__(self, array_data):
        self.array_data = array_data
        self.n = len(array_data)

    def get_positive_stats(self):
        sum_pos = sum(x for x in self.array_data if x > 0)
        count_pos = sum(1 for x in self.array_data if x > 0)
        return sum_pos, count_pos

# Исходные данные
N = 5
A = [12, -5, 0, 8, -3]

# Использование
analyzer = ArrayAnalyzer(A)
total_sum, total_count = analyzer.get_positive_stats()

print(f"Массив А: {A}")
print(f"Сумма положительных элементов: {total_sum}")
print(f"Количество положительных элементов: {total_count}")