from crewai import Task
from Agents.solution_architect import solution_architect

architecture_task = Task(
    description="""
    Read product requirements and design system architecture.

    Produce:
    solution_architecture.md
    system_flow.md
    tech_stack.md

    Include:
    - system components
    - service interactions
    - API boundaries
    - data flow
    - scalability considerations
    """,
    expected_output="System architecture and flow design documents",
    agent=solution_architect
)