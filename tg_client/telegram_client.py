import environ

from telethon import TelegramClient


env = environ.Env()
environ.Env.read_env()

API_ID = env('TELEGRAM_API_ID')
API_HASH = env('TELEGRAM_API_HASH')
SESSION_NAME = env('TELEGRAM_SESSION_NAME')

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


def start_client():
    client.start()
    return client


client = start_client()
