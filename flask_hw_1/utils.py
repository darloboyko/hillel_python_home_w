import string
import random
import csv
from faker import Faker
fake = Faker()


def open_arequirements_file():
    return open('requirements.txt', 'r')


def generate_mail(mail_length: int = 8):
    chars = string.ascii_lowercase + string.digits
    mail = ''

    for _ in range(mail_length):
        mail += random.choice(chars)
    return mail


def calculation_the_average_value_from_csv(number_row):
    with open('hw (2) (1).csv', newline='') as File:
        reader = csv.reader(File, delimiter=",")
        middle_value_row = []
        line_count = 0
        for row in reader:
            i = len(row)
            if i <= 1:
                pass
            elif line_count > 0:
                middle_value_row.append(float(row[number_row]))
            line_count += 1
        return sum(middle_value_row) / (line_count-2)


def converter_inches_to_cm(number_row):
    return calculation_the_average_value_from_csv(number_row) * 2.54


def converter_pounds_to_kg(number_row):
    return calculation_the_average_value_from_csv(number_row) * 0.4535923745