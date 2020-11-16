Feature: Mark Task as Done
    As a student,
    I mark a task as done on my course todo list,
    So I can track my accomplishments.

@task
Scenario Outline: Mark a task as done with PUT call (Normal Flow)
    Given a task <task> exists
    When the user changes the doneStatus of task <task> to True with a PUT call
    Then task <task> will be marked as completed

    Examples:
        | task | 
        |  3   | 
        |  4   |
        |  5   |

@task
Scenario Outline: Mark a task as done with POST call (Alternate Flow)
    Given a task <task> exists
    When the user changes the doneStatus of task <task> to True with a POST call
    Then task <task> will be marked as completed

    Examples:
        | task | 
        |  3   | 
        |  4   |
        |  5   |

@task 
Scenario Outline: Mark the doneStatus of a task with a non-boolean value (Error Flow)
    Given a task <task> exists
    When the user changes the doneStatus of task <task> to <nonbool> 
    Then a 400 status code will be returned with an error message

    Examples:
        | task | nonbool   |
        |  3   | test       |   
        |  4   | hi         |
        |  5   | 9          |