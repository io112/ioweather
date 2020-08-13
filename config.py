from os import path
from yaml import load_all
import constants


def get_configuration_file():
    if not path.exists('config.yaml'):
        print('Создайте файл конфигурации')
        exit(500)
    f = open('config.yaml')
    config = f.read()
    f.close()

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper

    config = load_all(config, Loader=Loader)
    formatted_conf = {}
    for a in config:
        formatted_conf = a
    try:
        constants.api_key = formatted_conf['WEATHER_API_KEY']
        constants.api_lang = formatted_conf['WEATHER_API_LANG']
    except Exception:
        exit(500)
