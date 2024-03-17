from fastapi import FastAPI

from config import config


app = FastAPI(title="__PROJECT_NAME__")

from router import middleware
