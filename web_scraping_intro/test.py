from bs4 import BeautifulSoup
import requests

bball_text = requests.get('https://www.basketball-reference.com/leagues/NBA_2019.html').text #accesses website with .get(), put string with url, .text accesses the html text from the site
cleaned_text = BeautifulSoup(bball_text, 'lxml') #uses lxml parser on the html text from the website
conference_table = cleaned_text.find_all('table', id='confs_standings_E')

for i in conference_table:
    b = i.find_all('a')
    for q in b:
        #print(q) #.replace(' ', '')) replace replaces a specified part of the text with whatever text is specified, in this instance spaces are removed
        new_request = requests.get(q['href']).text #brackets access an attribute of an element, here it is accessing the href attribute in each a element
        print(new_request)
        