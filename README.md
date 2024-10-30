# Multi-agent-Researcher

# 📝 Market Research & Use Case Generation Tool

This application leverages AI-powered agents to conduct market research, identify use cases, and gather relevant datasets for any topic. Built with Streamlit and LangChain's `Agent` and `Task` components, this tool allows users to input a topic, generate insights, propose use cases, and collect resources related to emerging technologies and AI advancements.

## Features
- **Automated Market Research**: Conducts research on cutting-edge developments in AI and data science.
- **Use Case Generation**: Identifies and proposes use cases aligning with strategic goals and industry trends.
- **Dataset Collection**: Searches for relevant datasets and resources on platforms like Kaggle, HuggingFace, and GitHub.

## Getting Started

### Prerequisites
1. **Python 3.8 or later** - Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. **Streamlit** - Install Streamlit to create and run the web app:
   ```bash
   pip install streamlit
   ```
3. **CrewAI and LangChain Community Tools** - Install necessary libraries for AI agent capabilities:
   ```bash
   pip install crewai langchain-community
   ```

### Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/market-research-use-case-gen.git
   cd market-research-use-case-gen
   ```

2. Install the required Python packages (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **OpenAI API key**. You can obtain one by signing up at [OpenAI's API](https://beta.openai.com/signup/).

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Using the App
1. **Open the app** in your browser (default URL: `http://localhost:8501`).
2. **Configure API key**: In the sidebar, input your OpenAI API key.
3. **Enter a topic** for research, such as "Space exploration" or "Climate change."
4. Click **"Generate Article"** to start the process.

The app will analyze the topic, generate insights and use cases, and collect relevant resources. The results will be displayed in the main content area.

## Code Structure

- **app.py**: Main application file with Streamlit UI and agent/task setup.
- **Agent Definitions**: Defines three agents to handle different tasks:
  - `researcher`: Conducts market research and analyzes AI advancements.
  - `generator`: Proposes relevant use cases for AI in the given industry.
  - `reporter`: Collects datasets and resources for the use cases on Kaggle, HuggingFace, and GitHub.
- **Tasks**: Specifies the objectives and expected outputs for each agent.
- **Crew and Process**: Uses `CrewAI` to manage agents and execute tasks sequentially.

## Dependencies


- crewai
- langchain-community
- streamlit
- openai


## Future Improvements
- Add file-saving functionality to export resource links.
- Enable selection of different research sources or custom datasets.
- Integrate additional GenAI tools for enhanced use case generation and dataset collection.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **OpenAI** for the API services.
- **LangChain and Streamlit** for the platform tools.
- **HuggingFace, Kaggle, and GitHub** for dataset resources.
```
