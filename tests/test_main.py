import pytest
import tempfile
import csv
import os
from unittest.mock import patch, mock_open
from main import read_csv_files, main


def test_read_csv_files():
    csv_content = """student_name,subject,teacher_name,date,grade
Иванов Алексей,Математика,Петрова Ольга,2023-09-10,5
Петрова Мария,Физика,Сидоров Иван,2023-09-12,4"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f:
        f.write(csv_content)
        temp_path = f.name

    try:
        data = read_csv_files([temp_path])

        assert len(data) == 2
        assert data[0]['student_name'] == 'Иванов Алексей'
        assert data[0]['grade'] == '5'
        assert data[1]['student_name'] == 'Петрова Мария'
        assert data[1]['grade'] == '4'
    finally:
        os.unlink(temp_path)


@patch('main.print')
@patch('main.tabulate')
@patch('main.reports.REPORTS', {'students-performance': lambda x: (['h1', 'h2'], [['data1', 'data2']])})
@patch('main.read_csv_files')
def test_main_success(mock_read, mock_tabulate, mock_print):
    with patch('sys.argv', ['main.py', '--files', 'test.csv', '--report', 'students-performance']):
        mock_read.return_value = [{'test': 'data'}]
        mock_tabulate.return_value = 'mocked table'

        main()

        mock_read.assert_called_once_with(['test.csv'])
        mock_tabulate.assert_called_once_with([['data1', 'data2']], headers=['h1', 'h2'], tablefmt='grid')
        mock_print.assert_called_once_with('mocked table')


@patch('sys.argv', ['main.py', '--files', 'test.csv', '--report', 'invalid-report'])
@patch('main.print')
@patch('main.read_csv_files')
def test_main_invalid_report(mock_read, mock_print):
    mock_read.return_value = []

    main()

    mock_read.assert_called_once_with(['test.csv'])
    mock_print.assert_called_once_with("Error: Report 'invalid-report' is not implemented.")
