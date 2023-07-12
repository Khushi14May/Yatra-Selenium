import time
import pytest
from selenium.webdriver.common.by import By
from Locators import OnewayLocate
from PageObjects.Oneway import Page
from Utilities.ExcelFile import HomePageData
import openpyxl
print("sample test case started")

@pytest.mark.usefixtures('setup')
class Test_Home_Page():

    @pytest.fixture(params=HomePageData.getTestData("OneWay"))
    def getData(self, request):
        return request.param

    @pytest.mark.oneway1
    def test_One_way(self,getData):
        Depart=getData["Departure"]
        Returnp=getData["Return"]
        Ddate = getData["Ddate"]
        economy = getData["economy"]
        adult = getData["adult"]
        child = getData["child"]
        infant = getData["infant"]
        cheapflight = getData["cheapflight"]
        # title="Non Stop Flights"|"Student Fare Offer"|"Armed Forces Offer"|"Senior Citizen Offer"
        flight = getData["flight"]
        fare = getData["fare"]
        flightName = getData["flightName1"]
      #--------------------------------------------------------------------------------
        self.driver.get("https://www.yatra.com/")
        self.driver.implicitly_wait(5)   #giving wait to all elements for 5secs.
        hp=Page(self.driver)
        time.sleep(5)
        # el=self.driver.find_element(By.XPATH,"//a[text()='My Account']")
        #
        # action = ActionChains(self.driver)
        # action.move_to_element_with_offset(el, 1, 1)
        # action.move_to_element(el)
        # time.sleep(4)
        # action.click()
        # action.perform()
        try:
            a = self.driver.find_element(By.NAME, "notification-frame-~10cb42c72")
            self.driver.switch_to.frame(a)
            self.driver.find_element(By.XPATH, "//a[@class='close']").click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            time.sleep(1)
        except:
            pass
        hp.oneway(OnewayLocate.onewaybutton())
        title=self.driver.title
        assert "Yatra.com" in title
        element1 = self.driver.find_element(By.XPATH,"// a[ @ title='One Way']")
        colour1=element1.value_of_css_property('color')
        element2 = self.driver.find_element(By.XPATH, "// a[ @ title='Round Trip']")
        colour2 = element2.value_of_css_property('color')
        element3 = self.driver.find_element(By.XPATH, "// a[ @ title='Multicity']")
        colour3 = element3.value_of_css_property('color')
        assert colour1=="rgba(243, 79, 79, 1)" and colour2 == "rgba(102, 102, 102, 1)" and colour3 == "rgba(102, 102, 102, 1)"

        hp.departFrom(OnewayLocate.departfrom(),Depart)
        hp.goingTo(OnewayLocate.goingTo(),Returnp)
        # Ddate.strftime("%d/%m/%Y")
        hp.departDate(OnewayLocate.DepartDate(),Ddate)
        hp.dropdown(OnewayLocate.dropdown())
        hp.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
        time.sleep(2)
        hp.adult(adult,OnewayLocate.minus(),OnewayLocate.plus())
        time.sleep(2)
        hp.child(child,fare,OnewayLocate.minus(),OnewayLocate.plus())
        time.sleep(2)
        hp.infant(infant,fare,OnewayLocate.minus(),OnewayLocate.plus())
        time.sleep(2)
        hp.FlightClass(economy,fare)
        try:
            hp.fares(flight,fare)
        except:
            pass
        element4 = self.driver.find_element(By.CSS_SELECTOR, "input[value = 'Search Flights']")
        colour4 = element4.value_of_css_property('background')
        assert "rgb(234, 35, 48)" in colour4
        hp.searchflight(OnewayLocate.searchbutton())
        time.sleep(3)
        url1=self.driver.current_url
        print(url1)
        print("sample test case successfully completed")

    # @pytest.mark.oneway
    # def test_One_way2(self):
        self.driver.get(url1)
        time.sleep(35)
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = Page(self.driver)
        hp.scroll()
        try:
            t1 = hp.noFlights()
            if "Sorry, There were no flights" in t1:
                self.driver.back()
                time.sleep(3)

        except:
            if flightName != "no":
                hp.fcount(OnewayLocate.flightcount(), fare, OnewayLocate.fare())
                hp.flightChoice(flightName, OnewayLocate.flightcount(), OnewayLocate.flightname(), OnewayLocate.stop(),
                                OnewayLocate.button(), OnewayLocate.book(), OnewayLocate.money(), OnewayLocate.money2(),
                                fare, OnewayLocate.fare(), cheapflight)
                time.sleep(10)

            else:
                hp.fcount(OnewayLocate.flightcount(), fare, OnewayLocate.fare())
                hp.randomdiv(OnewayLocate.stop(), OnewayLocate.flightname(), OnewayLocate.button(), OnewayLocate.book(),
                             OnewayLocate.money(), OnewayLocate.money2(), fare, OnewayLocate.fare(), cheapflight)
                time.sleep(10)
            try:
                check = self.driver.find_element(By.XPATH, "//h3[text()='Fare Options']").is_displayed()
                if check == True:
                    self.driver.find_element(By.XPATH, "// span[text() = 'Basic Fare'] /../../.// button").click()
                    time.sleep(3)
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        try:
                            self.driver.find_element(By.XPATH, "//button[@ng-click='continueSameFlight()']").click()
                        except:
                            self.driver.find_element(By.XPATH, "//button[@ng-click='continueSameFlight();']").click()
                        time.sleep(1)
                except:
                    pass
                hp.paymentpage(OnewayLocate.BufferFlight(), OnewayLocate.topay(), OnewayLocate.total())
            except:
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        try:
                            self.driver.find_element(By.XPATH, "//button[@ng-click='continueSameFlight()']").click()
                        except:
                            self.driver.find_element(By.XPATH, "//button[@ng-click='continueSameFlight();']").click()
                        time.sleep(1)
                except:
                    pass
                hp.paymentpage(OnewayLocate.BufferFlight(), OnewayLocate.topay(), OnewayLocate.total())
