from agents.weather_agent import WeatherAgent
from agents.daily_dish_agent import DailyDishAgent

class AgentRouter:
    def __init__(self, weather_agent, daily_dish_agent):
        self.weather_agent = weather_agent
        self.daily_dish_agent = daily_dish_agent
        self.weather_keywords = [
            "weather", "temperature", "forecast",
            "rain", "sunny", "climate", "humidity",
            "hot", "cold", "warm"
        ]
        self.restaurant_keywords = [
            "menu", "food", "reservation", "hours",
            "restaurant", "dish", "dining"
        ]

    def route(self, query):
        """Route the user query to the appropriate agent"""
        query_lower = query.lower()
        scores = {"weather": 0, "daily_dish": 0}

        # Calculate weather score
        for keyword in self.weather_keywords:
            if keyword in query_lower:
                scores["weather"] += 1
        # Calculate restaurant score
        for keyword in self.restaurant_keywords:
            if keyword in query_lower:
                scores["daily_dish"] += 1

        # Return agent with highest score
        if scores["weather"] > scores["daily_dish"]:
            return "weather", scores["weather"]
        else:
            return "daily_dish", scores["daily_dish"]

    def answer(self, query):
        """return the answer based on the agent that agent route choose"""
        try:
            route, confidence = self.route(query)
            if route == "weather":
                response = self.weather_agent.answer(query)
            else:
                response = self.daily_dish_agent.answer(query)

            # Check if response is valid
            if not response or response.startswith("Error"):
                return self.fallback_response(query)
            return response
        
        except Exception as e:
            return f"I encountered an issue: {str(e)}. Please try again."
        
    def fallback_response(self, query):
        return (
            "I'm having trouble answering that right now. "
            "Please try rephrasing your question or contact us directly."
        )
