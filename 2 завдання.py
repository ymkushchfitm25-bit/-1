
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Програма для демонстрації роботи з кортежами як записами предметної області.
Предметна область: облік наукових публікацій науковців.

Структура кортежу записа про науковця:
    (author_id: int, name: str, department: str, publications: list, citations: int)

Приклад:
    scientist_record = (1, "Іван Петренко", "Кафедра ІТ", ["AI в освіті", "ML методи"], 45)
"""

def print_separator(title=""):
    """Виводить розділювач для читабельності."""
    if title:
        print(f"\n{'='*80}")
        print(f"  {title}")
        print(f"{'='*80}")
    else:
        print(f"{'-'*80}")

def print_table_header():
    """Виводить заголовок таблиці."""
    print(f"\n{'ID':<5} {'ПІБ':<25} {'Кафедра':<20} {'Праці':<20} {'Цитування':<10}")
    print(f"{'-'*5} {'-'*25} {'-'*20} {'-'*20} {'-'*10}")

def print_scientist_record(record):
    """Виводить один запис про науковця в табличному форматі."""
    author_id, name, department, publications, citations = record
    publications_str = f"[{len(publications)} праць]"
    print(f"{author_id:<5} {name:<25} {department:<20} {publications_str:<20} {citations:<10}")

def load_initial_data():
    """Завантажує початкові дані про науковців (колекція кортежів)."""
    print_separator("КРОК 1: Завантаження даних — Колекція кортежів")

    # Колекція кортежів (записи про науковців)
    # ВАЖЛИВО: publications — це МУТАБЕЛЬНИЙ об'єкт (список) всередині іммутабельного кортежу!
    scientists = [
        (1, "Іван Петренко", "Кафедра ІТ", ["AI в освіті", "ML методи", "Deep Learning"], 45),
        (2, "Марія Коваленко", "Кафедра Математики", ["Теорія графів", "Комбінаторика"], 28),
        (3, "Петро Сидоренко", "Кафедра ІТ", ["Хмарні обчислення", "DevOps", "Kubernetes"], 67),
        (4, "Олена Іванівна", "Кафедра Фізики", ["Квантова механіка"], 12),
        (5, "Андрій Борисович", "Кафедра Математики", ["Числові методи", "Чисельний аналіз", "Оптимізація"], 55),
    ]

    print("Дані завантажені. Структура запису про науковця:")
    print("  (author_id: int, name: str, department: str, publications: list, citations: int)")
    print("\nДемонстрація колекції (таблиця):")
    print_table_header()

    for record in scientists:
        print_scientist_record(record)

    print(f"\nВсього науковців: {len(scientists)}")
    return scientists

def unpack_and_display_single_record(record):
    """
    Функція 1: Розпаковує один кортеж-запис і повертає окремі поля.

    Демонструє розпакування кортежу двома способами:
    1. Розпакування в змінні (tuple unpacking)
    2. Доступ через індексацію
    """
    print_separator("КРОК 2: Функція 1 — Розпакування одного кортежу")

    print("\n--- Спосіб 1: Розпакування в змінні (Tuple Unpacking) ---")
    print("Код: author_id, name, dept, pubs, citations = record")

    author_id, name, dept, pubs, citations = record

    print(f"\nРозпаковані поля:")
    print(f"  author_id    = {author_id} (тип: {type(author_id).__name__})")
    print(f"  name         = '{name}' (тип: {type(name).__name__})")
    print(f"  dept         = '{dept}' (тип: {type(dept).__name__})")
    print(f"  pubs         = {pubs} (тип: {type(pubs).__name__})")
    print(f"  citations    = {citations} (тип: {type(citations).__name__})")

    print("\n--- Спосіб 2: Доступ через індексацію ---")
    print("Код: record[0], record[1], record[2], record[3], record[4]")

    print(f"\nЗначення через індекс:")
    print(f"  record[0] = {record[0]:<15} (author_id)")
    print(f"  record[1] = '{record[1]:<22}' (name)")
    print(f"  record[2] = '{record[2]:<18}' (department)")
    print(f"  record[3] = {record[3]:<15} (publications)")
    print(f"  record[4] = {record[4]:<15} (citations)")

    print("\n⚠  Від'ємна індексація також працює:")
    print(f"  record[-1] = {record[-1]:<15} (останній елемент - citations)")
    print(f"  record[-2] = {record[-2]:<15} (другий з кінця - publications)")

    print("\n💡 ПОЯСНЕННЯ ВИБОРУ СПОСОБУ:")
    print("  • Розпакування: Краще для читаності коду, коли знаємо структуру")
    print("  • Індексація: Корисна для динамічного доступу або невідомої структури")

    return author_id, name, dept, pubs, citations

def calculate_average_citations(scientists_list):
    """
    Функція 2: Приймає список кортежів і обчислює агрегат.

    Обчислює середнє число цитувань по всіх науковцях.
    """
    print_separator("КРОК 3: Функція 2 — Агрегат: Середнє цитування")

    if not scientists_list:
        print("Список науковців пустий!")
        return 0

    # Розпакування та сумування цитувань
    total_citations = sum(record[4] for record in scientists_list)
    avg_citations = total_citations / len(scientists_list)

    print(f"\nОбчислення:")
    print(f"  Всього науковців:     {len(scientists_list)}")
    print(f"  Загальне цитування:   {total_citations} (на всіх)")
    print(f"  Середнє цитування:    {avg_citations:.2f} цит./науковець")

    # Детальна таблиця з деталізацією
    print(f"\nДетальна статистика:")
    print(f"{'ПІБ':<25} {'Цитування':<15} {'Від середнього':<20}")
    print(f"{'-'*25} {'-'*15} {'-'*20}")

    for record in scientists_list:
        name = record[1]
        citations = record[4]
        diff = citations - avg_citations
        sign = "+" if diff > 0 else ""
        print(f"{name:<25} {citations:<15} {sign}{diff:.2f}")

    return avg_citations

def demonstrate_tuple_immutability():
    """
    ДЕМОНСТРАЦІЯ: Спроба присвоєння до кортежу (іммутабельність).

    Показує типову помилку при спробі змінити кортеж.
    """
    print_separator("КРОК 4: Демонстрація — Іммутабельність кортежу (помилка)")

    test_tuple = (1, "Тест", "Кафедра", ["Робота 1"], 10)

    print("\nПопередній кортеж:")
    print(f"  test_tuple = {test_tuple}")

    print("\nСпроба 1: Присвоєння нового значення до індекса")
    print("Код: test_tuple[1] = 'Новое имя'")

    try:
        test_tuple[1] = "Нове ім'я"
        print("✓ Присвоєння успішне (неможливо, це помилка в демонстрації)")
    except TypeError as e:
        print(f"❌ ПОМИЛКА (очікувано): {e}")
        print(f"   Тип помилки: {type(e).__name__}")
        print(f"   Причина: Кортежі dalam Python є ІММУТАБЕЛЬНИМИ (незмінними)")

    print("\nСпроба 2: Видалення елемента")
    print("Код: del test_tuple[0]")

    try:
        del test_tuple[0]
        print("✓ Видалення успішне (неможливо, це помилка)")
    except TypeError as e:
        print(f"❌ ПОМИЛКА (очікувано): {e}")

    print("\nСпроба 3: Додавання нового елемента через присвоєння")
    print("Код: test_tuple[5] = 100")

    try:
        test_tuple[5] = 100
        print("✓ Додавання успішне (неможливо)")
    except (TypeError, IndexError) as e:
        print(f"❌ ПОМИЛКА (очікувано): {e}")
        print(f"   Тип помилки: {type(e).__name__}")

    print("\n✅ ВИСНОВОК: Кортеж залишається абсолютно незмінним!")
    print(f"   Поточне значення: {test_tuple}")

def demonstrate_mutable_nested_object():
    """
    ДЕМОНСТРАЦІЯ: Кортеж містить мутабельний об'єкт (список).

    Показує, що хоча кортеж іммутабельний, його ВМІСТИМЕ елементи
    (якщо це список, словник тощо) можна змінювати!
    """
    print_separator("КРОК 5: Демонстрація — Мутабельні вкладені об'єкти")

    # Кортеж з мутабельним списком
    scientist = (5, "Андрій Борисович", "Кафедра Математики", 
                 ["Числові методи", "Чисельний аналіз", "Оптимізація"], 55)

    print("\nПочатковий кортеж про науковця:")
    print(f"  scientist = ({scientist[0]}, '{scientist[1]}', '{scientist[2]}',")
    print(f"              {scientist[3]}, {scientist[4]})")

    print("\n" + "="*80)
    print("ЧТО ЗАЛИШАЄТЬСЯ НЕЗМІННИМ (іммутабельна структура кортежу):")
    print("="*80)

    print("\n❌ Неможна ЗАМІНИТИ список на інший объект:")
    print("Код: scientist[3] = ['Нова робота']")
    try:
        scientist[3] = ["Нова робота"]
    except TypeError as e:
        print(f"   ПОМИЛКА: {e}")

    print("\n❌ Неможна ВИЛУЧИТИ елемент список:")
    print("Код: del scientist[3]")
    try:
        del scientist[3]
    except TypeError as e:
        print(f"   ПОМИЛКА: {e}")

    print("\n" + "="*80)
    print("ЧТО МОЖНА ЗМІНЮВАТИ (вміст мутабельного вложеного об'єкта):")
    print("="*80)

    print("\n✅ МОЖНА ЗМІНЮВАТИ ВМІСТ СПИСКУ:")
    print("Код: scientist[3].append('Нова робота')")
    scientist[3].append("Нова робота")
    print(f"   Результат: scientist[3] = {scientist[3]}")
    print(f"   ✓ Успішно додана нова робота!")

    print("\n✅ МОЖНА ЗМІНЮВАТИ ЕЛЕМЕНТИ СПИСКУ:")
    print("Код: scientist[3][0] = 'Переиміньована робота'")
    scientist[3][0] = "Перейменована робота"
    print(f"   Результат: scientist[3] = {scientist[3]}")
    print(f"   ✓ Успішно змінено першу роботу!")

    print("\n✅ МОЖНА ВИДАЛИТИ ЕЛЕМЕНТ ЗІ СПИСКУ:")
    print("Код: scientist[3].pop()")
    removed = scientist[3].pop()
    print(f"   Видалено: '{removed}'")
    print(f"   Результат: scientist[3] = {scientist[3]}")

    print("\n✅ МОЖНА ОЧИСТИТИ ВЕСЬ СПИСОК:")
    publications_copy = scientist[3].copy()
    scientist[3].clear()
    print(f"   Код: scientist[3].clear()")
    print(f"   Результат: scientist[3] = {scientist[3]}")
    print(f"   (було: {publications_copy})")

    # Відновимо список для наступних демонстрацій
    scientist[3].extend(publications_copy)

    print("\n" + "="*80)
    print("ПОЯСНЕННЯ ЯВИЩА (Tuple з мутабельним обʼєктом):")
    print("="*80)

    print("""
    📌 ІММУТАБЕЛЬНІСТЬ КОРТЕЖУ:
       • Сам кортеж — це незмінна структура
       • Неможна додити/видалити/замінити МІСЦЕ визначень (слоти)
       • Неможна переєнести елемент на інший индекс

    📌 МУТАБЕЛЬНІСТЬ ВЛОЖЕНОГО ОБ'ЕКА:
       • Якщо елемент кортежу — це список, словник, множина (мутабельні об'єкти)
       • То їхні СОДЕРЖИМОЕ можна змінювати
       • Змінюється сам об'єкт, а не посилання в кортежу
       • Посилання (id об'єкта) залишається тим же!

    📌 АНАЛОГІЯ:
       Кортеж — це скринька з пронумерованими місцями
       • Неможна додати нове місце (іммутабельність)
       • Неможна перемістити місце А на місце Б
       • АЛЕ якщо в місці лежить сумка (список), то можна
        перекласти речі ВСЕРЕДИНІ сумки!
    """)

    # Демонстрація id об'єкта
    print("\n📊 ДЕМОНСТРАЦІЯ id об'ека (адреса в пам'яті):")
    publications_list = scientist[3]
    print(f"   id(scientist[3]) = {id(scientist[3])}")
    print(f"   id(publications_list) = {id(publications_list)}")
    print(f"   Одинаковий id? {id(scientist[3]) == id(publications_list)}")
    print(f"   (id не змінюється, змінюється лише вміст)")

def calculate_publications_per_scientist(scientists_list):
    """
    Додаткова функція: Обчислює агрегат - середню кількість публікацій.
    """
    print_separator("КРОК 6: Додаткова статистика — Публікації")

    total_publications = sum(len(record[3]) for record in scientists_list)
    avg_publications = total_publications / len(scientists_list) if scientists_list else 0

    print(f"\nОбчислення за публікаціями:")
    print(f"  Усього публікацій:          {total_publications}")
    print(f"  Науковців:                  {len(scientists_list)}")
    print(f"  Середньо на науковця:       {avg_publications:.2f} публ./чол.")

    print(f"\nТаблиця детальних даних:")
    print(f"{'ПІБ':<25} {'Публікацій':<15} {'Названя праць':<40}")
    print(f"{'-'*25} {'-'*15} {'-'*40}")

    for record in scientists_list:
        name = record[1]
        publications = record[3]
        pub_count = len(publications)
        pub_titles = ", ".join(publications) if publications else "(немає)"
        print(f"{name:<25} {pub_count:<15} {pub_titles:<40}")

    return avg_publications, total_publications

def print_final_statistics(scientists_list):
    """Виводить фінальну статистику."""
    print_separator("КРОК 7: Фінальна статистика")

    avg_citations = calculate_average_citations(scientists_list)
    avg_publications, total_publications = calculate_publications_per_scientist(scientists_list)

    # Знаходимо науковця з найбільшим числом цитувань
    best_scientist = max(scientists_list, key=lambda x: x[4])
    worst_scientist = min(scientists_list, key=lambda x: x[4])

    print(f"\n📊 УЗАГАЛЬНЕНА СТАТИСТИКА:")
    print(f"  Найцитованіший науковець:  {best_scientist[1]} ({best_scientist[4]} цит.)")
    print(f"  Найменш цитований:          {worst_scientist[1]} ({worst_scientist[4]} цит.)")
    print(f"  Середнє цитування:          {avg_citations:.2f} цит./чол.")
    print(f"  Середнє публікацій:         {avg_publications:.2f} публ./чол.")
    print(f"  Загальна кількість праць:  {total_publications}")

def main():
    """Головна функція програми."""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  ДЕМОНСТРАЦІЯ РОБОТИ З КОРТЕЖАМИ ЯК ЗАПИСАМИ ПРЕДМЕТНОЇ ОБЛАСТІ".center(78) + "║")
    print("║" + "  (Облік наукових публікацій)".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")

    # Крок 1: Завантаження даних
    scientists = load_initial_data()

    # Крок 2: Функція 1 - Розпакування одного кортежу
    unpack_and_display_single_record(scientists[0])

    # Крок 3: Функція 2 - Агрегат (середнє цитування)
    calculate_average_citations(scientists)

    # Крок 4: Демонстрація іммутабельності
    demonstrate_tuple_immutability()

    # Крок 5: Демонстрація мутабельного вкладеного об'єкта
    demonstrate_mutable_nested_object()

    # Крок 6-7: Фінальна статистика
    print_final_statistics(scientists)

    # Фінальний висновок
    print_separator("ВИСНОВОК")
    print("""
  Продемонстровано:

   1. Колекція кортежів як записи предметної області
      (3+ різні кортежі про науковців)

   2. Функція 1: unpack_and_display_single_record()
      - Розпаковує кортеж у змінні
      - Доступ через індекс
      - Пояснення переваг кожного методу

   3. Функція 2: calculate_average_citations()
      - Обчислює агрегат (середнє цитування) по всій колекції
      - Детальна таблиця с деталізацією

   4. Демонстрація ІММУТАБЕЛЬНОСТІ:
      - помилка при спробі присвоєння (test_tuple[i] = ...)
      - помилка при видаленні (del test_tuple[i])
      - Обробка винятку TypeError

   5. Демонстрація мутабельності ВЛОЖЕНОГО об'єкта:
      - Список в кортежі є мутабельним
      - Кортеж залишається незмінним як структура
      - Вміст списку можна змінювати (append, remove, clear)
      - Пояснення через аналогію зі скринькою й сумкою
      - Демонстрація id об'єкта (посилання не змінюється)

   6. Структурований вивід:
      - Таблиці з вирівнюванням
      - Явні одиниці виміру (цит./чол., публ./чол.)
      - Наскидні розділювачи й пояснення

   7. Коректне обчислення агрегату на всій колекції

  Ключові висновки щодо кортежів:
   • Кортежі — послідовності іммутабельних об'єктів
   • Структура кортежу незмінна (немає операцій додавання/видалення)
   • Мутабельні об'єкти всередині кортежу можна змінювати
   • Кортежі часто використовуються для записів БД / структурованих даних
   • Можна розпаковувати в змінні або звертатися по індексу
   • Обов'язкова обробка винятків при спробі модифікації

    """)
    print("\nПрограма завершена успішно!\n")

if __name__ == "__main__":
    main()
