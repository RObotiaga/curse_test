import json
from datetime import datetime


def get_data():
    """
        Функция get_data() считывает данные из файла operations.json.

        Returns:
            list: Список данных операций.
    """
    with open(os.path.join(os.path.dirname(os.path.abspath(file)), 'operations.json'), 'r') as file:
        return json.load(file)


def normalize_card(card):
    """
        Функция normalize_card(card) нормализует номер карты.

        Args:
            card (str): Номер карты.

        Returns:
            str: Нормализованный номер карты.
    """
    card_list = card.split(' ')
    if 'Visa' in card_list:
        card_list = [' '.join(card_list[:2]), card_list[2]]
    secret_card = card_list[1][0:4] + ' ' + card_list[1][4:6] + '** **** ' + card_list[1][12:17]
    return f'{card_list[0]} {secret_card}'


def normalize_check(check):
    """
        Функция normalize_check(check) нормализует номер счета.

        Args:
            check (str): Номер счета.

        Returns:
            str: Нормализованный номер счета.
    """
    check_list = check.split(' ')
    recipient_check = ' **' + check_list[1][-4:]
    return f'{check_list[0]}{recipient_check}'


def sort_by_data():
    """
        Функция sort_by_data() сортирует данные операций по дате и возвращает отсортированный список.

        Returns:
            list: Отсортированный список данных операций.
    """
    data = get_data()
    accepted_list = []
    for i in data:
        if i and i['state'] == 'EXECUTED':
            accepted_list.append(i)

    sorted_data = sorted(accepted_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    return sorted_data[::-1]
