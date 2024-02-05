#!/usr/bin/env python3
# -*- coding: utf-8 -*

def select_persons(staff, period):
    """
    Выбрать личностей с заданным месяцем.
    """
    # Инициализировать счетчик.
    count = 0

    # Сформировать список личностей.
    result = []

    # Проверить сведения личностей из списка.
    for person in staff:
        if period == int(person.get("birth_date").split('.')[1]):
            result.append(person)

    # Возвратить список выбранных личностей.
    return result
