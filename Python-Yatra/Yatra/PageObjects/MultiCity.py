import random
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
from TestCases.Base import BaseClass
from Locators import MultiLocate


class PageM(BaseClass):
    def __init__(self, driver):
        global log
        self.driver = driver
        log = self.loggingDemo()

    def MultiCity(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def departFrom(self,xpath,city1):
        log.info("Departure: "+city1)
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,xpath).send_keys(city1)
        time.sleep(2)
        self.driver.find_element(By.XPATH,xpath).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        time.sleep(2)

    def goingTo(self,ID,city1):
        log.info("Return: "+city1)
        self.driver.find_element(By.XPATH,ID).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,ID).send_keys(city1)
        time.sleep(2)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.ENTER)

    def goingback(self,ID,city1):
        log.info("Going to another place: "+city1)
        self.driver.find_element(By.XPATH, ID).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ID).send_keys(city1)
        time.sleep(2)
        self.driver.find_element(By.XPATH, ID).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, ID).send_keys(Keys.ENTER)

    def departDate(self,xpath,Ddate):
        log.info("Departure Date: "+Ddate)
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "// td[ @id = '" +Ddate+ "' and @data-date='" +Ddate+"']").click()
        time.sleep(3)

    def Addcity(self,Text):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,Text).click()
        time.sleep(2)

    def dropdown(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(3)


    def FlightClass(self,economy):
        self.driver.find_element(By.XPATH, "//span[text()='" + economy + "']").click()
        time.sleep(2)

    def traveller(self, adult, child, infant):
        global adult1, child1, infant1, a, c, i
        a = self.driver.find_element(By.XPATH, adult)
        c = self.driver.find_element(By.XPATH, child)
        i = self.driver.find_element(By.XPATH, infant)
        adult1 = int(a.find_element(By.XPATH, "./..//span[@class='adultcount']").text)
        child1 = int(c.find_element(By.XPATH, "./..//span[@class='adultcount']").text)
        infant1 = int(i.find_element(By.XPATH, "./..//span[@class='adultcount']").text)

    def adult(self, adult, minus, plus):
        while adult1 != adult:
            if adult < adult1 and adult <= 9:
                # minus
                a.find_element(By.XPATH,"."+minus).click()
                self.traveller(MultiLocate.adult(), MultiLocate.child(), MultiLocate.infant())
            else:
                a.find_element(By.XPATH,"."+ plus).click()
                self.traveller(MultiLocate.adult(), MultiLocate.child(), MultiLocate.infant())
        self.traveller(MultiLocate.adult(),MultiLocate.child(), MultiLocate.infant())

    def child(self, child, minus, plus):
        while child1 != child and adult1 + child1 < 9:
            if child1 > child:
                c.find_element(By.XPATH,"."+minus).click()
            else:
                c.find_element(By.XPATH,"."+ plus).click()
            self.traveller(MultiLocate.adult(), MultiLocate.child(), MultiLocate.infant())
        self.traveller(MultiLocate.adult(), MultiLocate.child(), MultiLocate.infant())

    def infant(self, infant, minus, plus):
        while infant1 != infant and infant1 < adult1:
            if infant1 > infant:
                i.find_element(By.XPATH,"."+ minus).click()
            else:
                i.find_element(By.XPATH,"."+ plus).click()
            self.traveller(MultiLocate.adult(),MultiLocate.child(), MultiLocate.infant())

    def fares(self,flight):
        if flight != "no":
            self.driver.find_element(By.XPATH, "// a[ @ title = '" + flight + "']").click()
            time.sleep(2)

    def searchflight(self,xpath):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR,xpath)).perform()
        self.driver.find_element(By.CSS_SELECTOR, xpath).click()

    def scroll(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        n = 0
        while n != 6:
            maxheight = height
            self.driver.find_element(By.XPATH, '//body').send_keys(Keys.CONTROL + Keys.END)
            height = self.driver.execute_script("return document.body.scrollHeight")
            if maxheight == height:
                n = n + 1
            else:
                n = 0

    def fcount(self, xpath1, xpath2):
        global count1, count2
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        count1 = len(self.driver.find_elements(By.XPATH, xpath1))
        count2 = len(self.driver.find_elements(By.XPATH, xpath2))
        log.info("No. of flights on one side are : " + str(count1))
        log.info("No. of flights on second side are : " + str(count2))

    def morecity(self,xpathn,n,xpath3,css1,XS,CB):
        global stop1,stop2
        if n > 2:
            for i in range(2, n):
                globals()["count" + str(i + 1)] = len(self.driver.find_elements(By.XPATH, xpathn + str(i) + "']"))
                log.info("No. of flights on " + str(i + 1) + "th side are : " + str(globals()["count" + str(i + 1)]))
                globals()["RNDB" + str(i + 1)]=random.randint(1,globals()["count" + str(i + 1)])
                log.info("Random number"+str(i+1)+" generated is" +str(globals()["RNDB" + str(i + 1)]))
                fc1 = self.driver.find_element(By.XPATH, "("+xpathn + str(i) + "'])[" + str(globals()["RNDB" + str(i + 1)]) + "]")
                self.driver.execute_script("arguments[0].click();", fc1)

        for i in range(1,n+1):
            globals()["flight" + str(i)] = self.driver.find_element(By.XPATH, "(" + xpath3 + ")["+str(i)+"]").text
            log.info("First flight selected is: " +str(globals()["flight" + str(i)]))
            globals()["stop" + str(i)] = self.driver.find_element(By.XPATH, "(" + XS + ")["+str(i)+"]").text
            log.info("stop is: " + str(globals()["stop" + str(i)]))
        Total_Fare = self.driver.find_element(By.CSS_SELECTOR, css1).text
        log.info("Total fare needed to pay: " + Total_Fare)
        b1 = self.driver.find_element(By.CSS_SELECTOR, CB)
        self.driver.execute_script("arguments[0].click();", b1)


    def randomdiv(self, xpath1, xpath2, xpath3, css1, XS, CB,n,cflight):
        global flight1, flight2, Total_Fare, stop1,stop2
        RNDB1 = random.randint(1, count1)
        RNDB2 = random.randint(1, count2)

        if cflight!="no":
            RNDB1=1
            RNDB2=1

        log.info("Random number1 generated is" + str(RNDB1))
        log.info("Random number2 generated is" + str(RNDB2))

        fc1 = self.driver.find_element(By.XPATH, "(" + xpath1 + ")[" + str(RNDB1) + "]")
        self.driver.execute_script("arguments[0].click();", fc1)

        fc2 = self.driver.find_element(By.XPATH, "(" + xpath2 + ")[" + str(RNDB2) + "]")
        self.driver.execute_script("arguments[0].click();", fc2)

        if n>2:

            self.morecity(MultiLocate.radion(),n,MultiLocate.flight(),MultiLocate.TotalFare(),
                             MultiLocate.stop(), MultiLocate.booknow())
        else:
            flight1 = self.driver.find_element(By.XPATH, "(" + xpath3 + ")[1]").text
            log.info("First flight selected is: " + flight1)
            flight2 = self.driver.find_element(By.XPATH, "(" + xpath3 + ")[2]").text
            log.info("Second flight selected is: " + flight2)
            Total_Fare = self.driver.find_element(By.CSS_SELECTOR, css1).text
            log.info("Total fare needed to pay: " + Total_Fare)
            stop1 = self.driver.find_element(By.XPATH, "(" + XS + ")[1]").text
            log.info("First stop is: " + stop1)
            stop2 = self.driver.find_element(By.XPATH, "(" + XS + ")[2]").text
            log.info("Second stop is: " + stop2)
            b1 = self.driver.find_element(By.CSS_SELECTOR, CB)
            self.driver.execute_script("arguments[0].click();", b1)

    def flightChoice(self, Fname1, Fname2, F1, F2, xpath1, xpath2, xpath3, css1, XS, CB,cflight):
        global flight1, flight2, Total_Fare, stop1
        count1 = self.driver.find_elements(By.XPATH, Fname1)
        count2 = self.driver.find_elements(By.XPATH, Fname2)
        c1 = []
        c2 = []
        for i in range(1, len(count1) + 1):
            FlightName = self.driver.find_element(By.XPATH, "(" + Fname1 + ")[" + str(i) + "]").text
            c1.append(FlightName)

        log.info(c1)
        # self.move(MultiLocate.move())
        for j in range(1, len(count2) + 1):
            FlightName2 = self.driver.find_element(By.XPATH, "(" + Fname2 + ")[" + str(j) + "]").text
            c2.append(FlightName2)

        log.info(c2)
        # self.move(MultiLocate.move())
        Number1 = []
        Number2 = []
        pos1 = 0
        pos2 = 0
        for item in c1:
            if item == F1:
                index = c1.index(item, pos1)
                Number1.append(index + 1)
            pos1 += 1
        log.info(Number1)

        for item in c2:
            if item == F2:
                index = c2.index(item, pos2)
                Number2.append(index + 1)
            pos2 += 1
        log.info(Number2)

        # if no particular flight is not present
        if len(Number1) == 0 or len(Number2) == 0:
            count1 = len(self.driver.find_elements(By.XPATH, xpath1))
            count2 = len(self.driver.find_elements(By.XPATH, xpath2))
            log.info("No. of flights on one side are : " + str(count1))
            log.info("No. of flights on second side are : " + str(count2))
            RNDF1 = random.randint(1, count1)
            RNDF2 = random.randint(1, count2)

        else:
            RNDF1 = random.choice(Number1)
            RNDF2 = random.choice(Number2)

        if cflight != "no":
            if len(Number1) == 0 or len(Number2) == 0:
                RNDF1 = 1
                RNDF2 = 1
            else:
                RNDF1 = Number1[0]
                RNDF2 = Number2[0]
        log.info("Random number1 generated is" + str(RNDF1))
        log.info("Random number2 generated is" + str(RNDF2))

        fc1 = self.driver.find_element(By.XPATH, "(" + xpath1 + ")[" + str(RNDF1) + "]")
        self.driver.execute_script("arguments[0].click();", fc1)
        # self.move(MultiLocate.move())
        fc2 = self.driver.find_element(By.XPATH, "(" + xpath2 + ")[" + str(RNDF2) + "]")
        self.driver.execute_script("arguments[0].click();", fc2)
        # self.move(MultiLocate.move())
        flight1 = self.driver.find_element(By.XPATH, "(" + xpath3 + ")[1]").text
        log.info("First flight selected is: " + flight1)
        flight2 = self.driver.find_element(By.XPATH, "(" + xpath3 + ")[2]").text
        log.info("Second flight selected is: " + flight2)
        Total_Fare = self.driver.find_element(By.CSS_SELECTOR, css1).text
        log.info("Total fare needed to pay: " + Total_Fare)
        stop1 = self.driver.find_element(By.XPATH, "(" + XS + ")[1]").text
        log.info("First stop is: " + stop1)
        stop2 = self.driver.find_element(By.XPATH, "(" + XS + ")[2]").text
        log.info("Second stop is: " + stop2)
        b1 = self.driver.find_element(By.CSS_SELECTOR, CB)
        self.driver.execute_script("arguments[0].click();", b1)


    def paymentpage(self, bf1, TP, total,n):
        i = 2
        if stop1 == "1 Stop":
            i = 3
        else:
            if stop1 == "2 Stop":
                i = 4
        j=0
        if n>2:
            if stop1=="Non Stop" and stop2=="Non Stop":
                j=3
            if stop1=="Non Stop" and stop2=="1 Stop":
                j=4
            if stop1 == "Non Stop" and stop2 == "2 Stop":
                j=5
            if stop1 == "1 Stop" and stop2 == "1 Stop":
                j=5
            if stop1 == "1 Stop" and stop2 == "2 Stop":
                j=6
            if stop1 == "2 Stop" and stop2 == "2 Stop":
                j=7

        BufferFlight1 = self.driver.find_element(By.XPATH, "(" + bf1 + ")[1]").text
        BufferFlight2 = self.driver.find_element(By.XPATH, "(" + bf1 + ")[" + str(i) + "]").text
        BufferFlight3=""
        if n>2:
            BufferFlight3 = self.driver.find_element(By.XPATH, "(" + bf1 + ")[" + str(j) + "]").text
        ToPay = self.driver.find_element(By.XPATH, TP).text
        Total = self.driver.find_element(By.XPATH, total).text
        log.info("bf1 is: " + BufferFlight1)
        log.info("bf2 is: " + BufferFlight2)

        fb1 = re.split("\n", BufferFlight1)
        fb2 = re.split("\n", BufferFlight2)
        if n>2:
            fb3 = re.split("\n", BufferFlight3)
            f3 = fb3[0]
            log.info("flight3: " + f3)
        # print("flight1: " + fb1[0])
        # print("flight2: " + fb2[0])
        f1 = fb1[0]
        f2 = fb2[0]

        # print("needed to pay: " + ToPay)
        if flight1=="Air India":
            f1="Air India"
        if flight2=="Air India":
            f2="Air India"
        Ttraveller = int(adult1) + int(child1) + int(infant1)
        log.info("No. of Adults: "+ str(adult1))
        log.info("No. of childs: "+ str(child1))
        log.info("No. of Infants: "+ str(infant1))
        log.info("total travellers: "+ str(Ttraveller))
        log.info("FlightName1 of paymentpage: " + f1)
        log.info("FlightName2 of paymentpage: " + f2)
        log.info("FlightName1 Selected: " + str(flight1))
        log.info("FlightName2 Selected: " + str(flight2))
        # print("Total_Fare obtain: " + str(Total_Fare))
        log.info("Total: " + str(Total))
        log.info("ToPay: " + str(ToPay))

        assert f1 == flight1 and f2 == flight2


    def noFlights(self):
        check=self.driver.find_element(By.CLASS_NAME, "no-result-text").is_displayed()
        log.info("No Flights Available")
        if check=="True":
            Noflights=self.driver.find_element(By.CLASS_NAME,"no-result-text").text
            print(Noflights)
            return Noflights
        else:
            return "Flights available"
