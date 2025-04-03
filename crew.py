from crewai import Crew
from agents import property_researcher, property_analyst
from tasks import property_research_task, property_analysis_task

crew = Crew(
    agents=[property_researcher, property_analyst],
    tasks=[property_research_task, property_analysis_task],
    verbose=True
)

task_output = crew.kickoff()
print(task_output)
