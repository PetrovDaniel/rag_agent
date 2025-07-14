import os
import subprocess
from langchain.agents import Tool
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google(query: str) -> str:
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=5).execute()
        results = res.get("items", [])
        if not results:
            return "Ничего не найдено."

        snippets = []
        for item in results:
            title = item.get("title")
            snippet = item.get("snippet")
            link = item.get("link")
            snippets.append(f"{title}\n{snippet}\nИсточник: {link}")
        return "\n\n".join(snippets)

    except Exception as e:
        return f"Ошибка при поиске Google: {e}"

# def search_web(query: str) -> str:
#     results = []
#     with DDGS() as ddgs:
#         for r in ddgs.text(query, max_results=5):
#             title = r.get("title", "")
#             body = r.get("body", "")
#             href = r.get("href", "")
#             results.append(f"{title}\n{body}\nИсточник: {href}")
#     return "\n\n".join(results)

def run_shell(command: str) -> str:
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Shell error: {e.output.decode()}"
    except Exception as e:
        return f"Execution error: {str(e)}"

tools = [
    Tool(name="search_web", func=search_google, description="Используй для поиска свежей информации из интернета (новости, погода, события). Не подходит для вычислений или доступа к локальным файлам."),
    Tool(name="run_shell", func=run_shell, description="Выполняет команду в shell."),
]
