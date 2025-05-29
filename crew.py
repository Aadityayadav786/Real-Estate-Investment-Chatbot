<<<<<<< HEAD
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
=======
from crewai import Crew
from agents import property_researcher, property_analyst
from tasks import generate_tasks

def run_crew_for_city(city_name: str):
    # Generate tasks dynamically based on city name
    property_research_task, property_analysis_task = generate_tasks(city_name)

    # Create Crew instance with agents and tasks
    crew = Crew(
        agents=[property_researcher, property_analyst],
        tasks=[property_research_task, property_analysis_task],
        verbose=True
    )

    # Run the crew and get output
    task_output = crew.kickoff()
    return task_output

# For testing standalone (optional)
# if __name__ == "__main__":
#     city = "Bhopal"
#     output = run_crew_for_city(city)
#     print(output)
>>>>>>> 8c514d9 (First commit)
