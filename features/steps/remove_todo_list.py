from behave import *
import requests
import json

@given('a course todo list {course} that does not exist')
def step_impl(context, course):
    url = f'http://localhost:4567/categories/{course}'
    response = requests.get(url)
    assert not response.ok

@when('the user deletes a course todo list {course}')
def step_impl(context, course):
    url = f'http://localhost:4567/category/{course}'
    context.response = requests.delete(url)

@when('the user deletes an invalid course todo list {course}')
def step_impl(context, course):
    url = f'http://localhost:4567/category/{course}'
    context.response = requests.delete(url)
    assert not context.response.ok

@then('the course to do list {course} no longer exists')
def step_impl(context, course):
    url = f'http://localhost:4567/category/{course}'
    context.response = requests.delete(url)
    assert not context.response.ok


