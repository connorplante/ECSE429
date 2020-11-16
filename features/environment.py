from behave import  *
import requests
import socket
import subprocess
import time

def before_all(context):
    context.config.setup_logging()

def before_scenario(context, scenario):
    # start application
    subprocess.Popen(['java -jar /Users/connorplante/Documents/ECSE429/Project_B/runTodoManagerRestAPI-1.5.5.jar &> /dev/null'], shell=True)
    time.sleep(0.5)
    # check if application is running  
    if (tryPort(4567)):
        raise Exception("Application is not running on port 4567")
    
    # adding categories id  = 3,4,5,6
    if ("priority" in context.tags):
        url = 'http://localhost:4567/categories'
        data = '''{
        "title": "HIGH"
        }'''
        response = requests.post(url, data=data) # 3
        data = '''{
        "title": "MEDIUM"
        }'''
        response = requests.post(url, data=data) # 4
        data = '''{
        "title": "LOW"
        }'''
        response = requests.post(url, data=data) # 5
    # data = '''{
    # "title": "Physics Course"
    # }'''
    # response = requests.post(url, data=data) # 6

    # adding todo id = 3,4,5,6
    if ("task" in context.tags):
        url = 'http://localhost:4567/todos'
        data = '''{
            "title": "Assignment3",
            "doneStatus": false,
            "description": "write essay"
        }'''
        response = requests.post(url, data=data) # 3
        data = '''{
            "title": "Assignment4",
            "doneStatus": false,
            "description": "write poem"
        }'''
        response = requests.post(url, data=data) # 4
        data = '''{
            "title": "Assignment5",
            "doneStatus": false,
            "description": "write song"
        }'''
        response = requests.post(url, data=data) # 5
        data = '''{
            "title": "Assignment6",
            "doneStatus": true,
            "description": "do math"
        }'''
        response = requests.post(url, data=data) # 6, done

def after_scenario(context, scenario):
    try:
        url = 'http://localhost:4567/shutdown'
        response = requests.get(url)
    except:
        pass

def tryPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind(("0.0.0.0", port))
        result = True
    except:
        result = False
    sock.close()
    return result