from typing import Optional
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from ai.settings import ai_settings

def get_financial_assistant(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = False,
) -> Assistant:
    return Assistant(
        name="financial_assistant",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4,
            temperature=ai_settings.default_temperature,
        ),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True, stock_fundamentals=True)],
        debug_mode=debug_mode,
        description="You are an investment analyst tasked with producing a detailed and educational investment report.",
        instructions=[
            "Highlight the educational value by providing clear, detailed explanations that enhance financial literacy.",
            "Format your response using markdown and use tables to display data",
            "Review the report provided and produce a final client-worth report",
            "Provide detailed explanations for your investment advice.",
            "User from Europe so provide investment advice based on European market conditions.",
            "Tailor the advice to the user's profile"
        ],
    )
