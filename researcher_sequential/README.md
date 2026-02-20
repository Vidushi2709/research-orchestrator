# Sequential Researcher

A simple multi-agent research workflow using CrewAI in **sequential mode**. Each agent completes its task one after another, passing results to the next agent for a streamlined, easy-to-follow research pipeline.

## Features

- Agents work in a fixed order (no parallelism or delegation)
- Each agent specializes in a specific research step
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
