from crewai import Task
from Agents.junior_developer import junior_developer

implementation_task = Task(
    description="""
    Implement user stories.

    Produce:
    implementation.md
    pull_request.md

    Include:
    - implementation approach
    - code snippets
    - file structure
    - PR description
    - reviewers (senior developer and engineering manager)
    """,
    expected_output="Implementation plan and pull request description",
    agent=junior_developer
)
