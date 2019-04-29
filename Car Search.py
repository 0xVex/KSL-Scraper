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
        sc = pd.DataFrame(self.scrape_cars())
        print('Your car search has been saved')
        sc.to_csv('KslCars.csv')
        self.driver.quit()

    def run(self):

        self.browse_ads()
        while True:
            print('Enter the car you want to search for')
            self.keyword = input()
            if not self.keyword:
                break
            self.search_cars()
            self.scrape_cars()
        self.save_cars()

if __name__ ==  "__main__":
    search = KSL()
    search.run()








   # miles = ['0', '1,000', '5,000', '10,000', '20,000', '30,000', '40,000', '50,000', '60,000', '70,000', '80,000',
   #          '90,000', '100,000', '110,000', '120,000', '130,000', '140,000', '150,000', '160,000', '170,000',
    #         '180,000', '190,000', '200,000', '1,000,000']
   # price = ['$0', '$1000', '$2,000', '$3,000', '$4,000', '$5,000', '$6,000', '$7,000', '$8,000', '$9,000', '$10,000',
    #         '$11,000', '$12,000', '$13,000', '$14,000', '$15,000', '$16,000', '$17,000', '$18,000', '$19,000',
    #         '$20,000', '$21,000', '$22,000', '$23,000', '$24,000', '$25,000', '$26,000', '$27,000', '$28,000',
    #         '$29,000', '$30,000', '$31,000', '$32,000', '$33,000', '$34,000', '$35,000', '$36,000', '$37,000',
    #         '$38,000', '$39,000', '$40,000', '$41,000', '$42,000', '$43,000', '$44,000', '$45,000', '$46,000',
    #         '$47,000', '$48,000', '$49,000', '$50,000', '$51,000', '$52,000', '$53,000', '$54,000', '$55,000',
    #         '$56,000', '$57,000', '$58,000', '$59,000', '$60,000', '$61,000', '$62,000', '$63,000', '$64,000',
    #         '$65,000', '$66,000', '$67,000', '$68,000', '$69,000', '$70,000', '$71,000']

   # for desired_min_miles in miles:
    #    if desired_min_miles == self.mileage_minimum:
     #       print(desired_min_miles)
     #       break
    #    else:
   #         print('sorry looks like you might have entered a mile value that was not recognized.')





