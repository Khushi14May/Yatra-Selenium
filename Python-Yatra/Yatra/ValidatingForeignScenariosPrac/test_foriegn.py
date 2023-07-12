import random
import time

import pytest
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from Locators import OnewayLocate
# from PageObjects.Oneway import Page
from datetime import date, timedelta

from TestCases.Base import BaseClass

print("sample test case started")

@pytest.mark.usefixtures('setup')
class Test_Home_Page:

    #getting data from user
    Ddate = date.today()+ timedelta(2)
    economy="Economy"
    adult=2
    child=1
    infant=1
    cheapflight="yes"
    #title="Non Stop Flights"|"Student Fare Offer"|"Armed Forces Offer"|"Senior Citizen Offer"
    flight = "Non Stop Flights"
    fare='no'
    flightName = 'no'
@pytest.mark.usefixtures('setup')
class Test_Home_Page(BaseClass):
    def test_One_way2(self):
        self.driver.get("https://flight.yatra.com/air-search-ui/int2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DXB&originCountry=AE&destination=AMD&destinationCountry=IN&flight_depart_date=17/06/2023&ADT=2&CHD=1&INF=2&class=Economy&source=fresco-home&unqvaldesktop=27042620603")
        time.sleep(35)
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        log=self.loggingDemo()
        log.info("Logs gets started")
        # hp = Page(self.driver)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH,"//div[@class='copyright js_copyright_hide']")).perform()
        fcout=len(self.driver.find_elements(By.XPATH,'//div[@class="pr tipsy mb-8 book-button"]/../../..'))
        log.info("total count of flights "+str(fcout))
        RNDB=random.randint(1,fcout)
        log.info("random no. genearted is: "+str(RNDB))
        flightName=self.driver.find_element(By.XPATH,'(//span[@class="text i-b"])['+str(RNDB)+']').text
        log.info("flightName: "+flightName)
        money=self.driver.find_element(By.XPATH,'(//p[@class="i-b"])['+str(RNDB)+']').text
        log.info("money: "+money)
        stop=self.driver.find_element(By.XPATH,'(//div[@class="pr tipsy mb-8 book-button"]/../../..)['+str(RNDB)+']//div[@class="content full-width"]//div[@class=" font-lightgrey fs-11 tipsy i-b"]').text
        log.info("stop: "+stop)
        bb=self.driver.find_element(By.XPATH, '(//div[@class="pr tipsy mb-8 book-button"])['+str(RNDB)+']//button')
        self.driver.execute_script("arguments[0].click();", bb)
        time.sleep(5)



# //div[@class="pr tipsy mb-8 book-button"]/../../..//span[@class="text i-b"] for flightname
# //p[@class="i-b"] money
# //span[@class="text i-b"]for flightname
#dropdown of more flights //div[@class="pr tipsy mb-8 book-button"]/../../..//span[@class='ytfi-angle-down v-aligm-m']
# //div[@class="content full-width show-more"]//input radio button path rountrip
# (//div[@class="content full-width"])[9]//div[@class=" font-lightgrey fs-11 tipsy i-b"] for stop of roundtrip
# ((//div[@class="pr tipsy mb-8 book-button"]/../../..)[1]//div[@class="content full-width"])[1]//div[@class=" font-lightgrey fs-11 tipsy i-b"]