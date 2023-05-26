from functions import sort_by_data, normalize_check, normalize_card
from datetime import datetime

for data in sort_by_data()[:4]:
    normal_date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f')
    formatted_date = normal_date.strftime('%d.%m.%Y')
    print(f"{formatted_date} {data['description']}")

    from_to_str = []
    try:
        from_value = normalize_check(data['from']) if 'Счет' in data['from'] else normalize_card(data['from'])
    except:
        from_value = 'Мы'

    to_value = normalize_check(data['to']) if 'Счет' in data['to'] else normalize_card(data['to'])

    print(f"{from_value} => {to_value}")
    print(f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}\n")
