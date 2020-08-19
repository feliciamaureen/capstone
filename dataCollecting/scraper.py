import requests
import pandas as pd
from bs4 import BeautifulSoup
from linkGen import linkGen

# send http request to a url
#make GET request to fetch raw html content
def linkHandling():
    links = linkGen()
    for i in links:
        html_content = requests.get(i).text
        print (html_content)
    return html_content

def scraper(html_content):
    #parse html content
    soup = BeautifulSoup(html_content, "lxml")

    #get the table class wikitable
    data = {}
    chart_table = soup.find("table", attrs={"class": "wikitable"})
    chart_table_data = chart_table.tbody.find_all("tr")  # contains 2 rows
    #print(chart_table_data)

    links = chart_table.findAll('a')
    #print(links)

    tableContents = []
    for link in links:
        tableContents.append(link.get('title'))

    return tableContents

def getArtists(tableContents):
    tableContents = scraper()
    artists = tableContents[1::2]
    return artists

def getTitles(tableContents):
    tableContents = scraper()
    titles = tableContents[::2]
    return titles

def chartDF(artists, titles):
    artists = getArtists()
    titles = getTitles()
    chart = pd.DataFrame()
    chart['artists'] = artists
    chart['songTitle'] = titles
    return chart

