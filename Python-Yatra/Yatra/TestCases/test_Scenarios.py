import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import OnewayLocate
from PageObjects.Oneway import Page
from Locators import MultiLocate
from datetime import date, timedelta
from PageObjects.MultiCity import PageM
from Locators import RoundtripLocate
from PageObjects.Roundtrip import PageR
print("sample test case started")

@pytest.mark.usefixtures('setup')
class Test_Page:

    def __init__(self):
        driver = webdriver.Chrome()
        self.driver = driver

    def data(self,data):
        global Depart, Ddate, Rdate, n, economy, adult, child, infant, cheapflight, flight, fare, flightName, Returnp, ReturnBack, flightName2, n, ReturnN, Ddate
        Depart = data["Departure"]
        Returnp = data["Return"]
        Returnp = data["Return"]
        ReturnBack = data["Departureback"]
        Ddate = data["Ddate"]
        economy = data["economy"]
        adult = data["adult"]
        child = data["child"]
        infant = data["infant"]
        cheapflight = data["cheapflight"]
        flight = data["flight"]
        fare = data["fare"]
        flightName = data["flightName1"]
        flightName2 = data["flightName2"]
        n = data["n"]
        ReturnN = data["Return3"]
    @pytest.mark.oneway1
    def test_OneWay(self,exdata):
        self.data(exdata)
      #--------------------------------------------------------------------------------
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)   #giving wait to all elements for 5secs.
        hp=Page(self.driver)
        time.sleep(5)
        self.popup()
        hp.oneway(OnewayLocate.onewaybutton())
        title=self.driver.title
        assert "Yatra.com" in title
        self.verify()
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
        self.driver.close()
# --------------------------------------------------------------------------
    def test_MultiCity(self,exdata):
        global Return3
        self.data(exdata)
        DdateM = date.today() + timedelta(2)
        if n>2:
            Return3=ReturnN
        # -----------------------------------------------------------
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageM(self.driver)
        time.sleep(5)
        self.popup()
        hp.MultiCity(MultiLocate.MultiCitybutton())
        title = self.driver.title
        assert "Yatra.com" in title
        self.verify()
        assert colour1 == "rgba(102, 102, 102, 1)" and colour2 == "rgba(102, 102, 102, 1)" and colour3 == "rgba(243, 79, 79, 1)"

        hp.departFrom(MultiLocate.departfrom1(),Depart)
        hp.goingTo(MultiLocate.goingTo1(),Returnp)
        DdateM=DdateM.strftime("%d/%m/%Y")
        print(DdateM)
        hp.departDate(MultiLocate.DepartDate1(),DdateM)
        hp.goingback(MultiLocate.goingTo2(),ReturnBack)
        DdateM = date.today() + timedelta(5)
        DdateM=DdateM.strftime("%d/%m/%Y")
        hp.departDate(MultiLocate.DepartDate2(), DdateM)
        if n>2:
            for i in range(3,n+1):
                DdateM=date.today()+timedelta(2+i)
                DdateM=DdateM.strftime("%d/%m/%Y")
                hp.Addcity(MultiLocate.AddCity())
                hp.goingTo(MultiLocate.goingTon(i),Return3)
                hp.departDate(MultiLocate.DepartDaten(i), DdateM)
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
        print("sample test case successfully completed")

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
        self.driver.close()
    @pytest.mark.roundtrip
    def test_RoundTrip(self, exdata):
        self.data(exdata)
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # giving wait to all elements for 5secs.
        hp = PageR(self.driver)
        time.sleep(5)
        self.popup()
        hp.roundtrip(RoundtripLocate.Roundtripbutton())
        title = self.driver.title
        assert "Yatra.com" in title
        self.verify()
        assert colour1 == "rgba(102, 102, 102, 1)" and colour2 == "rgba(243, 79, 79, 1)" and colour3 == "rgba(102, 102, 102, 1)"

        hp.departFrom(RoundtripLocate.departfrom(), Depart)
        hp.goingTo(RoundtripLocate.goingTo(), Returnp)
        hp.departDate(RoundtripLocate.DepartDate(), Ddate)
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
        hp.FlightClass(economy, fare)
        try:
            hp.fares(flight, fare)
        except:
            pass
        hp.searchflight(RoundtripLocate.searchbutton())
        url = self.driver.current_url
        print(url)
        print("sample test case successfully completed")

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
                                RoundtripLocate.booknow(), cheapflight)
                time.sleep(10)

            else:
                print("random block in test")
                hp.fcount(RoundtripLocate.radio1(), RoundtripLocate.radio2(), fare, RoundtripLocate.Tfare())
                hp.randomdiv(RoundtripLocate.radio1(), RoundtripLocate.radio2(), RoundtripLocate.flight(),
                             RoundtripLocate.TotalFare(), RoundtripLocate.stop(), RoundtripLocate.booknow(), fare,
                             RoundtripLocate.Tfare(), cheapflight)
                time.sleep(10)
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
        self.driver.close()

    def popup(self):
        try:
            a = self.driver.find_element(By.NAME, "notification-frame-~10cb42c72")
            self.driver.switch_to.frame(a)
            self.driver.find_element(By.XPATH, "//a[@class='close']").click()
            time.sleep(1)
            self.driver.switch_to.parent_frame()
            time.sleep(1)
        except:
            pass
    def verify(self):
        global colour1,colour2,colour3
        element1 = self.driver.find_element(By.XPATH, "// a[ @ title='One Way']")
        colour1 = element1.value_of_css_property('color')
        element2 = self.driver.find_element(By.XPATH, "// a[ @ title='Round Trip']")
        colour2 = element2.value_of_css_property('color')
        element3 = self.driver.find_element(By.XPATH, "// a[ @ title='Multicity']")
        colour3 = element3.value_of_css_property('color')