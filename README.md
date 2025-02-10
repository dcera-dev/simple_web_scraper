# Web Scraper
A simple web-scraper that pulls raw html data from (https://quotes.toscrape.com), parses it, and displays the quotes.

Utilizes the BeautifulSoup4, requests, and os libraries.
Recommend running in a venv.

## Running
Create the virtual environment
<br />
`python -m venv env/`

Activate the virtual environment
<br />
`source /env/bin/activate`

Install Dependencies
<br />
`pip install bs4 requests`

Run the program
<br />
`python main.py`