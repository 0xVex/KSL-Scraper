import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class KSL:

    def __init__(self):

        path = '/Users/austinlee/chromedriver'
        self.driver = webdriver.Chrome(path)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = 'https://www.ksl.com/auto/'
        self.scraped_cars = []
       #print('Enter any search keywords')
        self.keyword = None
        print('What is your minimum mileage? (Please enter in increments of 10,000)')
        self.mileage_minimum = input()
        print('what is your maximum mileage? (Please enter in increments of 10,000)')
        self.mileage_maximum = input()
        print('What is your price minimum? (Please enter in increments of $1,000)\n'
              'Please do not include a dollar sign as the program will include one for you')
        self.price_minimum = input()
        print('What is your price maximum? (Please enter in increments of $1,000) \n'
              'Please do not include a dollar sign as the program will include one for you')
        self.price_maximum = input()


    def browse_ads(self):

        self.driver.get(self.url)
        time.sleep(5)

    def search_cars(self):

        keyword_field = self.driver.find_element_by_name('keyword')
        mileage_minimum = self.driver.find_element_by_id('searchFormMileageFrom')
        mileage_maximum = self.driver.find_element_by_id('searchFormMileageTo')
        price_minimum = self.driver.find_element_by_id('priceFrom')
        price_maximum = self.driver.find_element_by_id('priceTo')

        keyword_field.send_keys(self.keyword)
        #mileage_minimum.send_keys(mileage_minimum)
        #mileage_minimum.send_keys(self.price_maximum)
        #mileage_maximum.send_keys(mileage_maximum)
        #price_minimum.send_keys('$' + price_minimum)
        #price_maximum.send_keys('$' + price_maximum)
        keyword_field.send_keys(Keys.ENTER)

    def scrape_cars(self):
        try: containers = self.driver.find_elements_by_xpath(
            "//div[contains(@class,'listing js-listing')]")
        except NoSuchElementException:
            print('Could not find any element')

        else:
            for title in containers:
                car_name = title.find_element_by_class_name('title').text
                link = title.find_element_by_class_name('title').find_element_by_tag_name('a').get_attribute('href')
                #price = title.find_element_by_class_name('listing-detail-line price').text
                #mileage = title.find_element_by_class_name('listing-detail-line mileage').text
                #seller_location = title.find_element_by_class_name('listing-detail-line').text
                print(car_name)
                print(link)
                #print(price)
                #print(mileage)
                #print(seller_location)
                self.scraped_cars.append({"Car": car_name, "Link": link})

    def save_cars(self):
        sc = pd.DataFrame(self.scraped_cars)
        print('Your car search has been saved')
        sc.to_csv('KslCars.csv')
        self.driver.quit()

    def run(self):

        self.browse_ads()
        print('Enter the car you want to search for')
        self.keyword = input()
        self.search_cars()
        self.scrape_cars()
        self.save_cars()

if __name__ ==  "__main__":
    search = KSL()
    search.run()
