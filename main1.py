from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quotes = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        quotes = get_quotes()
    return render_template('index.html', weather=weather, news=news, quotes=quotes)

def get_weather(city):
    api_key = '4b6f9c76121e00d35e763e413fdbbaff'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Weather API error: {e}")
        return None

def get_news():
    api_key = '551261f5d0e64c95a413b8d5c37f1018'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json().get('articles', [])
    except requests.exceptions.RequestException as e:
        print(f"News API error: {e}")
        return []

def get_quotes():
    category = 'happiness'
    api_key = '1pCtUYndfxO+DB2hqCmgLA==6CiN7FnLMvjzH5D7'
    url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    try:
        response = requests.get(url, headers={'X-Api-Key': f'{api_key}'}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Quotes API error: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
