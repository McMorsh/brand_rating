import pytest
from pathlib import Path
from brand_analyzer import read_csv

DATA_DIR = Path(__file__).parent.parent / "data"


def test_read_valid_csv():
    csv_file = DATA_DIR / "test_data_1.csv"
    data = read_csv([csv_file])
    assert len(data) == 3
    assert data[0]["brand"] == "apple"
    assert data[1]["rating"] == "4.2"


def test_read_missing_csv(tmp_path):
    missing_file = DATA_DIR / "missing.csv"
    with pytest.raises(FileNotFoundError):
        read_csv([missing_file])


def test_read_empty_csv(tmp_path):
    empty_file = DATA_DIR / "test_data_empty.csv"
    data = read_csv([empty_file])
    assert data == []
