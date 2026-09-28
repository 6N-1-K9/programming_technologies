# -*- coding: utf-8 -*-
import yaml

from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        self.students = {}
        with open(path, encoding='utf-8') as file:
            data = yaml.safe_load(file)
        if not data:
            return self.students
        for name, subjects in data.items():
            self.students[name] = [
                (subj, int(score))
                for subj, score in subjects.items()
            ]
        return self.students
