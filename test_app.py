from app import calculate_total, divide, process_data


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_divide():
    assert divide(10, 2) == 5


def test_process_data():
    assert process_data([1, None, 2, "", 3]) == [1, 2, 3]