# Hierarchical Researcher

A multi-agent research workflow using CrewAI in **hierarchical mode**. A manager agent oversees the process, delegates tasks to specialized agents, and ensures quality control at each step.

## Features

- Manager agent delegates tasks and reviews outputs
- Specialized agents for research, analysis, summary, and risk assessment
- Supports task revision and quality control
- Outputs are saved to the `outputs/` folder

## How to Use

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file**  
   Add your API keys (e.g., Mistral, OpenAI, Tavily, etc.) to `.env`.

3. **Configure agents and tasks**  
   Edit `src/researcher/config/agents.yaml` and `src/researcher/config/tasks.yaml` as needed.

4. **Run the workflow**  
   ```
   python src/researcher/main.py
   ```

5. **View results**  
   Check the `outputs/` directory for generated reports.

