#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys
from infoPack import *


def main():
    """
    Главная функция программы.
    """
    # Список личностей.
    persons = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command:
            case 'exit':
                break

            case 'add':
                # Запросить данные о работнике.

                person = get_person_module.get_person()

                # Добавить словарь в список.
                persons.append(person)

                # Отсортировать список в случае необходимости.
                if len(persons) > 1:
                    persons.sort(key=lambda item: item.get('zodiac_sign', ''))

            case 'list':
                # Отобразить всех личностей.
                display_persons_module.display_persons(persons)

            case 'select':
                # Разбить команду на части для выделения месяца.
                parts = command.split(' ', maxsplit=1)

                # Получить требуемый месяц.
                month = int(parts[1])

                # Выбрать личностей с заданным месяцем.
                selected = select_persons_module.select_persons(persons, month)

                # Отобразить выбранных личностей.
                display_persons.display_persons(selected)

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить личность;")
                print("list - вывести список личностей;")
                print("select <месяц> - запросить личностей с этим месяцем;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()