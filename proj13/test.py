import time
from main import stable_marriage


def generate_test_data(n):
    men_preferences = [list(range(n)) for _ in range(n)]
    women_preferences = [list(range(n)) for _ in range(n)]
    for i in range(n):
        men_preferences[i] = men_preferences[i][::-1]  # Обратный порядок предпочтений
    return men_preferences, women_preferences


def performance_test():
    sizes = [10, 100, 500, 1000, 2000]
    for n in sizes:
        men_preferences, women_preferences = generate_test_data(n)
        start_time = time.time()
        stable_marriage(men_preferences, women_preferences)
        end_time = time.time()
        print(f"Размер: {n}, Время выполнения: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    print("Тестирование производительности алгоритма Гэйла — Шепли")
    performance_test()
