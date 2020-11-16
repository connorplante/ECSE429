from behave import *
import requests
import json

@given('a course todo list {course} exists')
def step_impl(context, course):
    url = f'http://localhost:4567/categories/{course}'
    response = requests.get(url)
    if (not response.ok):
        raise Exception(f'Category {course} does not exist')

@when('the user creates a new task {task} with a relationship to category {course}')
def step_impl(context, task, course):
    url = f'http://localhost:4567/todos'
    data=f'''{{
        "title": "new task",
        "categories": [
        {{
            "id": "{course}"
        }}
    ]
    }}
    '''
    response = requests.post(url, data=data)

@when('the user adds a task {task} that does not exist to category {course}')
def step_impl(context, task, course):
    url = f'http://localhost:4567/categories/{course}'
    data=f'''{{
        "id": "{task}"
    }}'''
    context.response = requests.post(url, data=data)

@then('a 400 status code will be returned with an error message')
def step_impl(context):
    assert context.response.status_code == 400 and context.response.json()["errorMessages"]
