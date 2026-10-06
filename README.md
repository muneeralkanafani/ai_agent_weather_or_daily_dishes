# AI Agent: Weather or Daily Dishes

A small multi-agent Python app. A keyword-based router sends each question to the
right agent:

- **WeatherAgent** — extracts the city, calls the OpenWeatherMap API (geocoding +
  current weather) and remembers the last temperature per city.
- **DailyDishAgent** — matches the question against a restaurant FAQ dataset using
  TF-IDF + cosine similarity (scikit-learn).

## Setup

1. **Get a free API key**
   - Create an account at https://openweathermap.org/api
   - Go to **API keys** and copy your key
   - Note: new keys can take up to ~10 minutes to activate

2. **Create the virtual environment and install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirments.txt
   ```

3. **Configure your API key**

   ```bash
   cp .env.example .env
   ```

   Open `.env` and paste your key:

   ```
   WEATHER_API_KEY=your_api_key_here
   ```

## Run

```bash
python main.py
```

## Sample output

```
Q: What's the weather in Paris?
A: The current weather in Paris is scattered clouds with a temperature of 20.93°C.

Q: Do you have vegetarian options?
A: Yes, we have several vegetarian and vegan options on our menu.

Q: Is it going to rain in London?
A: The current weather in London is overcast clouds with a temperature of 17.56°C.

Q: What are your opening hours?
A: We're open Monday-Thursday 11am-10pm, Friday-Saturday 11am-11pm, Sunday 10am-9pm.
```

Weather answers are live, so temperature and conditions change with every run.
