# Main logic
from collections import defaultdict
from typing import Tuple, List, Dict
from tabulate import tabulate


class Report:
    """Базовый класс для отчетов"""
    name = "base"

    @classmethod
    def generate(cls, items: List[Dict[str, str]]) -> List[Tuple[str, float]]:
        """
        Метод для генерации данных для отчета
        """
        raise NotImplementedError

    @classmethod
    def display(cls, rows: List[Tuple[str, float]]) -> None:
        """
        Метод для отображения таблицы данных отчета
        """
        raise NotImplementedError


class RatingReport(Report):
    """
    Класс формирующий отчет "average-rating"

    Attributes:
        name(str): Флаг для формирования таблицы

    Методы:
        generate(items): возвращает список пар (бренд и его средний рейтинг)
        display(rows): выводит таблицу со значениями
    """
    name = "average-rating"

    @classmethod
    def generate(cls, items: List[Dict[str, str]]) -> List[Tuple[str, float]]:
        """
        Метод находит средний рейтинг для каждого бренда


        :param items: Список словарей данных бренда
        :return: Возвращает список пар (бренд и его средний рейтинг)
        """
        sums = defaultdict(float)
        counts = defaultdict(int)

        for it in items:
            brand = it.get('brand')
            rating = it.get('rating')

            # Фильтр, который пропускает пустые строки с названием бренда или рейтингом
            if not brand or rating is None:
                # print(f"Пустое поле rating = '{rating}', brand = {brand}")
                continue

            try:
                r = float(rating)
            except (TypeError, ValueError):
                # print(f"Ошибка '{rating}' для {brand}")
                continue

            key = brand.lower().strip()
            sums[key] += r
            counts[key] += 1

        result: List[Tuple[str, float]] = [(i.title(), round(sums[i] / counts[i], 2)) for i in sums]
        result.sort(key=lambda t: t[1], reverse=True)

        return result

    @classmethod
    def display(cls, rows: List[Tuple[str, float]]) -> None:
        """
        Метод для отображения таблицы данных отчета

        :param rows: Список пар (бренд и его средний рейтинг)
        """
        if not rows:
            raise ValueError(f"No data to generate report '{cls.name}'")

        headers = ["brand", "rating"]
        print(tabulate(rows, headers=headers, showindex=range(1, len(rows) + 1), tablefmt="psql"))


# Словарь для работы с --report
REPORTS = {
    "average-rating": RatingReport,
}
