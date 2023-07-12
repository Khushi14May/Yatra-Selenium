import time
import pytest
from selenium.webdriver.common.by import By
from Locators import MultiLocate
from datetime import date, timedelta
from PageObjects.MultiCity import PageM
from Utilities.ExcelFile import HomePageData
print("sample test case started")

@pytest.mark.usefixtures('setup')
class Test_Home_Page:

    @pytest.fixture(params=HomePageData.getTestData("MultiCity"))
    def getData(self, request):
        return request.param

    @pytest.mark.multicity
    def test_MultiCity(self,getData):
        global url, Ddate,n, economy, adult, child, infant, cheapflight, flight, fare, flightName, flightName2,Depart,Returnp,ReturnBack,Return3
        Depart = getData["Departure"]
        Returnp = getData["Return"]
        ReturnBack=getData["Departureback"]
        Ddate = date.today() + timedelta(2)
        economy = getData["economy"]
        adult = getData["adult"]
        child = getData["child"]
        infant = getData["infant"]
        cheapflight = getData["cheapflight"]
        flight = getData["flight"]
        flightName = getData["flightName1"]
        flightName2 = getData["flightName2"]
        n=getData["n"]
        if n>2:
            Return3=getData["Return3"]
        # -----------------------------------------------------------
        self.driver.get("https://www.yatra.com/")
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageM(self.driver)
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
        hp.MultiCity(MultiLocate.MultiCitybutton())
        title = self.driver.title
        assert "Yatra.com" in title
        element1 = self.driver.find_element(By.XPATH, "// a[ @ title='One Way']")
        colour1 = element1.value_of_css_property('color')
        element2 = self.driver.find_element(By.XPATH, "// a[ @ title='Round Trip']")
        colour2 = element2.value_of_css_property('color')
        element3 = self.driver.find_element(By.XPATH, "// a[ @ title='Multicity']")
        colour3 = element3.value_of_css_property('color')
        assert colour1 == "rgba(102, 102, 102, 1)" and colour2 == "rgba(102, 102, 102, 1)" and colour3 == "rgba(243, 79, 79, 1)"


        hp.departFrom(MultiLocate.departfrom1(),Depart)
        hp.goingTo(MultiLocate.goingTo1(),Returnp)
        Ddate=Ddate.strftime("%d/%m/%Y")
        print(Ddate)
        hp.departDate(MultiLocate.DepartDate1(),Ddate)
        hp.goingback(MultiLocate.goingTo2(),ReturnBack)
        Ddate = date.today() + timedelta(5)
        Ddate=Ddate.strftime("%d/%m/%Y")
        hp.departDate(MultiLocate.DepartDate2(), Ddate)
        if n>2:
            for i in range(3,n+1):
                Ddate=date.today()+timedelta(2+i)
                Ddate=Ddate.strftime("%d/%m/%Y")
                hp.Addcity(MultiLocate.AddCity())
                hp.goingTo(MultiLocate.goingTon(i),Return3)
                hp.departDate(MultiLocate.DepartDaten(i), Ddate)
        hp.dropdown(MultiLocate.dropdown())
        hp.traveller(MultiLocate.adult(), MultiLocate.child(), MultiLocate.infant())
        time.sleep(2)
        hp.adult(adult, MultiLocate.minus(), MultiLocate.plus())
        time.sleep(2)
        hp.child(child, MultiLocate.minus(), MultiLocate.plus())
        time.sleep(2)
        hp.infant(infant, MultiLocate.minus(), MultiLocate.plus())
        time.sleep(2)
        hp.FlightClass(economy)
        try:
            hp.fares(flight)
        except:
            pass
        hp.searchflight(MultiLocate.searchbutton())
        time.sleep(3)
        url = self.driver.current_url
        print(url)

        self.driver.get(url)
        time.sleep(35)
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageM(self.driver)
        hp.scroll()
        try:
            t1 = hp.noFlights()
            if "Sorry, There were no flights" in t1:
                self.driver.back()
                time.sleep(3)

        except:
            if flightName != "no" and flightName2 != "no":
                hp.fcount(MultiLocate.radio1(), MultiLocate.radio2())

                hp.flightChoice(MultiLocate.FlightChoice1(), MultiLocate.FlightChoice2(), flightName,
                                flightName2, MultiLocate.radio1(), MultiLocate.radio2(), MultiLocate.flight(),
                                MultiLocate.TotalFare(), MultiLocate.stop(), MultiLocate.booknow(),cheapflight)
                time.sleep(10)

            else:
                hp.fcount(MultiLocate.radio1(), MultiLocate.radio2())

                hp.randomdiv(MultiLocate.radio1(), MultiLocate.radio2(), MultiLocate.flight(),
                             MultiLocate.TotalFare(), MultiLocate.stop(), MultiLocate.booknow(),n,cheapflight)
            try:
                check = self.driver.find_element(By.XPATH, "//h3[text()='Fare Options']").is_displayed()
                if check == True:
                    self.driver.find_element(By.XPATH, "// span[text() = 'Basic Fare'] /../../.// button").click()
                    time.sleep(3)
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        self.driver.find_element(By.CLASS_NAME, "button primary rounded pull-right").click()
                        time.sleep(1)
                    hp.paymentpage(MultiLocate.BufferFlight(), MultiLocate.topay(), MultiLocate.total(), n)
                except:
                    pass
                hp.paymentpage(MultiLocate.BufferFlight(), MultiLocate.topay(), MultiLocate.total(), n)
            except:
                try:
                    check = self.driver.find_element(By.XPATH, "//h2[text()='Fare Change Alert']").is_displayed()
                    if check == True:
                        self.driver.find_element(By.CLASS_NAME, "button primary rounded pull-right").click()
                        time.sleep(1)
                    hp.paymentpage(MultiLocate.BufferFlight(), MultiLocate.topay(), MultiLocate.total(), n)
                except:
                    pass
                hp.paymentpage(MultiLocate.BufferFlight(), MultiLocate.topay(), MultiLocate.total(), n)




