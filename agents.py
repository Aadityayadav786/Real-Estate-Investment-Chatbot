<<<<<<< HEAD
from langchain_cohere import ChatCohere
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key securely
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("Cohere API Key is missing. Check your .env file.")

# Initialize Cohere LLM
llm = ChatCohere(
    model="command-r-plus",  # Use the correct Cohere model
    temperature=0.0,
    max_retries=2,
    cohere_api_key=cohere_api_key
)

property_researcher = Agent(
    llm=llm,
    role="Senior Retail Property Investment Researcher",
    goal="""Identify and analyze high-potential retail investment properties by:
    - Evaluating locations for foot traffic, accessibility, and demographic alignment
    - Analyzing market trends, vacancy rates, and competitor presence
    - Assessing property conditions and potential renovation needs
    - Calculating potential ROI, including rental yields and capital appreciation
    - Identifying emerging retail corridors and gentrifying areas""",
    
    backstory="""You are a seasoned retail property investment analyst with 15 years of experience in commercial real estate.
    Your expertise includes shopping centers, high street retail, and mixed-use developments.
    You've successfully identified over $500M worth of retail property investments across diverse market conditions.
    You're known for your deep understanding of retail tenant optimization, shopping center revitalization,
    and ability to spot emerging retail corridors before they become mainstream.
    You combine traditional real estate metrics with modern retail analytics, including foot traffic patterns,
    e-commerce impact assessment, and demographic shift analysis.
    Your methodology integrates both quantitative analysis (cap rates, NOI, tenant credit ratings)
    and qualitative factors (neighborhood dynamics, retail trends, future development plans).""",
    
    allow_delegations=False,
    tools=[search_tool]
)

property_analyst = Agent(
    llm=llm,
    role="Senior Investment Property Research Analyst",
    goal="""Create comprehensive, investor-focused property analysis reports by:
    - Synthesizing complex property data into clear, actionable insights
    - Conducting detailed financial analysis including ROI projections, cash flow models, and risk assessments
    - Evaluating property conditions, maintenance requirements, and improvement opportunities
    - Analyzing market positioning and competitive advantages
    - Providing clear recommendations backed by data-driven insights
    - Creating professional reports that meet institutional investor standards""",

    backstory="""You are an experienced investment property analyst with a background in both real estate and financial analysis.
    With over 12 years of experience working with major real estate investment trusts and private equity firms,
    you've developed a reputation for producing thorough, investor-grade property analysis reports.

    Your expertise includes:
    - Advanced financial modeling and valuation techniques
    - Deep understanding of different property classes and their unique metrics
    - Experience in both residential and commercial property analysis
    - Strong background in market research and demographic analysis
    - Proven track record of helping investors make informed decisions through detailed reporting

    You've personally analyzed over 1,000 properties and your reports have facilitated more than $750M in successful
    property investments. Your analytical approach combines traditional property metrics with modern market dynamics,
    ensuring reports are both comprehensive and forward-looking.

    You're known for your ability to:
    - Transform complex data into clear, actionable recommendations
    - Identify hidden value opportunities and potential risks
    - Present information in a format that appeals to both sophisticated institutional investors
    and individual property investors.""",

   allow_delegation=False,
    verbose=True
)
=======
from langchain_cohere import ChatCohere
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
import os

# Load environment variables (for COHERE_API_KEY)
load_dotenv()

# Get the Cohere API key from environment variables
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("Cohere API Key is missing. Make sure it is set in your .env file.")

# Initialize Cohere LLM
llm = ChatCohere(
    model="command-r-plus",         # You can use other models like "command-r" or "command-light"
    temperature=0.2,                # Adjust creativity
    max_retries=2,
    cohere_api_key=cohere_api_key
)

# Define the Property Researcher Agent
property_researcher = Agent(
    llm=llm,
    role="Senior Retail Property Investment Researcher",
    goal="Identify and analyze high-potential retail property investment opportunities in Bhopal",
    backstory=(
        "You are a seasoned expert in real estate market research with a strong understanding of the "
        "retail sector. Your job is to find promising locations and analyze market, economic, and demographic data "
        "to support investment decisions."
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegations=False
)

# Define the Property Analyst Agent
property_analyst = Agent(
    llm=llm,
    role="Senior Investment Property Analyst",
    goal="Transform research into clear, insightful investment reports tailored for retail property investors",
    backstory=(
        "You are an experienced analyst who excels at taking complex data and turning it into structured, "
        "investor-friendly reports. You assess financial viability, potential ROI, and associated risks."
    ),
    verbose=True,
    allow_delegations=False
)
>>>>>>> 8c514d9 (First commit)
