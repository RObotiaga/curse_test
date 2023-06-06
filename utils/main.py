from functions import sort_by_data, format_date, get_normalized_value

for data in sort_by_data()[:4]:
    formatted_date = format_date(data['date'])
    print(f"{formatted_date} {data['description']}")

    try:
        from_value = get_normalized_value(data['from'])
    except:
        from_value = 'Мы'

    to_value = get_normalized_value(data['to'])

    print(f"{from_value} => {to_value}")
    print(f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}\n")