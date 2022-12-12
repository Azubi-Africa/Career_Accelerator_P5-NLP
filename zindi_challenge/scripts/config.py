# -*- coding: utf-8 -*-
"""
    Contains all necessary paths and other usefull constants
"""

from os.path import abspath, dirname, join, exists

ROOT_PATH = dirname(dirname(abspath(__file__)))

DATA_PATH = join(ROOT_PATH, "data")
MODEL_PATH = join(ROOT_PATH, "models")

INPUT_CSV = join(DATA_PATH, "Train.csv")
OUTPUT_CSV = join(DATA_PATH, "Test.csv")

if __name__ == "__main__":
    # print(f" {None}")
    print(f"DATA_PATH: {DATA_PATH}\nexists?: {exists(DATA_PATH)}")
    print(f"INPUT_CSV: {INPUT_CSV}\nexists?: {exists(INPUT_CSV)}")