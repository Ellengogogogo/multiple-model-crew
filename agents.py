from crewai import Agent
#from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq  # Import Groq client
# from langchain_openai import ChatOpenAI
import os
# from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool

# from langchain.agents import load_tools
from langchain.chat_models.azure_openai import AzureChatOpenAI
from dotenv import load_dotenv


class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        # self.serper = SerperDevTool()
        # self.web = WebsiteSearchTool()
        # self.web_scrape=ScrapeWebsiteTool()
        
        # Load the .env file
        load_dotenv()

        model_name = os.environ["AZURE_MODEL_NAME"]
        openai_api_key = os.environ["AZURE_API_KEY"]
        open_ai_base = os.environ["AZURE_API_BASE"]
        openai_api_version = os.environ["AZURE_API_VERSION"]

        # OpenAI Models
        self.llm = AzureChatOpenAI(
                    model=model_name,
                    api_version=openai_api_version,
                    api_key=openai_api_key,   
                    base_url=open_ai_base,
                    temperature=0.2 
                )
    
        # Groq Models
        # self.llama3_8b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-8b-8192")
        # self.llama3_70b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-70b-8192")
        # self.mixtral_8x7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="mixtral-8x7b-32768")
        # self.gemma_7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="gemma-7b-it")

    # def researcher(self):
    # # Detailed agent setup for the Research Expert
    #     return Agent(
    #     role='Expert',
    #     goal='To break down broad visionary ideas into specific, actionable research topics, identify key areas requiring in-depth investigation, and prepare report that serves as a roadmap for future goals.',
    #     backstory="You are an expert that can easily reconvey ideas from others through critical thinking and systems thinking to figure out what the visionary wants to accompolish",
    #     verbose=True,
    #     allow_delegation=False,
    #     llm=self.selected_llm,
    #     max_iter=3,
    #     tools=[self.serper, self.web, self.web_scrape],
    #     ) 


    # def analyst(self):
    #     # Detailed agent setup for the Analyst
    #     return Agent(
    #         role='Analyst',
    #         goal='Come up with a learning curriculumn that will allow for the visionary to reach deep and broad knowledge in order to accomplish their goals',
    #         backstory="You are a talented organized logical educator who can deductively comeup with amazing learning plans in order to provide guidance starting from the goal and working backwards to the begining of a novice level so as to easily bridge the gap between inexperienced and experts alike.",
    #         verbose=True,
    #         allow_delegation=False,
    #         llm=self.selected_llm,
    #         max_iter=3,
    #     )

    # def writer(self):
    #     # Detailed agent setup for the Writer
    #     return Agent(
    #         role='Technical writer',
    #         goal='Use CrewAI tools to search and summarize findings of the previous agent, internet articles titles and their URLs, as well as books and online resource to carry out the learning needed',
    #         backstory="You are organized course creater and talented educator that understands what it takes for beginners to get from point a to point be when it comes to learning, you export great findings, you are great at scraping the web links and resources geared to ward learning specific goals.",
    #         verbose=True,
    #         allow_delegation=False,
    #         llm=self.selected_llm,
    #         tools=[self.serper, self.web, self.web_scrape],
    #         max_iter=3,


    #     )

    def content_planer(self):
        # Detailed agent setup for the Planner
        return Agent(
            role='Content Planner',
            goal="Plan engaging and factually accurate content on {topic}",
            backstory="You're working on planning a article, summerizing the news in last month about the topic: {topic} of a germen energy company RWE in {country}."
                    "You collect the news in the last month so the audience can get the most current news"
                    "Your work is the basis for the Content Writer to write an article on this topic."
                        "Each section should include one news item and cover the following points:"
                        "Topic: Clearly state the subject of the news."
                        "Date: Specify when the event occurred."
                        "Main Role: Describe the primary role or action taken by RWE."
                        "Details: Provide an exact description of what happened.",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def content_writer(self):
        # Detailed agent setup for the Content Writer
        return Agent(
            role='Content Writer',
            goal="Write insightful and factually accurate "
                "news about the topic: {topic}",
            backstory="You're working on writing a artical,"
                    "summerizing the news of the topic: {topic} of "
                    "the germen energy company RWE in last month in {country}"
                    "You base your writing on the work of "
                    "the Content Planner, who provides an outline "
                    "and relevant context about the topic. "
                    "You follow the main objectives and "
                    "direction of the outline, "
                    "as provide by the Content Planner. "
                    "Each section should include one news item and cover the following points:"
                        "Topic: Clearly state the subject of the news."
                        "Date: Specify when the event occurred."
                        "Main Role: Describe the primary role or action taken by RWE."
                        "Details: Provide an exact description of what happened",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def content_editor(self):
        # Detailed agent setup for the Content Editor
        return Agent(
            role='Content Editor',
            goal="Edit the content of the article on the topic: {topic}",
            backstory="You're working on editing a article,"
                    "summerizing the news of the topic: {topic} of "
                    "the germen energy company RWE in last month in {country}"
                    "You base your editing on the work of "
                    "the Content Writer, who provides the draft "
                    "of the article. "
                    "You follow the main objectives and "
                    "direction of the outline, "
                    "as provide by the Content Planner. "
                    "Each section should include one news item and cover the following points:"
                        "Topic: Clearly state the subject of the news."
                        "Date: Specify when the event occurred."
                        "Main Role: Describe the primary role or action taken by RWE."
                        "Details: Provide an exact description of what happened",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )