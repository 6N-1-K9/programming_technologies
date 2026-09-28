# -*- coding: utf-8 -*-
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:
    def test_read(self, tmp_path) -> None:
        text = (
            "Иванов Иван Иванович:\n"
            "  математика: 67\n"
            "  литература: 100\n"
            "  программирование: 91\n"
            "Петров Петр Петрович:\n"
            "  математика: 78\n"
            "  химия: 87\n"
            "  социология: 61\n"
        )
        expected: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91),
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61),
            ],
        }
        file = tmp_path / "data.yaml"
        file.write_text(text, encoding="utf-8")
        reader = YamlDataReader()
        result = reader.read(str(file))
        assert result == expected

    def test_read_empty(self, tmp_path) -> None:
        file = tmp_path / "empty.yaml"
        file.write_text("", encoding="utf-8")
        reader = YamlDataReader()
        result = reader.read(str(file))
        assert result == {}
