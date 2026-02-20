from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from researcher.tools.custom_tool import search_tool, advanced_search
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

@CrewBase
class Researcher():
    '''A researcher agent that can perform various research tasks using custom tools.'''
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['researcher'],
            tools = [advanced_search],
            verbose = True
        )
        
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['reporting_analyst'],
            tools = [advanced_search],
            verbose = True
        )
    
    @agent
    def executive_summary_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['executive_summary_analyst'],
            verbose = True
        )
    
    @agent
    def risk_assessment_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['risk_assessment_analyst'],
            tools = [search_tool],
            verbose = True
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config = self.tasks_config['research_task'],
            output_file = 'outputs/research_report.md'
        )
    
    @task
    def competitive_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_analysis_task'],
            output_file='outputs/competitive_analysis.md'
        )

    @task
    def executive_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['executive_summary_task'],
            output_file='outputs/executive_summary.md'
        )

    @task
    def risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment_task'],
            output_file='outputs/risk_assessment.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Researcher crew"""        
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
            )
        