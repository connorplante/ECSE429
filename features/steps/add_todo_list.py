from behave import *
import requests
import json

@given('the application is active')
def step_impl(context):
    url = f'http://localhost:4567/'
    context.response = requests.get(url)
    assert context.response.ok

@given('a todolist {course} exists')
def step_impl(context, course):
    url = f'http://localhost:4567/categories/{course}'
    context.response = requests.get(url)
    if (not context.response.ok):
        raise Exception(f'Category {course} does not exist')


@when('the user creates a new course to do list {course}')
def step_impl(context,course):
    url = f'http://localhost:4567/categories'
    data=f'''{{
        "title": "{course}"
    }}
    '''
    context.response = requests.post(url, data=data)

@when('the user creates an invalid course to do list {course} POST request')
def step_impl(context,course):
    url = f'http://localhost:4567/categories'
    data=f'''{{
        "mylength": "3",
        "title": "{course}"
    }}
    '''
    context.response = requests.post(url, data=data)

@then('a course todo list {course} with the same title exists')
def step_impl(context, course):
    url = f'http://localhost:4567/categories'
    context.response = requests.get(url)
    category_title = False

    for i in context.response.json()["categories"]:
        if (i["title"] == course):
            category_title = True
            break

    assert category_title

@then('a course todo list {course} with the same title doesnt exist')
def step_impl(context, course):
    url = f'http://localhost:4567/categories'
    context.response = requests.get(url)
    category_title = False

    for i in context.response.json()["categories"]:
        if (i["title"] == course):
            category_title = True
            break

    assert not category_title


