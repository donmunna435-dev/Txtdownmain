import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8266282399:AAHQapxFlhTrl0nd_zr5CfnOLCnqxNaBlYs")
    API_ID = int(os.environ.get("API_ID", "24754824"))
    API_HASH = os.environ.get("API_HASH", "e24a9c7a6aa24e1c56fa349e104ec20e")
    AUTH_USER = os.environ.get('AUTH_USERS', '968292174').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "〖ᴷⁱⁿg ADII REALUSER"#Here You Can Change with Your Name  or any custom name or title you prefer
