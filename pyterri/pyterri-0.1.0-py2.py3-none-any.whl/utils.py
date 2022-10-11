import requests

problems = list()

def requestClanData():
    response = requests.get("https://territorial.io/clans").text
    response = response.splitlines()

    for i in range(4): del response[0]

    return response

def resetProblems():
    global problems
    problems = list()

    return problems

def addProblem(problem):
    global problems
    problems.append(problem)

    return problems