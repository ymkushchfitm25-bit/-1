
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Програма побудови словника частот слів/символів.
Без використання collections.Counter.
"""

import os
import sys
import string

def get_input_source():
    """Вибір джерела введення: клавіатура або файл."""
    print("\n" + "="*70)
    print("ВИБІР ДЖЕРЕЛА ВВЕДЕННЯ")
    print("="*70)
    print("\n1. Введення з клавіатури (до рядка 'END')")
    print("2. Читання з файлу (UTF-8)")

    choice = input("\nОберіть (1 або 2): ").strip()

    if choice == "2":
        filename = input("Введіть ім'я файлу: ").strip()
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    text = f.read()
                print(f"\nФайл '{filename}' успішно прочитаний.")
                return text
            except Exception as e:
                print(f"Помилка при читанні файлу: {e}")
                sys.exit(1)
        else:
            print(f"Файл '{filename}' не знайдено.")
            sys.exit(1)
    else:
        print("\nВводьте текст (введіть 'END' на окремому рядку для завершення):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        text = "\n".join(lines)
        return text

def normalize_text(text, granularity='word'):
    """
    Нормалізація тексту.

    Параметр granularity:
    - 'word': розбір на слова
    - 'char': розбір на символи
    """
    print("\n" + "="*70)
    print("НОРМАЛІЗАЦІЯ ТЕКСТУ")
    print("="*70)

    if granularity == 'word':
        print("\nРівень гранулярності: СЛОВО")
        print("\nПравила нормалізації:")
        print("  1. Перехід до нижнього регістру")
        print("  2. Видалення розділових знаків: . , ! ? ; : \" ' - ( )")
        print("  3. Розбір по пробілам")
        print("  4. Видалення порожніх рядків")

        # Видаляємо розділові знаки
        for punct in ".,!?;:\"'-()\n":
            text = text.replace(punct, " ")

        # Розбиваємо на слова
        tokens = text.lower().split()

        # Видаляємо порожні рядки
        tokens = [token for token in tokens if token]

    else:  # granularity == 'char'
        print("\nРівень гранулярності: СИМВОЛ")
        print("\nПравила нормалізації:")
        print("  1. Перехід до нижнього регістру")
        print("  2. Видалення пробілів та переносів рядків")
        print("  3. Видалення розділових знаків")

        # Видаляємо розділові знаки
        punctuation = string.punctuation + " \n\t"
        text = text.lower()
        tokens = [char for char in text if char not in punctuation]

    print(f"\nКількість токенів: {len(tokens)}")
    return tokens

def build_frequency_dict(tokens):
    """
    Побудова словника частот явним циклом.
    Без використання collections.Counter.
    """
    print("\n" + "="*70)
    print("ПОБУДОВА СЛОВНИКА ЧАСТОТ")
    print("="*70)

    freq_dict = {}

    # Цикл інкременту лічильників
    for token in tokens:
        # Безпечне отримання частоти: get() з дефолтним значенням
        current_count = freq_dict.get(token, 0)
        freq_dict[token] = current_count + 1

    print(f"\nСловник побудований.")
    print(f"Унікальних ключів: {len(freq_dict)}")
    print(f"Всього токенів: {sum(freq_dict.values())}")

    return freq_dict

def filter_by_frequency(freq_dict, min_frequency=2):
    """
    Dict comprehension для фільтрації.
    Повертає словник з частотою не нижче порога.
    """
    print("\n" + "="*70)
    print(f"ФІЛЬТРАЦІЯ: мінімальна частота = {min_frequency}")
    print("="*70)

    # Dict comprehension
    filtered_dict = {key: count for key, count in freq_dict.items() 
                     if count >= min_frequency}

    print(f"\nОригінальних ключів: {len(freq_dict)}")
    print(f"Після фільтрації: {len(filtered_dict)}")
    print(f"Видалено: {len(freq_dict) - len(filtered_dict)}")

    return filtered_dict

def print_sorted_by_key(freq_dict, title="Sorted by Key (Alphabetically)"):
    """Виведення словника, відсортованого за ключем."""
    print("\n" + "="*70)
    print(title)
    print("="*70)

    sorted_items = sorted(freq_dict.items())

    print(f"\n{'Ключ':<30} {'Частота':<10} {'Відсоток':<10}")
    print("-" * 50)

    total = sum(freq_dict.values())

    for key, count in sorted_items:
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{key:<30} {count:<10} {percentage:>6.2f}%")

def print_sorted_by_frequency(freq_dict, title="Sorted by Frequency (Descending)", limit=None):
    """Виведення словника, відсортованого за частотою (спадаючий порядок)."""
    print("\n" + "="*70)
    print(title)
    print("="*70)

    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Обмеження кількості рядків для виведення (опціонально)
    if limit:
        sorted_items = sorted_items[:limit]

    print(f"\n{'Ключ':<30} {'Частота':<10} {'Відсоток':<10}")
    print("-" * 50)

    total = sum(freq_dict.values())

    for key, count in sorted_items:
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{key:<30} {count:<10} {percentage:>6.2f}%")

def save_to_file(freq_dict, filename="frequency_results.txt"):
    """Збереження результатів у файл."""
    print("\n" + "="*70)
    print(f"ЗБЕРЕЖЕННЯ РЕЗУЛЬТАТІВ")
    print("="*70)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("РЕЗУЛЬТАТИ АНАЛІЗУ ЧАСТОТИ\n")
            f.write("="*50 + "\n\n")

            # Сортування за ключем
            f.write("СОРТУВАННЯ ЗА КЛЮЧЕМ (АЛФАВІТНЕ)\n")
            f.write("-"*50 + "\n")
            f.write(f"{'Ключ':<30} {'Частота':<10}\n")
            f.write("-"*50 + "\n")

            sorted_by_key = sorted(freq_dict.items())
            total = sum(freq_dict.values())

            for key, count in sorted_by_key:
                percentage = (count / total * 100) if total > 0 else 0
                f.write(f"{key:<30} {count:<10} ({percentage:>6.2f}%)\n")

            f.write("\n\n")

            # Сортування за частотою
            f.write("СОРТУВАННЯ ЗА ЧАСТОТОЮ (СПАДАЮЧИЙ ПОРЯДОК)\n")
            f.write("-"*50 + "\n")
            f.write(f"{'Ключ':<30} {'Частота':<10}\n")
            f.write("-"*50 + "\n")

            sorted_by_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

            for key, count in sorted_by_freq:
                percentage = (count / total * 100) if total > 0 else 0
                f.write(f"{key:<30} {count:<10} ({percentage:>6.2f}%)\n")

            f.write("\n" + "="*50 + "\n")
            f.write(f"Всього унікальних ключів: {len(freq_dict)}\n")
            f.write(f"Загальна кількість токенів: {total}\n")

        print(f"\nРезультати сохранені у файл '{filename}'")
        return True
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")
        return False

def demonstrate_example():
    """Демонстрація на прикладі."""
    print("\n" + "="*70)
    print("ПРИКЛАД: Невеликий текст")
    print("="*70)

    example_text = "Hello world! Hello Python. Python is great."
    print(f"\nВхідний текст:\n'{example_text}'")

    # Нормалізація
    normalized = example_text.lower()
    for punct in ".,!?;:\"'-()\n":
        normalized = normalized.replace(punct, " ")
    tokens = normalized.split()
    tokens = [t for t in tokens if t]

    print(f"\nТокени: {tokens}")

    # Побудова словника
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1

    print(f"Словник частот: {freq}")

    # Виведення
    print(f"\nВідсортовано за ключем:")
    for key, count in sorted(freq.items()):
        print(f"  {key}: {count}")

    print(f"\nВідсортовано за частотою (спадаючий порядок):")
    for key, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  {key}: {count}")

def main():
    """Головна функція."""
    print("\n" + "="*70)
    print("ПОБУДОВА СЛОВНИКА ЧАСТОТ")
    print("="*70)

    # Демонстрація на прикладі
    demo = input("\nПоказати приклад? (y/n): ").strip().lower()
    if demo == 'y':
        demonstrate_example()
        another = input("\nПродовжити з основною програмою? (y/n): ").strip().lower()
        if another != 'y':
            return

    # Основна програма
    text = get_input_source()

    # Вибір гранулярності
    print("\n" + "="*70)
    print("ВИБІР РІВНЯ ГРАНУЛЯРНОСТІ")
    print("="*70)
    print("\n1. Слова")
    print("2. Символи")

    granularity_choice = input("\nОберіть (1 або 2): ").strip()
    granularity = 'char' if granularity_choice == '2' else 'word'

    # Нормалізація
    tokens = normalize_text(text, granularity)

    # Побудова словника
    freq_dict = build_frequency_dict(tokens)

    # Виведення у відсортованому порядку за ключем
    print_sorted_by_key(freq_dict)

    # Виведення у відсортованому порядку за частотою
    print_sorted_by_frequency(freq_dict, limit=50)

    # Фільтрація через dict comprehension
    min_freq = input("\nУведіть мінімальну частоту для фільтрації (або Enter для пропуску): ").strip()
    if min_freq and min_freq.isdigit():
        min_freq = int(min_freq)
        filtered_dict = filter_by_frequency(freq_dict, min_freq)
        print_sorted_by_frequency(filtered_dict, 
                                 title=f"Top frequencies (minimum: {min_freq})")

    # Збереження результатів
    save_choice = input("\nЗберегти результати у файл? (y/n): ").strip().lower()
    if save_choice == 'y':
        output_file = input("Введіть ім'я файлу (за замовчуванням 'frequency_results.txt'): ").strip()
        if not output_file:
            output_file = "frequency_results.txt"
        save_to_file(freq_dict, output_file)

    print("\n" + "="*70)
    print("Програма завершена.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
