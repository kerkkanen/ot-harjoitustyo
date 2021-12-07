import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

COUNTRIES_FILENAME = os.getenv('COUNTRIES_FILENAME') or 'country_list_all.csv'
COUNTRIES_FILE_PATH = os.path.join(dirname, '..', 'data', COUNTRIES_FILENAME)

SCORE_FILENAME = os.getenv('SCORE_FILENAME') or 'highscores.csv'
SCORE_FILE_PATH = os.path.join(dirname, '..', 'data', SCORE_FILENAME)
