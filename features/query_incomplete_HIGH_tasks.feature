Feature: Query All Incomplete High Priority Tasks
    As a student,
    I query all incomplete HIGH priority tasks from all my classes,
    To identity my short-term goals.

@task @priority @link_task_priority
Scenario: Query All Incomplete HIGH Priority Tasks (Normal Flow)
    Given some tasks have been assigned priorities
    When a user queries for all HIGH priority tasks that are incomplete
    Then a list of all HIGH priority tasks with doneStatus = false will be returned with no others

@task @priority @link_task_priority
Scenario: Query All Completed HIGH Priority Tasks (Alternative Flow)
    Given some tasks have been assigned priorities
    When a user queries for all HIGH priority tasks that are complete
    Then a list of all HIGH priority tasks with doneStatus = true will be returned with no others

@task @priority @link_task_priority
Scenario: Query All HIGH Priority Tasks with Empty Completion Status (Error Flow)
    Given some tasks have been assigned priorities
    When a user queries for all HIGH priority tasks and leaves the doneStatus parameter empty
    Then an empty list will be returned