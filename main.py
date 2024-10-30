import os
import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun


st.sidebar.title("📊 API Configuration")
OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key", type="password")
st.title("📝 Market Research & Use Case Generation")
st.markdown("Generate articles on any topic using AI-powered agents.")
topic = st.text_input("Enter a topic for your article:", placeholder="e.g., Space exploration, Climate change")


if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
else:
    st.warning("Please enter your OpenAI API key in the sidebar to proceed.")


search_tool = DuckDuckGoSearchRun()


researcher = Agent(
    role='Senior Market Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="You are an expert at a technology research group, skilled in identifying trends and analyzing complex data.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

generator = Agent(
    role='Tech & Real World Use Case Strategist',
    goal='To identify, design, and strategize the implementation of technology use cases that align with organizational goals and address real-world challenges effectively.',
    backstory="The Tech & Real World Use Case Strategist has a deep understanding of emerging technologies and their potential applications across various industries.",
    verbose=True,
    allow_delegation=True
)
reporter = Agent(
    role='Resource Asset Collection Specialist',
    goal=(
        'To gather, organize, and document relevant datasets and resources that support Rohan Sridhar’s project use cases. '
        'Search platforms like Kaggle, HuggingFace, and GitHub to find datasets and resources that align with project requirements.'
    ),
    backstory=(
        "The Resource Asset Collection Specialist has a keen eye for identifying and curating data resources, ensuring "
        "relevance and quality. With a solid understanding of project needs, they streamline access to key datasets and assets, "
        "saving time and optimizing workflow."
    ),
    verbose=True,
    allow_delegation=True
)



task1 = Task(
    description=f"Analyze AI advancements related to '{topic}'. Find major trends, new technologies, and their effects.Identify the company’s key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.). A vision and product information on the industry should be fine as well. Provide a detailed report.",
    expected_output="A comprehensive report on major AI trends, technologies, and their potential impacts.  ",
    agent=researcher
)

task2 = Task(
    description="Based on the industry conducted, analyze industry trends and standards within the company’s sector related to AI, ML, and automation.Propose relevant use cases where the company can leverage GenAI, LLMs, and ML technologies to improve their processes, enhance customer satisfaction, and boost operational efficiency.",
    expected_output="A blog post with engaging insights on at least 3 AI market trends, accessible to both technical and non-technical audiences.",
    agent=generator
)
task3 = Task(
    description=(
        "Collect relevant datasets and resources,use cases by searching platforms "
        "such as Kaggle, HuggingFace, and GitHub. Document the resource links in a structured text or markdown file."
    ),
    expected_output=(
        "A well-organized text all the details of researched content along with the use cases containing links to datasets and resources with descriptions, "
        "indicating their relevance to each project use case."
    ),
    agent=reporter
)


# Initialize crew
crew = Crew(
    agents=[researcher, generator,reporter],
    tasks=[task1, task2,task3],
    process=Process.sequential,
    verbose=True
)


if st.button("Generate Article"):
    if not OPENAI_API_KEY:
        st.error("Please enter your OpenAI API key.")
    elif not topic:
        st.error("Please enter a topic.")
    else:
        with st.spinner("Generating content..."):
            result = crew.kickoff(inputs={'topic': topic})
        st.success("Article generated successfully!")
        st.subheader("Generated Report")
        st.markdown(result)
