import os
from dotenv import load_dotenv

load_dotenv()

class Data:
#получаем логин и пароль из файла env
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")