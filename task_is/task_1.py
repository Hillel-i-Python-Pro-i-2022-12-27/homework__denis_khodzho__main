import csv

import aiohttp as aiohttp
import requests as requests
from faker import Faker


def fist_task_file_reader(file) -> object:
    csv = open(file=file, mode="r")
    return csv

def second_task_users_generator(len_users=100):
    fake = Faker()
    last_names = [fake.unique.last_name() for i in range(len_users)]
    mails = [f"{last_name}@mail.com" for last_name in last_names]
    print(len(mails), mails)

def third_task_what(detail=False):
    url = "http://api.open-notify.org/astros.json"
    try:
        third_task_what_async(url)
    except:
        pass
    try:
        res = requests.get(url)
        res_json = res.json()
        count = res_json['number']
        peoples = res_json['people']

        if detail == False:
            print(count)
        else:
            print(f"Сейчас не на земле {count} человек:")
            for people in peoples:
                print(people['name'])
    except:
        pass

async def third_task_what_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)


def last_task_reader(file):
    with open(file, newline='') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',')
        table = []
        for row in csv_file:
            table.append(row)
        weght = 0
        for item in table:
            try:
                weght = weght + float(item[4])
            except:
                continue
        print(weght)
