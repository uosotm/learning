import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

load_dotenv(dotenv_path, verbose=True)

OWM_API_KEY = os.environ.get('OWM_API_KEY')
OER_API_KEY = os.environ.get('OER_API_KEY')
