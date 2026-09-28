# -*- coding: utf-8 -*-
from src.Types import DataType
from src.TextDataReader import TextDataReader


class TestTextDataReader:
    def test_read(self, tmp_path) -> None:
        text = (
            "Иванов Константин Дмитриевич\n"
            " математика:91\n"
            " химия:100\n"
            "Петров Петр Семенович\n"
            " математика:76\n"
            " литература:80\n"
        )
        expected: DataType = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91),
                ("химия", 100),
            ],
            "Петров Петр Семенович": [
                ("математика", 76),
                ("литература", 80),
            ],
        }
        file = tmp_path / "data.txt"
        file.write_text(text, encoding="utf-8")
        reader = TextDataReader()
        result = reader.read(str(file))
        assert result == expected

    def test_read_empty(self, tmp_path) -> None:
        file = tmp_path / "empty.txt"
        file.write_text("", encoding="utf-8")
        reader = TextDataReader()
        result = reader.read(str(file))
        assert result == {}
