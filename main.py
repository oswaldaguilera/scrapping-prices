from stores.Alternate import Alternate
import time
import click
import json

@click.command()
@click.option('--store', default='Alternate', prompt='Store', help='Store to webscrape')
@click.option('--item', default='RTX 3060', prompt='Item', help='Item to look for')
@click.option('--delay', default=5, prompt='Delay', help='Delay between scraps')
@click.option('--output', default=None, prompt='Output', help='Output file')
def cli(store, item, delay, output):
    print("""-------------------------------------------------------------""")
    print("""--------------- STARTING WEBSCRAPPING PROCESS ---------------""")
    print("""-------------------------------------------------------------""")
    while True:
        alternate = Alternate()
        price_list = alternate.get_item_prices(item)
        for _item in price_list[0]["products"]:
            print(f'The item: {_item["product_name"]} is at {_item["price"]}')
        print("""-------------------------------------------------------------""")
        print("""-------------------------------------------------------------""")
        print("""-------------------------------------------------------------""")
        if output != None:
            with open(output, 'a') as outfile:
                for _item in price_list:
                    outfile.write('%s\n' % _item)
        time.sleep(delay)
    
if __name__ == "__main__":
    process()