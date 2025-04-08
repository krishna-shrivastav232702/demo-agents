from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role="search the web for information",
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)


finance_agent = Agent(
    name="Financial Agent",
    role="Get Financial data",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include sources","Use tables to display data"],
    markdown=True,
    show_tool_calls=True
)

agent_team.print_response("Analyze Companies like Tesla , Nvidia  and suggest which to buy in long term")