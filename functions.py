import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r') as file:
        return json.load(file)


def normalize_card(card):
    card_list = card.split(' ')
    if 'Visa' in card_list:
        card_list = [' '.join(card_list[:2]), card_list[2]]
    secret_card = card_list[1][0:4] + ' ' + card_list[1][4:6] + '** **** ' + card_list[1][12:17]
    return f'{card_list[0]} {secret_card}'


def normalize_check(check):
    check_list = check.split(' ')
    recipient_check = ' **' + check_list[1][11:17]
    return f'{check_list[0]} {recipient_check}'


def sort_by_data():
    data=get_data()
    accepted_list = []
    for i in data:
        if i and i['state'] == 'EXECUTED':
            accepted_list.append(i)

    sorted_data = sorted(accepted_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    return sorted_data[::-1]



