import json

api_key = ''
api_address = 'https://api.openweathermap.org/data/2.5/'
api_lang = 'ru'
api_endpoints = {'daily_forecast': 'forecast'}


class ForecastResult:
    warm_recommendation = 'На улице тепло, можно смело надевать шорты'
    neutral_recommendation = 'На улице прохладно, наденьте легкую куртку'
    cold_recommendation = 'На улице холодно, оденьтесь потеплее'
    rain_recommendation = 'Скоро будет дождь, не забудьте зонт'

    city = ''
    weather_recommendations = ''
    weather = ''
    now_temp = ''
    now_desc = ''
    now_icon = ''
    icon1 = ''
    temp1 = ''
    time1 = ''
    desc1 = ''
    icon2 = ''
    temp2 = ''
    time2 = ''
    desc2 = ''

    def __init__(self, resp_data):
        resp_data = json.loads(resp_data)
        self.city = resp_data['city']['name']
        self.weather_recommendations = self.warm_recommendation
        self.now_icon = resp_data['list'][0]["weather"][0]["icon"]
        self.icon1 = resp_data['list'][1]["weather"][0]["icon"]
        self.icon2 = resp_data['list'][2]["weather"][0]["icon"]
        self.now_temp = resp_data['list'][0]["main"]["temp"]
        self.temp1 = resp_data['list'][1]["main"]["temp"]
        self.temp2 = resp_data['list'][2]["main"]["temp"]
        self.now_desc = resp_data['list'][0]["weather"][0]["description"]
        self.desc1 = resp_data['list'][1]["weather"][0]["description"]
        self.desc2 = resp_data['list'][2]["weather"][0]["description"]
        self.time1 = resp_data['list'][1]["dt_txt"][-8:-3]
        self.time2 = resp_data['list'][2]["dt_txt"][-8:-3]
        self.get_forecast(resp_data)

    def get_data(self):
        data = {'city': self.city,
                'weather_recommendations': self.weather_recommendations,
                'now_temp': self.now_temp,
                'now_desc': self.now_desc,
                'now_icon': self.now_icon,
                'temp1': self.temp1,
                'time1': self.time1,
                'desc1': self.desc1,
                'icon1': self.icon1,
                'temp2': self.temp1,
                'time2': self.time2,
                'desc2': self.desc2,
                'icon2': self.icon2,
                'weather': self.weather}
        return data

    def get_forecast(self, data):
        temp = data['list'][0]["main"]["temp"]
        weather = data['list'][0]["weather"][0]["main"]
        if weather == 'Rain':
            self.weather = 'rain'
            self.weather_recommendations = self.rain_recommendation
        elif temp < 5:
            self.weather = 'cold'
            self.weather_recommendations = self.cold_recommendation
        elif temp < 15:
            self.weather = 'neutral'
            self.weather_recommendations = self.neutral_recommendation
        else:
            self.weather = 'warm'
            self.weather_recommendations = self.warm_recommendation
