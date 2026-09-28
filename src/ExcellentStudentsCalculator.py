# -*- coding: utf-8 -*-
from Types import DataType


class ExcellentStudentsCalculator:
    EXCELLENT_THRESHOLD = 90

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0
        for student in self.data:
            scores = [score for _, score in self.data[student]]
            if scores and all(
                s >= self.EXCELLENT_THRESHOLD for s in scores
            ):
                count += 1
        return count
