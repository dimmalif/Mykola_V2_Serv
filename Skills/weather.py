import requests


class Weather:
    def __init__(self, city, text_data=None):
        self.city = city

        self.h = None

        self.parameters = {
            "lang": "ua",
            "q": self.city,
            "appid": "84061a2a5ff54b490d63bd38d557b06d",
            "units": "metric"
            }

    def get_json(self, time):
        match time:
            case 'now':
                now = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=self.parameters)
                return now
            case 'for day':
                f_day = requests.get('http://api.openweathermap.org/data/2.5/forecast?', params=self.parameters)
                return f_day

    @staticmethod
    def set_weather(data):
        dt = data.get('dt_txt')
        weather = data.get("weather")[0].get("description")
        temp = data.get("main").get("temp")
        hum = data.get("main").get("humidity")
        w_speed = data.get("wind").get("speed")

        if dt is None:
            dt = 'Зараз'

        return {'Дата, час': dt,
                'Погода': weather,
                'Температура': f'{temp}°C',
                'Вологість': f'{hum}%',
                'Швидкість вітру': f'{w_speed}м/с'}

    def get_weather(self, time):
        weather = []

        match time:
            case 'now':
                data = self.get_json(time).json()
                weather.append(self.set_weather(data))
                return weather
            case 'for day':
                data = self.get_json(time).json().get('list')[:5]
                for h in data:
                    weather.append(self.set_weather(h))
                return weather

    @staticmethod
    def formater(data):
        result = ''
        for d in data:
            for key, value in d.items():
                result += f"{key}: {value}\n"
                if key == 'Швидкість вітру':
                    result += '\n'
        return result
