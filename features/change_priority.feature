Feature: Change Priority
    As a student,
    I want to adjust the priority of a task,
    To help better manage my time.

@priority @task
Scenario Outline: Change priority of a task (Normal Flow)
    Given a relationship exists from category <category> to task <task>
    And a relationship exists from task <task> to category <category> 
    When the user removes both relationships between category <category> and task <task>
    And the user adds task <task> to category <priority2>
    And the user adds category <priority2> to task <task>
    Then a two-way relationship will exist between the task <task> and the category <priority2>
    And the old two-way relationship will no longer exist between task <task> and category <category>

    Examples:
        | task  | category  | priority2 |
        | 3     | 5         | 3         |
        | 4     | 3         | 4         |
        | 5     | 4         | 5         |

@priority @task
Scenario Outline: Add a priority to a task (Alternate Flow)
    Given a relationship exists from category <category> to task <task>
    And a relationship exists from task <task> to category <category> 
    When the user adds task <task> to category <category2>
    And the user adds category <category2> to task <task>
    Then a two-way relationship will exist between the task <task> and the category <category2>

    Examples:
        | task  | category  | category2 |
        | 3     | 5         | 3         |
        | 4     | 3         | 4         |
        | 5     | 4         | 5         |

@priority @task
Scenario Outline: Remove a priority relationship that does not exist (Error Flow)
    Given a relationship does not exist from category <category> to task <task>
    And a relationship does not exist from task <task> to category <category>
    When the user attempts to delete the relationship between task <task> and category <category>
    Then a 404 status code will be returned with an error message 
    
    Examples:
        | task  | category  | 
        | 3     | 5         | 
        | 4     | 4         |
        | 5     | 3         |
