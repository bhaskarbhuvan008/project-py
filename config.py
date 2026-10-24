import os
from urllib import parse
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    db = os.environ["DB_NAME"]

    url = f"mysql+mysqlconnector://{user}:{parse.quote(password)}@{host}/{db}"
    return create_engine(url)

