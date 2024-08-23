from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city_name):
    api_key = "1235bbad91ec4f5a974154045242008"
    base_url = "http://api.weatherapi.com/v1/current.json?key="
    complete_url = base_url + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(complete_url)
    print(response)
    
    if response.status_code != 200:
        return {"error": "Unable to fetch data."}
    
    return response.json()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    print(weather_data)
    if 'error' in weather_data:  # Check if there's an error
        return render_template('index.html', error=weather_data['error'])
    
    return render_template('weather.html', weather=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
