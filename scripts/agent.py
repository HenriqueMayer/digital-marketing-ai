import os
from pathlib import Path
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground, serve_playground_app

ROOT_DIR = Path(__file__).parent.parent

from transcription_reader import get_creator_transcriptions, list_available_creators
from dotenv import load_dotenv

load_dotenv()

prompt_path = ROOT_DIR / "prompts" / "copywriter.md"

db_path = ROOT_DIR / "tmp" / "storage.db"
db_path.parent.mkdir(exist_ok=True)

copywriter = Agent(
    model=Groq(id="llama3-70b-8192"),
    name="copywriter",
    add_history_to_messages=True,
    num_history_responses=10,
    storage=SqliteStorage(table_name="agent_sessions", db_file=str(db_path)),
    tools=[TavilyTools(), list_available_creators, get_creator_transcriptions],
    show_tool_calls=True,
    instructions=open(prompt_path).read(),
    markdown=True,
)

playground = Playground(agents=[copywriter])

if __name__ == "__main__":
    serve_playground_app(playground.get_app(), port=7777)
