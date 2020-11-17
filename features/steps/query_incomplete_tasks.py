from behave import *
import requests
import json

@given('there is a course with associated tasks')
def step_impl(context):
    url = f'http://localhost:4567/categories/3/todos'
    response = requests.get(url)
    if (not response.ok):
        raise Exception("category does not exist")
    if (not response.json()["todos"]):
        raise Exception("no tasks linked to this category")

@when('the user queries for all associated tasks with doneStatus = false')
def step_impl(context):
    url = f'http://localhost:4567/categories/3/todos?doneStatus=false'
    context.response = requests.get(url)

@then('the returned subset of tasks associated to the course will exclude those having already been completed')
def step_impl(context):
    todos = context.response.json()["todos"]
    for i in todos:
        if i["id"] != '3' and i["id"] != '5':
            assert False
    assert len(todos) == 2

@given('there are tasks in the system')
def step_impl(context):
    url = f'http://localhost:4567/todos'
    response = requests.get(url)
    if (not response.json()["todos"]):
        raise Exception("no tasks present")

@when('the user queries for all tasks with doneStatus = false')
def step_impl(context):
    url = f'http://localhost:4567/todos?doneStatus=false'
    context.response = requests.get(url)

@then('the returned subset of tasks will be all those with a false doneStatus')
def step_impl(context):
    todos = context.response.json()["todos"]
    assert len(todos) == 5

@when('the user queries for all tasks with doneStatus = {param}')
def step_impl(context, param):
    url = url = f'http://localhost:4567/todos?doneStatus={param}'
    context.response = requests.get(url)

@then('an empty list will be returned')
def step_impl(context):
    assert len(context.response.json()["todos"]) == 0