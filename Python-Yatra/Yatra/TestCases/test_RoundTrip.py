import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators import RoundtripLocate
from PageObjects.Roundtrip import PageR
from Utilities.ExcelFile import HomePageData

print("sample test case started")

@pytest.mark.usefixtures('setup')
class Test_Home_Page:

    @pytest.fixture(params=HomePageData.getTestData("RoundTrip"))
    def getData(self, request):
        return request.param

    @pytest.mark.roundtrip
    def test_RoundTrip(self,getData):
        global url, Ddate,Rdate, economy, adult, child, infant, cheapflight, flight, fare, flightName,flightName2,Depart,Returnp
        Depart = getData["Departure"]
        Returnp = getData["Return"]
        Ddate = getData["Ddate"]
        Rdate=getData["Rdate"]
        economy = getData["economy"]
        adult = getData["adult"]
        child = getData["child"]
        infant = getData["infant"]
        cheapflight = getData["cheapflight"]
        # title="Non Stop Flights"|"Student Fare Offer"|"Armed Forces Offer"|"Senior Citizen Offer"
        flight = getData["flight"]
        fare = getData["fare"]
        flightName = getData["flightName1"]
        flightName2 = getData["flightName2"]
        #-----------------------------------------------------------
        self.driver.get("https://www.yatra.com/")
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageR(self.driver)
        time.sleep(5)
        # el = self.driver.find_element(By.XPATH, "//a[text()='My Account']")
        # action = ActionChains(self.driver)
        # action.move_to_element_with_offset(el, 1, 1)
        # action.move_to_element(el)
        # time.sleep(4)
        # action.click()
        # action.perform()
        a = self.driver.find_element(By.NAME, "notification-frame-~10cb42c72")
        self.driver.switch_to.frame(a)
        self.driver.find_element(By.XPATH, "//a[@class='close']").click()
        time.sleep(1)
        self.driver.switch_to.parent_frame()
        time.sleep(1)
        hp.roundtrip(RoundtripLocate.Roundtripbutton())
        title = self.driver.title
        assert "Yatra.com" in title
        element1 = self.driver.find_element(By.XPATH, "// a[ @ title='One Way']")
        colour1 = element1.value_of_css_property('color')
        element2 = self.driver.find_element(By.XPATH, "// a[ @ title='Round Trip']")
        colour2 = element2.value_of_css_property('color')
        element3 = self.driver.find_element(By.XPATH, "// a[ @ title='Multicity']")
        colour3 = element3.value_of_css_property('color')
        assert colour1 == "rgba(102, 102, 102, 1)" and colour2 == "rgba(243, 79, 79, 1)" and colour3 == "rgba(102, 102, 102, 1)"

        hp.departFrom(RoundtripLocate.departfrom(),Depart)
        hp.goingTo(RoundtripLocate.goingTo(),Returnp)
        # Ddate.strftime("%d/%m/%Y")
        hp.departDate(RoundtripLocate.DepartDate(), Ddate)
        # Rdate.strftime("%d/%m/%Y")
        hp.returnDate(RoundtripLocate.ReturnDate(), Rdate)
        hp.dropdown(RoundtripLocate.dropdown())
        hp.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        time.sleep(2)
        hp.adult(adult, RoundtripLocate.minus(), RoundtripLocate.plus())
        time.sleep(2)
        hp.child(child, fare, RoundtripLocate.minus(), RoundtripLocate.plus())
        time.sleep(2)
        hp.infant(infant, fare, RoundtripLocate.minus(), RoundtripLocate.plus())
        time.sleep(2)
        hp.FlightClass(economy,fare)
        try:
            hp.fares(flight, fare)
        except:
            pass
        hp.searchflight(RoundtripLocate.searchbutton())
        url = self.driver.current_url
        print(url)

        self.driver.get(url)
        time.sleep(35)
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageR(self.driver)
        hp.scroll()
        try:
            t1 = hp.noFlights()
            if "Sorry, There were no flights" in t1:
                self.driver.back()
                time.sleep(3)


        except:
            if flightName != "no" and flightName2 != "no":
                print("flight block in test")
                hp.fcount(RoundtripLocate.radio1(), RoundtripLocate.radio2(), fare, RoundtripLocate.Tfare())
                hp.flightChoice(RoundtripLocate.FlightChoice1(), RoundtripLocate.FlightChoice2(),
                                RoundtripLocate.Tfare(), fare, RoundtripLocate.Flight(), flightName,
                                flightName2, RoundtripLocate.radio1(), RoundtripLocate.radio2(),
                                RoundtripLocate.flight(), RoundtripLocate.TotalFare(), RoundtripLocate.stop(),
                                RoundtripLocate.booknow(),cheapflight)
                time.sleep(10)

            else:
                print("random block in test")
                hp.fcount(RoundtripLocate.radio1(), RoundtripLocate.radio2(), fare, RoundtripLocate.Tfare())
                hp.randomdiv(RoundtripLocate.radio1(), RoundtripLocate.radio2(), RoundtripLocate.flight(),
                             RoundtripLocate.TotalFare(), RoundtripLocate.stop(), RoundtripLocate.booknow(), fare,
                             RoundtripLocate.Tfare(),cheapflight)
                time.sleep(10)
            try:
                check=self.driver.find_element(By.XPATH,"//h3[text()='Fare Options']").is_displayed()
                if check == True:
                    self.driver.find_element(By.XPATH,"// span[text() = 'Basic Fare'] /../../.// button").click()
                    time.sleep(3)
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        self.driver.find_element(By.CLASS_NAME, "button primary rounded pull-right").click()
                        time.sleep(1)
                    hp.paymentpage(RoundtripLocate.BufferFlight(), RoundtripLocate.topay(), RoundtripLocate.total())
                except:
                    pass
                hp.paymentpage(RoundtripLocate.BufferFlight(), RoundtripLocate.topay(), RoundtripLocate.total())
            except:
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        self.driver.find_element(By.CLASS_NAME, "button primary rounded pull-right").click()
                        time.sleep(1)
                    hp.paymentpage(RoundtripLocate.BufferFlight(), RoundtripLocate.topay(), RoundtripLocate.total())
                except:
                    pass
                hp.paymentpage(RoundtripLocate.BufferFlight(), RoundtripLocate.topay(), RoundtripLocate.total())


#//h3[text()='Fare Options']
# //span[text()='Basic Fare']/../.././/button