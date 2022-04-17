import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote




class BeautifulHelper():
    def get_page_content(self, output_file = True) -> str:
        """ Gets page content and returns it """
        page = requests.get(f'{self.website_url}{self.item}')
        soup = BeautifulSoup(page.content, 'html.parser')
        if output_file is True:
            with open('./Output/Output.txt', 'w+') as write_file:
                write_file.write(page.text)
        return soup
    def get_class_list(self, class_name: str) -> list:
        """ Gets all the ocurrences of a certain class in the page's content """
        soup = self.get_page_content()
        items = soup.find_all(class_=class_name)
        items = [item.get_text() for item in items]
        return items