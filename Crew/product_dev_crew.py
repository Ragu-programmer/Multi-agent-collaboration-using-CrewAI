from crewai import Crew

from Agents.product_owner import product_owner
from Agents.solution_architect import solution_architect
from Agents.engineering_manager import engineering_manager
from Agents.senior_developer import senior_developer
from Agents.junior_developer import junior_developer

from Tasks.requirement_task import requirement_task
from Tasks.architecture_task import architecture_task
from Tasks.feature_task import feature_task
from Tasks.user_story_task import user_story_task
from Tasks.implementation_task import implementation_task

product_dev_crew = Crew(
    agents=[
        product_owner,
        solution_architect,
        engineering_manager,
        senior_developer,
        junior_developer
    ],
    tasks=[
        requirement_task,
        architecture_task,
        feature_task,
        user_story_task,
        implementation_task
    ],
    verbose=True
)