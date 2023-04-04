from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.startups-list.com/'
class Data():
     
    def __init__(self, url) -> None:
        
        self.url = url
        self.soup = self.__get_all_html_info()
    
    def __get_all_html_info(self):
        
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'lxml')
        return soup
        
    def __collecc_all_cities(self):
        
        header = self.soup.find('header')
        cities = [city.text.strip() for city in header.find_all('a', href = True)]
        return cities
        
    def __collect_starups(self):
        
        startups= []
        body = self.soup.find('body', id='body')
        links = [link['href'] for link in body.find_all('a', href = True)][:-4]
        for link in links:
            html_link = requests.get(link).text
            soup_link = BeautifulSoup(html_link, 'lxml')
            wrap = soup_link.find('div' , id = 'wrap', class_= 'wrap')
            startup = [startup['data-name'] for startup in wrap.find_all('div', attrs={'data-name': True})]
            startups.append(startup)
        return startups
       
    def create_info_dict(self):
        
        cities = self.__collecc_all_cities()
        startup =  self.__collect_starups()
        parsing_dict = {}
        for city, startup in zip(cities, startup, strict = True):
            parsing_dict.setdefault(city, startup)
        return parsing_dict

            
def main(): 
         
    data = Data(URL)
    parsing_dict = data.create_info_dict()
    
    records = [(key, i) for key, value in parsing_dict.items() for i in value]
    parse_df = pd.DataFrame.from_records(records, columns = ["Countries", "Startups"])
    parse_df.to_csv('Parsing_data.csv')
    
if __name__ == '__main__':
    main()