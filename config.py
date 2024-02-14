import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    API_HASH = os.environ.get("API_HASH", "")
    APP_ID = os.environ.get("APP_ID", "")

    