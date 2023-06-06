from utils import functions

def test_get_data():
    data = functions.get_data()
    assert isinstance(data, list)
    assert len(data) > 0

def test_normalize_card_visa():
    card = "Visa Gold 5999414228426353"
    normalized_card = functions.normalize_card(card)
    assert normalized_card == "Visa Gold 5999 41** **** 6353"

def test_normalize_card_mastercard():
    card = "Mastercard 5123456789012346"
    normalized_card = functions.normalize_card(card)
    assert normalized_card == "Mastercard 5123 45** **** 2346"

def test_normalize_check():
    check = "Счет 72731966109147704472"
    normalized_check = functions.normalize_check(check)
    assert normalized_check == "Счет **4472"

def test_sort_by_data():
    sorted_data = functions.sort_by_data()
    assert isinstance(sorted_data, list)
    assert len(sorted_data) > 0
    assert sorted_data[0]['date'] == '2019-12-08T22:46:21.935582'

