from beautiful_helper.BeautifulHelper import BeautifulHelper
import json
from datetime import datetime


with open('stores/config.json') as config:
    stores_conf = json.load(config)

class Alternate(BeautifulHelper):
    def __init__(self):
        self.name_class = stores_conf['Alternate']['name_class']
        self.price_class = stores_conf['Alternate']['price_class']
        self.website_url = stores_conf['Alternate']['url']
    def get_item_prices(self, item = None) -> list:
        self.item = item
        price_items = self.get_class_list(class_name = self.price_class)
        name_items = self.get_class_list(class_name = self.name_class)
        product_prices = [{"product_name" : name, "price" : price.strip('\n')} for name, price in zip(name_items, price_items)]
        measurement_timestamp = datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')
        measurement = [{"measurement_timestamp" : measurement_timestamp,
        "products" : product_prices}]
        return measurement