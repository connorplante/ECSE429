Feature: Remove a todo list 
    As a student,
    I remove a to do list for a class which I am no longer taking,
    to declutter my schedule.

@course
Scenario Outline: Remove an existing course todo list (Normal Flow)
    Given a course todo list <course> exists
    When the user deletes a course todo list <course>
    Then the course to do list <course> no longer exists

    Examples:
        | course  |
        | 3       |
        | 4       |
        | 5       |

@course @task
Scenario Outline: Remove an existing course todo list (Alternate Flow)
    Given a course todo list <course> exists
    And a relationship exists from course to do list <course> to task <task>
    When the user deletes a course todo list <course> 
    And the user deletes the relationship between the course to do list <course> and task <task>
    Then the course to do list <course> no longer exists
    And there will be no relation between course to do list <course> and task <task>

    Examples:
        | task  | course    | 
        | 3     | 3         | 
        | 4     | 4         | 
        | 5     | 5         | 

@course
Scenario Outline: Remove an existing course todo list (Error Flow)
    Given a course todo list <course> that does not exist
    When the user deletes an invalid course todo list <course>
    Then a 404 status code will be returned

    Examples:
        | course   |
        | 99       |
        | -1       |
        | 00       |