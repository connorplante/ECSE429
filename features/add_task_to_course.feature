Feature: Add Task to Course Todo List
    As a student,
    I add a task to acourse todo list,
    So I can remember it.

@course @task
Scenario Outline: Add an existing task to a course todo list (Normal Flow)
    Given a course todo list <course> exists
    And a task <task> exists
    When the user adds task <task> to category <course>
    And the user adds category <course> to task <task>
    Then a two-way relationship will exist between the task <task> and the category <course>

    Examples:
        | task  | course    | 
        | 3     | 3         | 
        | 4     | 3         | 
        | 5     | 3         | 

@course
Scenario Outline: Create a new task that is added to the course todo list (Alternate Flow)
    Given a course todo list <course> exists
    When the user creates a new task <task> with a relationship to category <course>
    And the user adds task <task> to category <course>
    Then a two-way relationship will exist between the task <task> and the category <course>

    Examples:
        | task  | course    | 
        | 3     | 3         | 
        | 3     | 4         | 
        | 3     | 5         | 

@course
Scenario Outline: Add a non existent task to a course todo list (Error Flow)
    Given a course todo list <course> exists
    When the user adds a task <task> that does not exist to category <course>
    Then a 400 status code will be returned with an error message

    Examples:
        | task  | course    | 
        | 100   | 3         | 
        | -2    | 4         | 
        | 000   | 5         | 
       