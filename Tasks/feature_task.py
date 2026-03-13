from crewai import Task
from Agents.engineering_manager import engineering_manager

feature_task = Task(
    description="""
    Analyze architecture and break the system into features.

    Produce features.md containing:
    - feature list
    - feature descriptions
    - engineering milestones
    - feature ownership plan
    """,
    expected_output="Feature breakdown and engineering roadmap",
    agent=engineering_manager
)