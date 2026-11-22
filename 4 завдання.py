
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Програма демонстрації операцій над множинами.
Побудова множин з колекцій з повторами та операції над ними.
"""

def load_collections():
    """
    Завантаження двох вхідних колекцій ідентифікаторів.
    Дані задано як константи в коді (для воспроизводимості).
    """
    print("\n" + "="*70)
    print("ВХІ́ДНІ ДАНІ: Колекції ідентифікаторів")
    print("="*70)

    collection_1 = [
        "Alice", "Bob", "Charlie", "Alice", "David",
        "Eve", "Bob", "Frank", "Charlie", "Alice",
        "George", "Henry", "Bob"
    ]

    collection_2 = [
        "Charlie", "David", "Frank", "Grace",
        "Henry", "Ivy", "David", "Frank",
        "Charlie", "Jack", "Grace", "Henry"
    ]

    print("\nКолекція 1 (з повторами):")
    print(f"  {collection_1}")
    print(f"  Довжина: {len(collection_1)}")

    print("\nКолекція 2 (з повторами):")
    print(f"  {collection_2}")
    print(f"  Довжина: {len(collection_2)}")

    return collection_1, collection_2

def build_sets(collection_1, collection_2):
    """
    Побудова множин унікальних значень з колекцій.
    """
    print("\n" + "="*70)
    print("ПОБУДОВА МНОЖИН УНІКАЛЬНИХ ЗНАЧЕНЬ")
    print("="*70)

    set_1 = set(collection_1)
    set_2 = set(collection_2)

    print("\nМножина 1 (унікальні значення з колекції 1):")
    print(f"  set_1 = {sorted(set_1)}")
    print(f"  Кількість унікальних: {len(set_1)}")

    print("\nМножина 2 (унікальні значення з колекції 2):")
    print(f"  set_2 = {sorted(set_2)}")
    print(f"  Кількість унікальних: {len(set_2)}")

    return set_1, set_2

def intersection_operation(set_1, set_2):
    """
    Операція ПЕРЕТИН (intersection).
    Елементи, які присутні в обох множинах.
    """
    print("\n" + "="*70)
    print("ОПЕРАЦІЯ 1: ПЕРЕТИН (Intersection)")
    print("="*70)

    result = set_1 & set_2

    print("\nСинтаксис: set_1 & set_2")
    print("Семантика: Елементи, присутні в обох множинах одночасно")
    print(f"\nРезультат (відсортовано):")
    print(f"  {sorted(result)}")
    print(f"  Кількість: {len(result)}")

    return result

def union_operation(set_1, set_2):
    """
    Операція ОБ'ЄДНАННЯ (union).
    Усі елементи з обох множин (без дублятів).
    """
    print("\n" + "="*70)
    print("ОПЕРАЦІЯ 2: ОБ'ЄДНАННЯ (Union)")
    print("="*70)

    result = set_1 | set_2

    print("\nСинтаксис: set_1 | set_2")
    print("Семантика: Всі унікальні елементи з обох множин")
    print(f"\nРезультат (відсортовано):")
    print(f"  {sorted(result)}")
    print(f"  Кількість: {len(result)}")

    return result

def difference_operation(set_1, set_2):
    """
    Операція РІЗНИЦЯ (difference).
    Елементи з множини 1, яких немає в множині 2.
    """
    print("\n" + "="*70)
    print("ОПЕРАЦІЯ 3: РІЗНИЦЯ 1 - 2 (Difference)")
    print("="*70)

    result = set_1 - set_2

    print("\nСинтаксис: set_1 - set_2")
    print("Семантика: Елементи в set_1, які не присутні в set_2")
    print(f"\nРезультат (відсортовано):")
    print(f"  {sorted(result)}")
    print(f"  Кількість: {len(result)}")

    return result

def symmetric_difference_operation(set_1, set_2):
    """
    Операція СИМЕТРИЧНА РІЗНИЦЯ (symmetric difference).
    Елементи, які присутні в одній множині, але не в обох одночасно.
    """
    print("\n" + "="*70)
    print("ОПЕРАЦІЯ 4: СИМЕТРИЧНА РІЗНИЦЯ (Symmetric Difference)")
    print("="*70)

    result = set_1 ^ set_2

    print("\nСинтаксис: set_1 ^ set_2")
    print("Семантика: Елементи, які присутні в set_1 XOR в set_2")
    print("           (в одній множині, але не в обох)")
    print(f"\nРезультат (відсортовано):")
    print(f"  {sorted(result)}")
    print(f"  Кількість: {len(result)}")

    return result

def subset_check(set_1, set_2):
    """
    ПЕРЕВІРКА ПІДМНОЖИНИ.
    Чи є set_1 підмножиною set_2?
    """
    print("\n" + "="*70)
    print("ПЕРЕВІРКА 1: ЧИ Є set_1 ПІДМНОЖИНОЮ set_2?")
    print("="*70)

    is_subset = set_1 <= set_2

    print(f"\nОперація: set_1 <= set_2")
    print(f"set_1 = {sorted(set_1)}")
    print(f"set_2 = {sorted(set_2)}")
    print(f"\nРезультат: {is_subset}")

    if is_subset:
        print("Висновок: Усі елементи set_1 присутні в set_2")
    else:
        print("Висновок: Не всі елементи set_1 присутні в set_2")
        missing = set_1 - set_2
        print(f"Елементи в set_1, яких немає в set_2: {sorted(missing)}")

    return is_subset

def subset_check_reverse(set_1, set_2):
    """
    ПЕРЕВІРКА ПІДМНОЖИНИ (обернений порядок).
    Чи є set_2 підмножиною set_1?
    """
    print("\n" + "="*70)
    print("ПЕРЕВІРКА 2: ЧИ Є set_2 ПІДМНОЖИНОЮ set_1?")
    print("="*70)

    is_subset = set_2 <= set_1

    print(f"\nОперація: set_2 <= set_1")
    print(f"set_2 = {sorted(set_2)}")
    print(f"set_1 = {sorted(set_1)}")
    print(f"\nРезультат: {is_subset}")

    if is_subset:
        print("Висновок: Усі елементи set_2 присутні в set_1")
    else:
        print("Висновок: Не всі елементи set_2 присутні в set_1")
        missing = set_2 - set_1
        print(f"Елементи в set_2, яких немає в set_1: {sorted(missing)}")

    return is_subset

def proper_subset_check(set_1, set_2):
    """
    ПЕРЕВІРКА СТРОГОЇ ПІДМНОЖИНИ.
    Чи є set_1 строгою підмножиною set_2?
    (підмножина, але не дорівнює)
    """
    print("\n" + "="*70)
    print("ПЕРЕВІРКА 3: ЧИ Є set_1 СТРОГОЮ ПІДМНОЖИНОЮ set_2?")
    print("="*70)

    is_proper_subset = set_1 < set_2

    print(f"\nОперація: set_1 < set_2")
    print(f"set_1 = {sorted(set_1)}")
    print(f"set_2 = {sorted(set_2)}")
    print(f"\nРезультат: {is_proper_subset}")

    if is_proper_subset:
        print("Висновок: set_1 є строгою підмножиною set_2")
        print("          (усі елементи set_1 в set_2, але вони не дорівнюють)")
    else:
        print("Висновок: set_1 НЕ є строгою підмножиною set_2")

    return is_proper_subset

def create_frozenset_example():
    """
    Демонстрація frozenset - іммутабельної множини.
    Корисна як ключ у словнику або елемент іншої множини.
    """
    print("\n" + "="*70)
    print("FROST МНОЖИНА (Frozenset) - Іммутабельна множина")
    print("="*70)

    fs_1 = frozenset(["A", "B", "C"])
    fs_2 = frozenset(["B", "C", "D"])

    print("\nFrozenset - іммутабельна множина (не можна змінювати)")
    print(f"  fs_1 = frozenset({sorted(fs_1)})")
    print(f"  fs_2 = frozenset({sorted(fs_2)})")

    print("\nОперації над frozenset (як з звичайною множиною):")
    intersection = fs_1 & fs_2
    print(f"  fs_1 & fs_2 = {sorted(intersection)}")

    print("\nПереваги frozenset:")
    print("  1. Можна використовувати як ключ у словнику")
    print("  2. Можна використовувати як елемент іншої множини")
    print("  3. Гарантія, що значення не змінится")

    dict_with_frozenset = {
        fs_1: "Це frozenset як ключ",
        fs_2: "Іший frozenset як ключ"
    }
    print(f"\nЗастосування як ключі у словнику:")
    for key, value in dict_with_frozenset.items():
        print(f"  {sorted(key)}: {value}")

    return fs_1, fs_2

def compare_set_vs_list():
    """
    Порівняння множини та списку.
    Показує переваги множини для роботи з унікальностю
    та перевірки належності.
    """
    print("\n" + "="*70)
    print("ПОРІВНЯННЯ: Множина vs Список")
    print("="*70)

    items = ["A", "B", "C", "D", "A", "B", "E", "F", "C", "A"]

    print(f"\nВхідна колекція (з повторами): {items}")

    print("\n--- ОПЕРАЦІЯ 1: Отримання унікальних елементів ---")
    print("\nСписок:")
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    print(f"  Код: if item not in unique_list:")
    print(f"       unique_list.append(item)")
    print(f"  Результат: {unique_list}")
    print(f"  Складність: O(n²) - для кожного елемента перевірка по всьому списку")

    print("\nМножина:")
    unique_set = set(items)
    print(f"  Код: unique_set = set(items)")
    print(f"  Результат: {sorted(unique_set)}")
    print(f"  Складність: O(n) - пряма операція перетворення")

    print("\n--- ОПЕРАЦІЯ 2: Перевірка належності ---")
    print("\nСписок:")
    search_item = "D"
    print(f"  Код: if '{search_item}' in unique_list:")
    print(f"  Складність: O(n) - може потребувати перегляду всього списку")

    print("\nМножина:")
    print(f"  Код: if '{search_item}' in unique_set:")
    print(f"  Складність: O(1) - середня, хеш-таблиця")
    print(f"  Результат: {search_item in unique_set}")

    print("\n--- ОПЕРАЦІЯ 3: Множинні операції ---")
    list_a = ["A", "B", "C"]
    list_b = ["B", "C", "D"]

    print("\nПеретин (список):")
    intersection_list = [x for x in list_a if x in list_b]
    print(f"  Код: [x for x in list_a if x in list_b]")
    print(f"  Результат: {intersection_list}")
    print(f"  Складність: O(n*m)")

    print("\nПеретин (множина):")
    intersection_set = set(list_a) & set(list_b)
    print(f"  Код: set(list_a) & set(list_b)")
    print(f"  Результат: {sorted(intersection_set)}")
    print(f"  Складність: O(n+m)")

    print("\nВИСНОВОК:")
    print("  Множина переважніша коли:")
    print("    - Важливо зберегти УНІКАЛЬНІСТЬ елементів")
    print("    - Часто виконуються перевірки належності")
    print("    - Потрібні операції: об'єднання, перетин, різниця")
    print("    - Потрібна краща продуктивність (O(1) vs O(n))")

def main():
    """Головна програма."""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦІЯ ОПЕРАЦІЙ НА МНОЖИНАМИ")
    print("="*70)

    collection_1, collection_2 = load_collections()
    set_1, set_2 = build_sets(collection_1, collection_2)

    intersection = intersection_operation(set_1, set_2)
    union = union_operation(set_1, set_2)
    difference = difference_operation(set_1, set_2)
    sym_diff = symmetric_difference_operation(set_1, set_2)

    is_subset_1_2 = subset_check(set_1, set_2)
    is_subset_2_1 = subset_check_reverse(set_1, set_2)
    is_proper_subset = proper_subset_check(set_1, set_2)

    fs_1, fs_2 = create_frozenset_example()

    compare_set_vs_list()

    print("\n" + "="*70)
    print("ПІДСУМУВАННЯ")
    print("="*70)

    print("\nВиконані операції:")
    print(f"  1. Перетин:               {len(intersection)} елементів")
    print(f"  2. Об'єднання:            {len(union)} елементів")
    print(f"  3. Різниця (1-2):         {len(difference)} елементів")
    print(f"  4. Симетрична різниця:    {len(sym_diff)} елементів")

    print("\nПеревірки підмножини:")
    print(f"  set_1 <= set_2: {is_subset_1_2}")
    print(f"  set_2 <= set_1: {is_subset_2_1}")
    print(f"  set_1 < set_2:  {is_proper_subset}")

    print("\n" + "="*70)
    print("Програма завершена.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
