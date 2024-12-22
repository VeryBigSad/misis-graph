def stable_marriage(
    men_preferences: list[list[int]], women_preferences: list[list[int]]
) -> list[int]:
    """
    Реализует алгоритм Гейла-Шепли для решения задачи о стабильных браках.

    Алгоритм находит стабильное паросочетание между двумя множествами равного размера
    (мужчины и женщины), где каждый человек ранжировал всех представителей противоположного
    множества в порядке предпочтения. Паросочетание считается стабильным, когда не существует
    двух людей из противоположных множеств, которые предпочли бы друг друга своим
    текущим партнерам.

    Аргументы:
        men_preferences: Список списков, где men_preferences[i] содержит предпочтения i-го мужчины
                        относительно всех женщин, упорядоченные по убыванию предпочтения
                        (0 - наиболее предпочтительный вариант)
        women_preferences: Список списков, где women_preferences[i] содержит предпочтения i-й женщины
                          относительно всех мужчин, упорядоченные по убыванию предпочтения
                          (0 - наиболее предпочтительный вариант)

    Возвращает:
        Список, где индекс i представляет женщину i, а значение представляет мужчину,
        с которым она образует пару. Например, если result[2] = 1, то женщина 2
        образует пару с мужчиной 1.
    """
    n = len(men_preferences)
    free_men = list(range(n))
    women_partners = [None] * n
    men_next = [0] * n

    while free_men:
        man = free_men.pop(0)
        woman = men_preferences[man][men_next[man]]
        men_next[man] += 1

        if women_partners[woman] is None:
            women_partners[woman] = man
        else:
            current_partner = women_partners[woman]
            if women_preferences[woman].index(man) < women_preferences[woman].index(
                current_partner
            ):
                women_partners[woman] = man
                free_men.append(current_partner)
            else:
                free_men.append(man)

    return women_partners
