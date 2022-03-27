from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import pandas as pd


class PropertyListing:
    def __init__(self, url):
        self.listing_url = url
        self.listed_price = None
        self.listed_potential_gross_revenue = None
        self.listed_walk_score = None
        self.number_of_units = None
        self.year_built = None

    def get_data(self):
        WEBDRIVER_PATH = 'drivers/msedgedriver.exe'
        edge_options = Options()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(WEBDRIVER_PATH)
        driver.get(self.listing_url)
        
        try:
            self.listed_price = driver.find_element_by_id('BuyPrice').text
        except:
            pass
        try:
            self.listed_potential_gross_revenue = driver.find_element_by_xpath("//*[contains(text(), 'Potential gross revenue')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.listed_walk_score = driver.find_element_by_class_name('walkscore').text
        except:
            pass
        try:
            self.number_of_units = driver.find_element_by_xpath("//*[@data-id='NbUniteFormatted']").text
        except:
            pass
        try:
            self.year_built = driver.find_element_by_xpath("//*[contains(text(), 'Year built')]/..").find_element_by_class_name('carac-value').text
        except:
            pass

    def to_dataframe(self):
        df = pd.DataFrame(self.__dict__, index=[0])
        return df
        
        
