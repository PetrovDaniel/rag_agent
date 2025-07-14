from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from tools import tools

llm = OllamaLLM(model="llama3:8b", base_url="http://ollama:11434")  # или другое имя, если ты загрузил с другим названием

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
