import argparse
import csv
from tabulate import tabulate

# Импортируем модуль с отчетами
import reports


def read_csv_files(files):
    """Чтение и объединение данных из CSV файлов."""
    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data


def main():
    parser = argparse.ArgumentParser(description='Generate student reports.')
    parser.add_argument('--files', nargs='+', required=True, help='CSV files to process')
    parser.add_argument('--report', required=True, help='Report type to generate')

    args = parser.parse_args()
    data = read_csv_files(args.files)
    if args.report not in reports.REPORTS:
        print(f"Error: Report '{args.report}' is not implemented.")
        return
    report_function = reports.REPORTS[args.report]
    headers, report_data = report_function(data)
    print(tabulate(report_data, headers=headers, tablefmt='grid'))


if __name__ == '__main__':
    main()
