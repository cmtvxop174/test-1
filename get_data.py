import requests as rqs 
from bs4 import BeautifulSoup

class site:

    def __init__(self, username, passwords):
        self.username = username
        self.passwords = password

        self.sites = ["https://www.twitter.com", "https://www.instagram.com"
    , "https://www.facebook", "https://wwww.ufc.org"]


    def get_site(self, num):
        try:
            text = ""
            if(num > len(sites)):
            raise ValueError("Invalid input")

            content = rqs.get(self.sites[num], auth=(self.username[num], self.password[num]))
            text += content.text

            return text



