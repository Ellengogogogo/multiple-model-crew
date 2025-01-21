import os
# from decouple import config
from crewai import Crew, Process
# from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks



class ResearchCrew:
    def __init__(self, inputs):
        self.topic = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Initialize agents
        planner = self.agents.content_planer()
        writer = self.agents.content_writer()
        editor = self.agents.content_editor()

        # Initialize tasks with respective agents
        planning_task = self.tasks.planning_task(planner, self.topic)
        writing_task = self.tasks.writing_task(writer, self.topic)
        edit_task = self.tasks.edit_task(editor, [writing_task])

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[planner, writer, editor],
            tasks=[planning_task, writing_task, edit_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the RWE News Crew AI!")
    print("---------------------------------------")
    topic = input("Please enter the main topic of your interest: ")
    
    inputs = f"Topic: {topic}\n"
    research_crew = ResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your research project:")
    print("##############################\n")
    print(result)
