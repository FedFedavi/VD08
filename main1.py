from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index.html', weather=weather, news=news)

def get_weather(city):
    api_key = '4b6f9c76121e00d35e763e413fdbbaff'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = '551261f5d0e64c95a413b8d5c37f1018'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)
