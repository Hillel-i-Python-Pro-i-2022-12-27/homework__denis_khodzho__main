from flask import Flask
from faker import Faker
import requests as requests
import aiohttp as aiohttp
import csv

app = Flask(__name__)
file = "tasks/files/people_data(extended).csv"


@app.route("/")
def start():  # put application's code here
    text = "вбейте путь /task_1-4 и будет счастье"
    return text


@app.route("/task_1")
# def hello_world():  # put application's code here
#     return file
def fist_task_file_reader() -> object:
    csv = open(file=file)
    return csv.name


@app.route("/task_2")
def second_task_users_generator(len_users=100):
    fake = Faker()
    last_names = [fake.unique.last_name() for i in range(len_users)]
    mails = [f"{last_name}@mail.com" for last_name in last_names]
    return mails


@app.route("/task_3")
def third_task_what(detail=False):
    url = "http://api.open-notify.org/astros.json"
    # try:
    #     third_task_what_async(url)
    # except:
    #     pass
    try:
        res = requests.get(url)
        res_json = res.json()
        count = res_json["number"]
        peoples = res_json["people"]

        if detail is False:
            return str(count)
        else:
            text = f"Сейчас не на земле {count} человек:"
            people_name = []
            for people in peoples:
                people_name.append(people["name"])
                return f"{text} \n {people_name}"
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry, or continue in a retry loop
        return e
    except requests.exceptions.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        return e
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)


async def third_task_what_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)


@app.route("/task_4")
def last_task_reader():
    with open(file, newline="") as csvfile:
        csv_file = csv.reader(csvfile, delimiter=",")
        table = []
        for row in csv_file:
            table.append(row)
        weght = 0
        for item in table:
            if table[0] != item:
                weght = weght + float(item[4])
        return str(weght)


if __name__ == "__main__":
    app.run()
