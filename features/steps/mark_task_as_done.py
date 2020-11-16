from behave import *
import requests
import json

@when('the user changes the doneStatus of task {task} to True with a PUT call')
def step_impl(context, task):
    url = f'http://localhost:4567/todos/{task}'
    data=f'''{{
        title = "some title",
        doneStatus = True
    }}
    '''
    context.response = requests.put(url, data=data)

@when('the user changes the doneStatus of task {task} to True with a POST call')
def step_impl(context, task):
    url = f'http://localhost:4567/todos/{task}'
    data=f'''{{
        doneStatus = True
    }}
    '''
    context.response = requests.post(url, data=data)

@when('the user changes the doneStatus of task {task} to {nonbool}')
def step_impl(context, task, nonbool):
    url = f'http://localhost:4567/todos/{task}'
    data=f'''{{
        doneStatus = {nonbool}
    }}
    '''
    context.response = requests.post(url, data=data)

@then('task {task} will be marked as completed')
def step_impl(context, task):
    url = f'http://localhost:4567/todos/{task}'
    assert context.response.json()["doneStatus"] == "true"