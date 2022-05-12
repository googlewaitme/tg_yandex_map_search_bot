from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list("ADMINS")
YANDEX_TOKEN = env.str('YANDEX_TOKEN')
YANDEX_URL = 'https://search-maps.yandex.ru/v1/'

