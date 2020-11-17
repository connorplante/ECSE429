Feature: Query All Incomplete Tasks for a Class
    As a student,
    I query the incomplete tasks for a class I am taking,
    To help manage my time.

@task @course @link_task_course
Scenario: Query All Incomplete Tasks for a Category (Normal Flow)
    Given there is a course with associated tasks
    When the user queries for all associated tasks with doneStatus = false
    Then the returned subset of tasks associated to the course will exclude those having already been completed

@task
Scenario: Query All Incomplete Tasks in the System (Alternate Flow)
    Given there are tasks in the system
    When the user queries for all tasks with doneStatus = false
    Then the returned subset of tasks will be all those with a false doneStatus

@task 
Scenario Outline: Query All Tasks with Improper doneStatus Parameter (Error Flow)
    Given there are tasks in the system
    When the user queries for all tasks with doneStatus = <param>
    Then an empty list will be returned

    Examples:
        | param | 
        | no    |
        | 99    |
        | yes   |