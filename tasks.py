<<<<<<< HEAD
from crewai import Task
from agents import property_researcher, property_analyst

property_research_task = Task(
    description="Conduct a comprehensive analysis of potential retail property investments in different cities of Indore.",
    specific_research_requirements=[
        "1. Market Analysis:",
        "- Identify top 3-5 potential retail property investment locations",
        "- Analyze current market trends and economic indicators",
        "- Assess demographic data and consumer spending patterns",
        "- Evaluate local retail ecosystem and potential tenant mix",
        
        "2. Property Evaluation Criteria:",
        "- Foot traffic analysis",
        "- Accessibility and transportation infrastructure",
        "- Proximity to complementary businesses",
        "- Local economic development plans",
        
        "3. Financial Analysis:", 
        "- Estimate potential rental yields",
        "- Calculate projected ROI",
        "- Assess property valuation and appreciation potential",
        "- Identify potential renovation or repositioning opportunities",
        
        "4. Risk Assessment:",
        "- Analyze competitor landscape",
        "- Evaluate e-commerce impact on local retail",
        "- Assess potential regulatory or zoning challenges",
        "- Identify potential long-term growth barriers",
        
        "5. Detailed Reporting:",
        "- Provide a comprehensive report with:",
        "  - Executive summary",
        "  - Detailed market insights",
        "  - Property recommendations",
        "  - Financial projections",
        "  - Risk analysis"
    ],
    agent=property_researcher,
    expected_output="A structured report with insights on market trends, property evaluations, financial metrics, risk assessment, and investment recommendations.",
    output_file="research_task_output.txt"
)

property_analysis_task = Task(
    description="Summarize the property information into a bullet point list.",
    expected_output="""A detailed report of each of the cities.
    The results should ALWAYS be formatted as shown below:

    City 1: Name of the city
    Mean Price: $1,200,000
    Rental Vacancy: x%
    Rental Yield: y%
    Background Information: These cities are typically located near major transport hubs,
    employment centers, and educational institutions.
    The following list highlights some of the top contenders for investment opportunities.""",
    
    agent=property_analyst,
    output_file="property_analysis_report.txt"
)
=======
from crewai import Task
from agents import property_researcher, property_analyst

def generate_tasks(city_name: str):
    property_research_task = Task(
        description=f"Conduct a comprehensive analysis of potential retail property investments in different areas of {city_name}.",
        specific_research_requirements=[
            "1. Market Analysis:",
            "- Identify top 3-5 potential retail property investment locations",
            "- Analyze current market trends and economic indicators",
            "- Assess demographic data and consumer spending patterns",
            "- Evaluate local retail ecosystem and potential tenant mix",
            
            "2. Property Evaluation Criteria:",
            "- Foot traffic analysis",
            "- Accessibility and transportation infrastructure",
            "- Proximity to complementary businesses",
            "- Local economic development plans",
            
            "3. Financial Analysis:", 
            "- Estimate potential rental yields",
            "- Calculate projected ROI",
            "- Assess property valuation and appreciation potential",
            "- Identify potential renovation or repositioning opportunities",
            
            "4. Risk Assessment:",
            "- Analyze competitor landscape",
            "- Evaluate e-commerce impact on local retail",
            "- Assess potential regulatory or zoning challenges",
            "- Identify potential long-term growth barriers",
            
            "5. Detailed Reporting:",
            "- Provide a comprehensive report with:",
            "  - Executive summary",
            "  - Detailed market insights",
            "  - Property recommendations",
            "  - Financial projections",
            "  - Risk analysis",
            "  - Useful Links & Resources section with relevant official and market data URLs"
        ],
        agent=property_researcher,
        expected_output=(
            "A structured, detailed report including:\n"
            "- Market trends and demographic insights\n"
            "- Property evaluations (foot traffic, accessibility, etc.)\n"
            "- Financial metrics like rental yields and ROI\n"
            "- Risk factors\n"
            "- Investment recommendations for all salary groups\n"
            "- A dedicated 'Useful Links & Resources' section with relevant URLs for the city\n"
        ),
        output_file="research_task_output.txt"
    )

    property_analysis_task = Task(
        description=f"Summarize the property information into a detailed bullet point report for {city_name}.",
        expected_output=(
            "The report should ALWAYS follow this format:\n\n"
            f"City: {city_name}\n"
            "Mean Price: [average price in local currency]\n"
            "Rental Vacancy: [vacancy rate %]\n"
            "Rental Yield: [yield % for prime and emerging areas]\n\n"
            "Background Information: [detailed city insights covering economic growth, retail corridors, infrastructure projects, and demographic trends]\n\n"
            "Investment Recommendations:\n"
            "- Include insights for low, middle, and high salary earning groups\n\n"
            "Useful Links & Resources:\n"
            "- Provide at least 3-5 relevant official or market data URLs related to the city's real estate, infrastructure, or economic development\n\n"
            "**Final Recommendation:** [clear investment advice balancing risk and growth potential]\n"
        ),
        agent=property_analyst,
        output_file="property_analysis_report.txt"
    )
    
    return property_research_task, property_analysis_task
>>>>>>> 8c514d9 (First commit)
