Feature: Add a to course
    As a student, 
    I create a to do list for a new class I am taking, 
    so I can manage course work.

@course 
Scenario Outline: Create a new course todo list(Normal Flow)
    Given the application is active
    When the user creates a new course to do list <course>
    Then a course todo list <course> with the same title exists

    Examples:
        | course      | 
        | todo list 1 |
        | todo list 2 |
        | todo list 3 |

@course @task
Scenario Outline: Create a new course todo list with a task (Alternate Flow)
    Given the application is active
    And a task <task> exists
    When the user creates a new course to do list <course>
    And the user adds task <task> to category <course>
    And the user adds category <course> to task <task>
    Then a two-way relationship will exist between the task <task> and the category <course>

    Examples:
        | task  | course    | 
        | 3     | 5         | 
        | 4     | 4         |
        | 5     | 3         |

@course 
Scenario Outline: Create an invalid new course todo list (Error Flow)
    Given the application is active
    When the user creates an invalid course to do list <course> POST request
    Then a 400 status code will be returned with an error message
    And a course todo list <course> with the same title doesnt exist

    Examples:
        | course      | 
        | todo list 1 |
        | todo list 2 |
        | todo list 3 |
