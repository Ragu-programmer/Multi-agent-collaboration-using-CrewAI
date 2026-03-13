from crewai import Task
from Agents.senior_developer import senior_developer

user_story_task = Task(
    description="""
    Convert features into user stories.

    Produce user_stories.md containing:
    - feature name
    - user stories
    - development tasks
    - technical subtasks
    - acceptance criteria
    """,
    expected_output="User stories and engineering tasks",
    agent=senior_developer
)