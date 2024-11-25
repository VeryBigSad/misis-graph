class DisjointSet:
    def __init__(self, size):
        """
        Инициализация структуры данных системы непересекающихся множеств.

        Args:
            size (int): Количество элементов в структуре
        """
        # parent[i] хранит родителя элемента i
        self.parent = list(range(size))
        # rank[i] хранит ранг (приближенную высоту) поддерева с корнем i
        self.rank = [0] * size
        # Количество элементов
        self.size = size
        # Количество множеств
        self.num_sets = size

    def find(self, x):
        """
        Поиск представителя множества, содержащего элемент x,
        с применением оптимизации сжатия пути.

        Args:
            x (int): Элемент, для которого ищется представитель

        Returns:
            int: Представитель множества
        """
        # Если элемент не является своим собственным родителем
        if self.parent[x] != x:
            # Рекурсивно находим корень и обновляем родителя (сжатие пути)
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Объединение множеств, содержащих элементы x и y,
        с применением ранговой эвристики.

        Args:
            x (int): Элемент первого множества
            y (int): Элемент второго множества

        Returns:
            bool: True если элементы были в разных множествах, False иначе
        """
        root_x = self.find(x)
        root_y = self.find(y)

        # Если элементы уже в одном множестве
        if root_x == root_y:
            return False

        # Объединяем деревья по рангу
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.num_sets -= 1
        return True

    def get_num_sets(self):
        """
        Получить текущее количество множеств.

        Returns:
            int: Количество множеств
        """
        return self.num_sets

    def connected(self, x, y):
        """
        Проверка, находятся ли элементы в одном множестве.

        Args:
            x (int): Первый элемент
            y (int): Второй элемент

        Returns:
            bool: True если элементы в одном множестве, False иначе
        """
        return self.find(x) == self.find(y)
