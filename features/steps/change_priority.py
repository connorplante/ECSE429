from behave import *
import requests
import json

@then("the old two-way relationship will no longer exist between task {task} and category {category}")
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories/{category}'
    response1 = requests.delete(url)

    url = f'http://localhost:4567/categories/{category}/todos/{task}'
    response2 = requests.delete(url)

    assert not response1.ok and not response2.ok

@given('a relationship does not exist from category {category} to task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/categories/{category}/todos/{task}'
    response = requests.delete(url)
    if (response.ok):
        raise Exception("relation already exists")

@given('a relationship does not exist from task {task} to category {category}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories/{category}'
    response = requests.delete(url)
    if (response.ok):
        raise Exception("relation already exists")

@when('the user attempts to delete the relationship between task {task} and category {category}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories/{category}'
    context.response = requests.delete(url)

@then('a 404 status code will be returned with an error message')
def step_impl(context):
    assert context.response.status_code == 404 and context.response.json()["errorMessages"]