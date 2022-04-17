# scrapping-prices
This is a project for scrapping prices from different places that sell tech
# Start virtual environment
```
python3 -m venv venv/
source venv/bin/activate
```
# Install the CLI
```
python -m pip install --editable .
```
# Example of usage
```
scrapping-prices --item "RTX 3060" --store "Alternate" --delay 5 --output "./Output/scrape.json"
```