#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import packetFunction


if __name__ == "__main__":
    string_to_transform = input("Введите строку с "
                                "повторяющимися символами: ")

    said_char = input("Введите символ: ")

    replacement_func = packetFunction.replace_duplicates(said_char)
    transformed_string = replacement_func(string_to_transform)

    print(f"Исправленная строка: {transformed_string}")


