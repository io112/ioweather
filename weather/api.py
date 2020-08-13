import constants
import requests


def request_api(endpoint, data):
    result = requests.get(constants.api_address + endpoint, params=data)
    return result


def daily_forecast(country, region, city):
    req_data = {'q': f'{city},{region},{country}',
                'units': 'metric',
                'cnt': '3',
                'lang': constants.api_lang,
                'APPID': constants.api_key}

    result = request_api(constants.api_endpoints['daily_forecast'], req_data)
    result = constants.ForecastResult(result.content)

    return result
