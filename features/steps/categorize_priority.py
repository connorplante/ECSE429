from behave import *
import requests
import json

@given('the categories HIGH, MEDIUM and LOW exist')
def step_impl(context):
    url = 'http://localhost:4567/categories'
    response = requests.get(url)
    high = response.json()["categories"][2]["title"] = "HIGH"
    medium = response.json()["categories"][3]["title"] = "MEDIUM"
    low = response.json()["categories"][4]["title"] = "LOW"
    if (not (high and medium and low)):
        raise Exception("categories HIGH, MEDIUM and LOW not present")

@given('a task {task} exists')
def step_impl(context, task):
    url = f'http://localhost:4567/todos/{task}'
    response = requests.get(url)
    if (not response.ok):
        raise Exception(f'task {task} not present')

@when('the user adds task {task} to category {category}')
@given('a relationship exists from category {category} to task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/categories/{category}/todos'
    data=f'''{{
        "id": "{task}"
    }}
    '''
    response = requests.post(url, data=data)

@when('the user adds category {category} to task {task}')
@given('a relationship exists from task {task} to category {category}')
@when('a user assigns task {task} a priority {category} that does not exist')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories'
    data=f'''{{
        "id": "{category}"
    }}
    '''
    context.response = requests.post(url, data=data)

@when('the user removes both relationships between category {category} and task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories/{category}'
    response = requests.delete(url)

    url = f'http://localhost:4567/categories/{category}/todos/{task}'
    response = requests.delete(url)

@then('a two-way relationship will exist between the task {task} and the category {category}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories'
    response = requests.get(url)
    todo_to_category = False
    for i in response.json()["categories"]:
        if (i["id"] == category):
            todo_to_category = True
            break

    url = f'http://localhost:4567/categories/{category}/todos'
    response = requests.get(url)
    category_to_todo = False
    for i in response.json()["todos"]:
        if (i["id"] == task):
            category_to_todo = True
            break
        
    assert category_to_todo and todo_to_category

@then('there will be no association between the task {task} and the priority {category}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/todos/{task}/categories'
    response = requests.get(url)
    todo_to_category = not response.json()["categories"]

    url = f'http://localhost:4567/categories/{category}/todos'
    response = requests.get(url)
    category_to_todo = not response.json()["todos"]

    assert category_to_todo and todo_to_category

@then('a 404 status code will be returned')
def step_impl(context):
    assert context.response.status_code == 404