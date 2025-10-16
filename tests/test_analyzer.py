from pathlib import Path

import pytest

from brand_analyzer import read_csv
from brand_analyzer.analyzer import Report, RatingReport

DATA_DIR = Path(__file__).parent.parent / "data"


# Test base class Report
def test_generate_error():
    with pytest.raises(NotImplementedError):
        Report.generate([])


def test_display_error():
    with pytest.raises(NotImplementedError):
        Report.display([])


# Test RatingReport
def test_generate_average_rating():
    items = read_csv([DATA_DIR / "test_data_1.csv"])
    res = RatingReport.generate(items)

    assert res[0][0] == "Samsung"
    assert res[0][1] == 4.8
    assert res[1][0] == "Apple"
    assert res[1][1] == 4.55


def test_generate_with_invalid_ratings():
    items = read_csv([DATA_DIR / "test_data_invalid.csv"])
    res = RatingReport.generate(items)

    assert len(res) == 1
    assert res[0][0] == "Samsung"
    assert res[0][1] == 4.8
