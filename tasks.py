from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    # def research_task(self, agent, inputs):
    #   return Task(
    #       agent=agent,
    #       description=f" Based {inputs} figure out what it is that the user needs in order to figure out their problem, check https://www.thetoolbus.ai/ai-tools, and https://appsumo.com/collections/new/ for relevant tools that could be usefull ",
    #       expected_output=f"A clear explanation of the principles, concepts, disciplines, and skills needed by the visionary in order to accomoplish their goal"

    #   )


    # def analysis_task(self, agent, context):
    #   return Task(
    #     agent=agent,
    #     context=context,
    #     description=f"Evaluate the following report: {context}. Based on the results, create a learning plan, figure out the things the user needs to learn and focus on.",
    #     expected_output=f"A thorough learning plan for the next agent"
   
    # )


    # def writing_task(self, agent, context, inputs):
    #     return Task(
    #         agent=agent,
    #         context=context,
    #         description=f"Answer the users inquiry their request topics: {inputs} Given the following learning plan {context}, using web search, web scraping ,figure give 5 principles or concepts that the user needs to learn with a short overview of each one and what it is, 5 internet articles titles and their URL, 5 books name and author and their purpose.",
    #         expected_output=f" 5 principles and concepts reviewed, and thoroughly explaiened , 5 internet articles titles and their URL,  5 books name and author and their purpose.",
    #     )

    
    def planning_task(self, agent, topic):
        return Task(
            agent=agent,
            description=("1. Prioritize the latest trends, key players, "
                  f"and noteworthy news on {topic} for the energy company RWE in Germany.\n"
              "2. Identify the target audience, considering "
                  "their interests and pain points.\n"
              "3. Develop a detailed content outline including "
                  f"key points, and a call to action for different news on {topic}.\n"
              "4. Include SEO keywords and relevant data or sources."
            ),
            expected_output="A comprehensive content plan document "
                "with a topic, date, main role, details and resources."
              )

    def writing_task(self, agent, topic):
        return Task(
            agent=agent,
            description=(
                "1. Use the content plan to craft a compelling "
                    f"news post on {topic} of RWE.\n"
                "2. Incorporate SEO keywords naturally.\n"
                "3. Sections/Subtitles are properly named "
                    "in an engaging manner.\n"
                "4. Ensure the post is structured with an "
                    "engaging introduction, insightful body, "
                    "and a summarizing conclusion.\n"
                "5. Proofread for grammatical errors and "
                    "alignment with the brand's voice.\n"
            ),
            expected_output="A well-written news post "
                "in markdown format, ready for publication, "
                "each section include one news topic.",
        )

    def edit_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description=("Proofread the given news post for "
                        "grammatical errors and "
                        "alignment with the brand's voice."),
            expected_output="A well-written news post in markdown format, "
                            "ready for publication, "
                            "each section include one news topic.",
        )



