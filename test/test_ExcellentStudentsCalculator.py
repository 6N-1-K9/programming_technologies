# -*- coding: utf-8 -*-
from src.Types import DataType
from src.ExcellentStudentsCalculator import (
    ExcellentStudentsCalculator,
)


class TestExcellentStudentsCalculator:
    def test_two_excellent(self) -> None:
        data: DataType = {
            "Сидоров Иван Петрович": [
                ("математика", 95),
                ("химия", 92),
                ("литература", 90),
            ],
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("химия", 95),
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("химия", 100),
                ("социология", 99),
            ],
        }
        calc = ExcellentStudentsCalculator(data)
        assert calc.calc() == 2

    def test_empty(self) -> None:
        calc = ExcellentStudentsCalculator({})
        assert calc.calc() == 0

    def test_all_excellent(self) -> None:
        data: DataType = {
            "A": [("math", 90), ("phys", 95)],
            "B": [("math", 100)],
        }
        calc = ExcellentStudentsCalculator(data)
        assert calc.calc() == 2

    def test_none_excellent(self) -> None:
        data: DataType = {
            "A": [("math", 89), ("phys", 95)],
            "B": [("math", 50)],
        }
        calc = ExcellentStudentsCalculator(data)
        assert calc.calc() == 0

    def test_boundary_90(self) -> None:
        data: DataType = {
            "A": [("math", 90)],
            "B": [("math", 89)],
        }
        calc = ExcellentStudentsCalculator(data)
        assert calc.calc() == 1
