import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("LAMBDA_URI")

def getData():
    response = requests.request("GET", url)
    print(response.text)
getData()

