#!/usr/bin/env python3
# -*- coding: utf-8 -*

def get_person():
    """
    Запросить данные о личносте.
    """
    # Запросить данные о личности.
    name = input("Фамилия и имя? ")
    zodiac_sign = input("Знак Зодиака? ")
    birth_date = input("Дата рождения? ")

    # Создать словарь.
    return {
        'name': name,
        'zodiac_sign': zodiac_sign,
        'birth_date': birth_date
    }