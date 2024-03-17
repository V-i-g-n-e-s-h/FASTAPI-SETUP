import os
import json

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


if os.path.exists('.env'):
    load_dotenv('.env')


class Settings(BaseSettings):
    config: str = ""


settings = Settings()
assert settings.config, 'environment settings missing!'
config:dict = json.loads(settings.config)
