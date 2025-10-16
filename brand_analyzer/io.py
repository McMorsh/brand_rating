# Input/Output
import csv
from pathlib import Path


def read_csv(file_paths):
    """
    Функция для чтения csv файлов

    :param file_paths: Список путей для csv файлов
    :return: Список данных
    :raise: FileNotFoundError: Если любой файл не найден
    """
    all_data = []

    for fp in file_paths:
        path = Path(fp)

        if not path.exists():
            raise FileNotFoundError(f"File {fp} does not exist")

        with path.open(encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            all_data.extend(csv_reader)

    return all_data
