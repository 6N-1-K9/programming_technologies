# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from ExcellentStudentsCalculator import ExcellentStudentsCalculator
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True,
        help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def get_reader(path: str):
    if path.endswith(".yaml") or path.endswith(".yml"):
        return YamlDataReader()
    return TextDataReader()


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_reader(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    excellent = ExcellentStudentsCalculator(students).calc()
    print("Excellent students count: ", excellent)


if __name__ == "__main__":
    main()
