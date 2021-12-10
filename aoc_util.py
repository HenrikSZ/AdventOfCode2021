import os
from typing import Callable
import requests
import pyperclip


def download_data_set(day:int) -> list[str]:
    input_data = ""

    with    open("session_cookie.txt") as session_file, \
            open(f"data_day{day}.txt", "w") as data_file:
        url = f"https://adventofcode.com/2021/day/{day}/input"
        session_cookie = session_file.readline()
        cookies = { "session": session_cookie }

        response = requests.get(url, cookies=cookies)
        input_data = response.content.decode("ascii")[:-1]
        data_file.write(input_data)

    return input_data.split("\n")


def get_data_set(day: int) -> list[str]:
    ret = []
    data_file_path = f"./data_day{day}.txt"
    if os.path.isfile(data_file_path):
        with open(data_file_path) as data_file:
            ret = data_file.read().split("\n")
    else:
        ret = download_data_set(day)

    return ret


def run_with_data_set(fun: Callable, day: int):
    data_set = get_data_set(day)

    run(fun, data_set)


def run_with_data_str(fun: Callable, data_str: str):
    data_set = data_str.split("\n")

    run(fun, data_set)


def run(fun: Callable, data_set: list[str]):
    result = fun(data_set)

    print(result)
    pyperclip.copy(result)
