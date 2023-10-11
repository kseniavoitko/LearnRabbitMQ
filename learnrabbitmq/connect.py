import os
from pathlib import Path
from mongoengine import connect
import configparser

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

db_client = connect(
    host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}", ssl=True
)
