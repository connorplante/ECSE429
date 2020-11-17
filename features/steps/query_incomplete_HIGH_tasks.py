from behave import * 
import requests
import json

@given('some tasks have been assigned priorities')
def step_impl(context):
    url = 'http://localhost:4567/categories/3/todos'
    response = requests.get(url)
    if (len(response.json()["todos"]) == 0):
        raise Exception("no HIGH priority tasks")
    url = 'http://localhost:4567/categories/4/todos'
    response = requests.get(url)
    if (len(response.json()["todos"]) == 0):
        raise Exception("no MEDIUM priority tasks")

@when('a user queries for all HIGH priority tasks that are incomplete')
def step_impl(context):
    url = 'http://localhost:4567/categories/3/todos?doneStatus=false'
    context.response = requests.get(url)

@then('a list of all HIGH priority tasks with doneStatus = false will be returned with no others')
def step_impl(context):
    assert context.response.ok and len(context.response.json()["todos"]) == 1

@when('a user queries for all HIGH priority tasks that are complete')
def step_impl(context):
    url = 'http://localhost:4567/categories/3/todos?doneStatus=true'
    context.response = requests.get(url)

@then('a list of all HIGH priority tasks with doneStatus = true will be returned with no others')
def step_impl(context):
    assert context.response.ok and len(context.response.json()["todos"]) == 1

@when('a user queries for all HIGH priority tasks and leaves the doneStatus parameter empty')
def step_impl(context):
    url = 'http://localhost:4567/categories/3/todos?doneStatus'
    context.response = requests.get(url)