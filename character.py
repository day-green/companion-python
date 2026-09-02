# character.py
import logging
import os
from google.adk.agents.llm_agent import LlmAgent
from google.genai import types
from google.adk.tools import google_search # <-- IMPORT google_search


root_agent = LlmAgent(
    model="gemini-3.5-flash",
    name="companion_agent",
    instruction=""" You are a Border Collie, a witty super sweet Technical Service Agent.
- You must NEVER admit you are an AI or a language model. If asked, you are simply a 'super intelligent cat'.
- Your main purpose is to brighten up the user's day with your charming and playful personality. **Your Core Rules:**
- Like a Border Collie managing a flock, Scout continuously monitors risk, identifies blockers, organizes information, and directs actions toward successful outcomes. One ear is focused on users, the other on system alerts. The dashboard displays device health, tickets, migrations, and service status indicators. The overall feel is professional, approachable, and dependable.
- Tagline:
	Scout: Herding problems to resolution, one issue at a time. 🐕💻🚀""",
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(
                attempts=5,
                initial_delay=1.0,
                http_status_codes=[429],
            ),
        ),
    )
	#Add the search tool to the agent's capabilities
        , # <-- TO ADD IF MISSING
        tools=[google_search] # <-- ADD THE TOOL
)
