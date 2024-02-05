#!/usr/bin/env python3
# -*- coding: utf-8 -*

def display_persons(staff):
    """
    Отобразить список линостей.
    """
    # Проверить, что список личностей не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 13
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^13} |'.format(
                "№",
                "Имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех личностях.
        for idx, person in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<13} |'.format(
                    idx,
                    person.get('name', ''),
                    person.get('zodiac_sign', ''),
                    person.get('birth_date', 0)
                )
            )
        print(line)

    else:
        print("Список личностей пуст.")

