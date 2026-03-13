from crewai import Task
from Agents.product_owner import product_owner

requirement_task = Task(
    description="""
    Analyze the client request.

    Produce a document called product_requirements.md containing:
    - product overview
    - user personas
    - key workflows
    - functional requirements
    - non-functional requirements
    - acceptance criteria
    """,
    expected_output="Structured product requirement document",
    agent=product_owner
)