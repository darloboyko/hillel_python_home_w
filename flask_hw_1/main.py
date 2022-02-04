from flask import Flask, request
from faker import Faker
from utils import generate_mail, open_arequirements_file, converter_inches_to_cm, converter_pounds_to_kg
import requests

fake = Faker()

app = Flask(__name__)


@app.route("/requirements/")
def read_requirements_file():
    return str(open_arequirements_file().read())


@app.route("/generate-users/")
def make_fake_name_list():
    fake_name_list = []
    query_params = request.args
    list_length = query_params.get('length')

    default_list_length = 100
    maximum_list_length = 150

    if list_length is None:
        list_length = default_list_length
    elif not list_length.isdigit():
        list_length = default_list_length

    list_length = int(list_length)
    if list_length > maximum_list_length:
        list_length = default_list_length

    for _ in range(100):
        post = (fake.first_name() + ', ' + generate_mail() + '@' + fake.domain_name())
        fake_name_list.append(post)
    return str(fake_name_list)


@app.route("/mean/")
def print_middl_value_from_csv():
    return (f'\t Средний рост = {round(converter_inches_to_cm(1), 2)} см; Средний вес = {round(converter_pounds_to_kg(2), 2)} кг')


@app.route("/space/")
def print_number_people_from_json():
    r = requests.get('http://api.open-notify.org/astros.json')
    return (f'Количество космонавтов в настоящий момент:  {str(r.json()["number"])}')


if __name__ == '__main__':
    app.run(debug=True)