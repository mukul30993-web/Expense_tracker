import csv
import os

FILE_NAME = "data.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


def read_data():
    create_file()

    with open(FILE_NAME, "r") as file:
        return list(csv.reader(file))


def write_data(rows):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)