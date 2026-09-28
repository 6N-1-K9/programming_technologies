# -*- coding: utf-8 -*-
import pytest

from src.main import get_path_from_arguments, get_reader
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


class TestMain:
    def test_get_path_from_arguments(self) -> None:
        path = get_path_from_arguments(["-p", "data/data.txt"])
        assert path == "data/data.txt"

    def test_missing_argument(self) -> None:
        with pytest.raises(SystemExit):
            get_path_from_arguments([])

    def test_get_reader_txt(self) -> None:
        assert isinstance(get_reader("data/data.txt"), TextDataReader)

    def test_get_reader_yaml(self) -> None:
        assert isinstance(get_reader("data/data.yaml"), YamlDataReader)
