Feature: Change Description
    As a student,
    I want to change a task description, 
    To better represent the work to do.

@task
Scenario Outline: Change task description with PUT call (Normal Flow)
    Given a task exists
    When the user sends a PUT call to the api with the id of the task, the <title> and the new description <description>
    Then it will be successfully updated with the new description <description>

    Examples:
        | title       | description             | 
        | Assignment3 | do physics problem set  |
        | Assignment3 | do mathematics          | 
        | Assignment3 | write a pancake         |

@task
Scenario Outline: Change task description with POST call (Alternate Flow)
    Given a task exists
    When the user sends a POST call to the api with the id of the task and the new description <description>
    Then it will be successfully updated with the new description <description>

    Examples:
        | description               | 
        | do physics problem set    |
        | do mathematics            | 
        | write a pancake           |

@task
Scenario Outline: Attempt to change task description with PUT call without passing a title (Error Flow)
    Given a task exists
    When the user sends a PUT call to the api with only the id of the task and the new description <description>
    Then a 400 status code will be returned
    And an error message will be sent back to the user

    Examples:
        | description               | 
        | do physics problem set    |
        | do mathematics            | 
        | write a pancake           |