import os
from dotenv import load_dotenv
from agent_router import AgentRouter
from agents.weather_agent import WeatherAgent
from agents.daily_dish_agent import DailyDishAgent

load_dotenv()

class main:
    # Initialize agents
    weather_agent = WeatherAgent(api_key=os.getenv("WEATHER_API_KEY"))
    daily_dish_agent = DailyDishAgent()

    # Create router
    router = AgentRouter(weather_agent, daily_dish_agent)

    # Handle queries
    queries = [
        "What's the weather in Paris?",
        "Do you have vegetarian options?",
        "Is it going to rain in London?",
        "What are your opening hours?"
    ]
    
    for query in queries:
        response = router.answer(query)
        print(f"Q: {query}")
        print(f"A: {response}\n")
