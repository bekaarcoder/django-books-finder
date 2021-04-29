import requests
from bs4 import BeautifulSoup as bs4

url = "http://library.lol/main/9CFDEA9DB6487E4FE74BF9921D5E5B3F"


def run():
    res = requests.get(url)
    soup = bs4(res.text, "html.parser")

    image_src = soup.find("img").get("src")
    print(f"http://{res.url[7:].split('/')[0]}{image_src}")
