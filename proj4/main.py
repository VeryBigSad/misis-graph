from disjoint_set import DisjointSet
import time
import random


def demonstration_example():
    """Простой пример использования структуры данных"""
    ds = DisjointSet(10)

    # Объединяем некоторые элементы
    print("Объединяем элементы 0 и 1")
    ds.union(0, 1)
    print("Объединяем элементы 2 и 3")
    ds.union(2, 3)
    print("Объединяем элементы 0 и 2")
    ds.union(0, 2)

    # Проверяем связность
    print(f"Элементы 1 и 3 связаны: {ds.connected(1, 3)}")  # True
    print(f"Элементы 4 и 5 связаны: {ds.connected(4, 5)}")  # False

    print(f"Количество множеств: {ds.get_num_sets()}")


def performance_test(n=10_000, operations=100_000):
    """
    Тест производительности структуры данных

    Args:
        n (int): Размер структуры данных
        operations (int): Количество операций
    """
    ds = DisjointSet(n)

    # Замеряем время выполнения операций
    start_time = time.time()

    for _ in range(operations):
        # Случайно выбираем между операциями union и find
        if random.random() < 0.5:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            ds.union(x, y)
        else:
            x = random.randint(0, n - 1)
            ds.find(x)

    end_time = time.time()
    print(f"Время выполнения {operations} операций: {end_time - start_time:.3f} секунд")
    print(
        f"Среднее время на операцию: {(end_time - start_time) * 1000000 / operations:.3f} микросекунд"
    )


if __name__ == "__main__":
    print("=== Демонстрационный пример ===")
    demonstration_example()

    print("\n=== Тест производительности ===")
    performance_test(10_000_000, 100_000_000)
