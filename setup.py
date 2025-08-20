from setuptools import setup, find_packages

setup(
    name='mcp_weather_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langgraph',
        'openswe',
        'transformers',
    ],
    entry_points={
        'openswe.agents': [
            'manager = mcp_weather_project.agents.manager_agent:ManagerAgent',
            'planner = mcp_weather_project.agents.planner_agent:PlannerAgent',
            'researcher = mcp_weather_project.agents.researcher_agent:ResearcherAgent',
            'reviewer = mcp_weather_project.agents.reviewer_agent:ReviewerAgent',
        ],
