import csv
from pathlib import Path


def create_csv(path, rows):
    with open(path, "w", encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'brand', 'price', 'rating'])
        clean_rows = [row for row in rows if row]
        writer.writerows(clean_rows)


def validate_data(tmp_path):
    path = tmp_path / 'test_data_1.csv'
    rows = [
        ("iphone 15", "apple", 399, 4.9),
        ("ipod", "apple", 150, 4.2),
        ("galaxy S99", "samsung", 1199, 4.8)
    ]
    create_csv(path, rows)

    path = tmp_path / 'test_data_2.csv'
    rows = [
        ("redmi note 12 pro max ultra", "xiaomi", 199, 4.3),
        ("galaxy j7", "samsung", 50, 4.1)
    ]
    create_csv(path, rows)


def empty_data(tmp_path):
    create_csv(tmp_path / 'test_data_empty.csv', [])


def invalid_data(tmp_path):
    path = tmp_path / 'test_data_invalid.csv'
    rows = [
        ("iphone 15", "apple", 399, "bad"),
        ("galaxy S99", "samsung", None, 4.8),
        ("pixel 8", "google", 299, "")
    ]
    create_csv(path, rows)


if __name__ == '__main__':
    validate_data(Path("../data"))
    empty_data(Path("../data"))
    invalid_data(Path("../data"))
