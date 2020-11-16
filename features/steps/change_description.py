from behave import *
import requests
import json

url = 'http://localhost:4567/todos/3'

@given('a task exists')
def step_impl(context):
    response = requests.get(url)
    print(response.json())
    if (not response.ok):
        raise Exception("task not present")

@when('the user sends a PUT call to the api with the id of the task, the {title} and the new description {description}')
def step_impl(context, title, description):
    data=f'''{{
        "title": "{title}",
        "description": "{description}"
    }}
    '''
    response = requests.put(url, data=data)

@when('the user sends a POST call to the api with the id of the task and the new description {description}')
def step_impl(context, description):
    data=f'''{{
        "description": "{description}"
    }}
    '''
    response = requests.post(url, data=data)

@when('the user sends a PUT call to the api with only the id of the task and the new description {description}')
def step_impl(context, description):
    data=f'''{{
        "description": "{description}"
    }}
    '''
    context.response = requests.put(url, data=data)
    
@then('a 400 status code will be returned')
def step_impl(context):
    assert context.response.status_code == 400

@then('an error message will be sent back to the user')
def step_impl(context):
    assert context.response.json()["errorMessages"][0] == "title : field is mandatory"

@then('it will be successfully updated with the new description {description}')
def step_impl(context, description):
    response = requests.get(url)
    assert response.json()["todos"][0]["description"] == description

    