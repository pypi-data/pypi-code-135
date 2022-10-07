import requests
import os
import datetime

api_key = os.environ["DONELIST_API_KEY"]


def get_today_filepath():
    '''
    Based on the date format "10-06-22", get the corresponding date object for the current day and assign it to text_filepath
    strftime format is "%-m-%d-%y"
    '''
    today = datetime.date.today()
    return f"/mnt/c/Users/darks/Dropbox/Journal/Notebook/{today.strftime('%-m-%d-%y')}.txt"


text_filepath = get_today_filepath()


def get_tasks(text_filepath):
    # read in text file as a list
    with open(text_filepath, "r") as f:
        lines = f.readlines()
    # loop through list and if "---\n" is found directly after "done\n", print every following value to a new list called tasks, then remove "/n" from each item in tasks
    tasks = []
    for i in range(len(lines)):
        if lines[i] == "done\n" and lines[i + 1] == "---\n":
            tasks.extend(lines[j].replace("\n", "")
                         for j in range(i + 2, len(lines)))
    return tasks


def add_tasks(text_filepath):
    tasks = get_tasks(text_filepath)
    for task in tasks:
        add_done_task(task)


def add_done_task(task):
    r = requests.post(
        f"https://donel.ist/list/api/v1/integration/items?apikey={api_key}",
        json={"text": task})
    print(r.text)


add_tasks(text_filepath)
