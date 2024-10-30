import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()


researcher = Agent(
    role='Senior Market Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You are an expert at a technology research group, skilled in identifying trends and analyzing complex data.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

generator = Agent(
    role='Tech & Real World Use Case Strategist',
    goal='To identify, design, and strategize the implementation of technology use cases that align with organizational goals and address real-world challenges effectively.',
    backstory="""The Tech & Real World Use Case Strategist has a deep understanding of emerging technologies and their potential applications across various industries. They collaborate with cross-functional teams to identify pain points and opportunities, researching and validating use cases to ensure technology solutions drive meaningful impact. With a background in both technology and business, the strategist bridges the gap between technical capabilities and practical needs, helping shape an innovation roadmap that aligns with company objectives and enhances competitive advantage.""",
    verbose=True,
    allow_delegation=True
)


task1 = Task(
    description="""Analyze 2024-2025 AI advancements. Find major trends, new technologies, and their effects. Provide a detailed report.""",
    expected_output="A comprehensive report on major AI trends, technologies, and their potential impacts for 2024-2025.",
    agent=researcher
)

task2 = Task(
    description="""Create a blog post containing use cases about major market trends using your insights. Make it interesting, clear, and suited for both tech and non-tech enthusiasts. It should include at least 3 use cases.""",
    expected_output="A blog post with engaging insights on at least 3 AI market trends, accessible to both technical and non-technical audiences.",
    agent=generator
)


crew = Crew(
    agents=[researcher, generator],
    tasks=[task1, task2],
    verbose=True
)


result = crew.kickoff()
print("################")
print(result)
