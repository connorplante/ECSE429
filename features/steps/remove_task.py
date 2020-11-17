from behave import *
import requests
import json

@given('a relationship exists from course to do list {category} to task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/categories/{category}/todos'
    data=f'''{{
        "id": "{task}"
    }}
    '''
    context.response = requests.post(url, data=data)

@when('the user deletes a task {task}')
def step_impl(context, task):
    url = f'http://localhost:4567/todos/{task}'
    context.response = requests.delete(url)

@when('the user deletes the relationship between the course to do list {category} and task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/categories/{category}/todos/{task}'
    context.response = requests.delete(url)

@then('there will be no relation between course to do list {category} and task {task}')
def step_impl(context, task, category):
    url = f'http://localhost:4567/categories/{category}/todos/{task}'
    response = requests.delete(url)
    assert not response.ok

@when('the user removes a task {task} that does not exist from course to do list {course}')
def step_impl(context, task, course):
    url = f'http://localhost:4567/todos/{task}'
    context.response = requests.delete(url)