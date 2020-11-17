Feature: Remove task from course to do list
    As a student,
    I remove an unnecessary task from my course to do list,
    so I can forget about it.

@course @task
Scenario Outline: Remove an existing task from a course todo list (Normal Flow)
    Given a relationship exists from course to do list <category> to task <task>
    When the user deletes a task <task>
    And the user deletes the relationship between the course to do list <category> and task <task>
    Then there will be no relation between course to do list <category> and task <task>

    Examples:
        | task  | category  | 
        | 3     | 3         | 
        | 4     | 3         | 
        | 5     | 3         | 

@course @task
Scenario Outline: Remove an existing task from a course todo list (Alternate Flow)
    Given a relationship exists from course to do list <category> to task <task>
    When the user deletes the relationship between the course to do list <category> and task <task>
    Then there will be no relation between course to do list <category> and task <task>

    Examples:
        | task  | category  | 
        | 3     | 3         | 
        | 4     | 3         | 
        | 5     | 3         | 


@course @task
Scenario Outline: Remove a non existent task from a course todo list (Error Flow)
    Given a course todo list <course> exists
    When the user removes a task <task> that does not exist from course to do list <course>
    Then a 404 status code will be returned with an error message

    Examples:
        | task  | course    | 
        | 100   | 3         | 
        | -2    | 4         | 
        | 000   | 5         | 