Feature: Prioritize Tasks
    As a student,
    I categorize tasks as HIGH, MEDIUM or LOW priority,
    So I can better manage my time.

@priority @task
Scenario Outline: Prioritize todo tasks (Normal Flow)
    Given the categories HIGH, MEDIUM and LOW exist
    And a task <task> exists
    When the user adds task <task> to category <category>
    And the user adds category <category> to task <task>
    Then a two-way relationship will exist between the task <task> and the category <category>

    Examples:
        | task  | category  | 
        | 3     | 5         | 
        | 4     | 4         |
        | 5     | 3         |

@priority @task
Scenario Outline: Remove priority from tasks (Alternate Flow)
    Given a relationship exists from category <category> to task <task>
    And a relationship exists from task <task> to category <category> 
    When the user removes both relationships between category <category> and task <task>
    Then there will be no association between the task <task> and the priority <category>

    Examples:
        | task  | category  | 
        | 3     | 5         | 
        | 4     | 4         |
        | 5     | 3         |

@priority @task
Scenario Outline: Assign non-existent priority to a task (Error Flow)
    Given a task <task> exists
    When a user assigns task <task> a priority <category> that does not exist
    Then a 404 status code will be returned

    Examples:
        | task  | category  | 
        | 3     | 800       | 
        | 4     | -11       |
        | 5     |  98       |