import pytest
from reports import students_performance


def test_students_performance():
    # Тестирование с нормальной data
    test_data = [
        {'student_name': 'Иванов Алексей', 'grade': '5'},
        {'student_name': 'Петрова Мария', 'grade': '4'},
        {'student_name': 'Иванов Алексей', 'grade': '4'}
    ]

    headers, result = students_performance(test_data)

    assert headers == ['№', 'student_name', 'grade']
    assert len(result) == 2
    assert result[0][1] == 'Иванов Алексей'
    assert result[0][2] == 4.5  # (5+4)/2 = 4.5
    assert result[1][1] == 'Петрова Мария'
    assert result[1][2] == 4.0


# С пустой data
def test_students_performance_empty_data():
    headers, result = students_performance([])
    assert headers == ['№', 'student_name', 'grade']
    assert result == []


# С одной строкой в data
def test_students_performance_single_student():
    test_data = [{'student_name': 'Иванов Алексей', 'grade': '5'}]
    headers, result = students_performance(test_data)
    assert len(result) == 1
    assert result[0] == [1, 'Иванов Алексей', 5.0]
