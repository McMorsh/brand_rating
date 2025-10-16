from pathlib import Path
import pytest

from brand_analyzer.cli import parse_arguments
from brand_analyzer import cli_main

DATA_DIR = Path(__file__).parent.parent / "data"


# Test parse_arguments
def test_parse_arguments():
    parser = parse_arguments().parse_args([
        "--files",
        str(DATA_DIR / "test_data_1.csv"),
        str(DATA_DIR / "test_data_2.csv"),
        "--report",
        "average-rating"
    ])

    assert parser.files == [str(DATA_DIR / "test_data_1.csv"),
                            str(DATA_DIR / "test_data_2.csv")]
    assert parser.report == "average-rating"


def test_parse_arguments_error():
    with pytest.raises(SystemExit):
        parse_arguments().parse_args([
            "--files",
            str(DATA_DIR / "test_data_1.csv"),
            str(DATA_DIR / "test_data_2.csv")
        ])


# Test cli main
def test_cli_main_error_file_not_found(monkeypatch):
    args = [
        "--files",
        str(DATA_DIR / "test_data.csv"),
        "--report",
        "average-rating"
    ]
    monkeypatch.setattr("sys.argv", ["main.py"] + args)

    with pytest.raises(SystemExit) as e:
        cli_main()

    assert e.value.code == 1


def test_cli_main_error_empty_file(monkeypatch):
    args = [
        "--files",
        str(DATA_DIR / "test_data_empty.csv"),
        "--report",
        "average-rating"
    ]
    monkeypatch.setattr("sys.argv", ["main.py"] + args)

    with pytest.raises(SystemExit) as e:
        cli_main()

    assert e.value.code == 3
