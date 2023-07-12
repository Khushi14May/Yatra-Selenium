import random
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
from Locators import RoundtripLocate
from TestCases.Base import BaseClass


class PageR(BaseClass):
    def __init__(self, driver):
        global log
        self.driver = driver
        log = self.loggingDemo()

    def roundtrip(self,xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def departFrom(self,xpath,city1):
        # listCity=["New Delhi ","Banglore "]
        # city1=random.choice(listCity)
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,xpath).send_keys(city1)
        time.sleep(2)
        self.driver.find_element(By.XPATH,xpath).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        time.sleep(2)

    def goingTo(self,ID,city1):
        # listCity = ["Mumbai ", "Goa "]
        # city1 = random.choice(listCity)
        self.driver.find_element(By.XPATH,ID).click()
        # time.sleep(2)
        self.driver.find_element(By.XPATH,ID).send_keys(city1)
        time.sleep(2)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.ENTER)

    def departDate(self,xpath,Ddate):
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "// td[ @id = '" +Ddate+ "' and @data-date='" +Ddate+"']").click()
        time.sleep(3)

    def returnDate(self,xpath,Rdate):
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td [@id='" + Rdate + "' and @data-date='" + Rdate + "']").click()
        time.sleep(3)

    def dropdown(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(3)

    def FlightClass(self, economy, fare):
        if fare == "Student Fare Offer" or fare == "Senior Citizen Offer":
            economy = "Economy"
            self.driver.find_element(By.XPATH, "//span[text()='" + economy + "']").click()
            time.sleep(2)
        else:
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
        log.info("adult work started")
        while adult1 != adult:
            if adult < adult1 and adult <= 9:
                a.find_element(By.XPATH,"."+minus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
            else:
                a.find_element(By.XPATH, "."+plus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        self.traveller(RoundtripLocate.adult(),RoundtripLocate.child(), RoundtripLocate.infant())
        log.info("adult work completed")

    def child(self, child, fare, minus, plus):
        log.info("child work started")
        if fare == "Student Fare Offer" or fare == "Senior Citizen Offer":
            while child1 > 0:
                c.find_element(By.XPATH,"."+minus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(),RoundtripLocate.infant())
        else:
            while child1 != child and adult1 + child1 < 9:
                if child1 > child:
                    c.find_element(By.XPATH,"."+minus).click()
                else:
                    c.find_element(By.XPATH,"."+plus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        log.info("child work completed")

    def infant(self, infant, fare, minus, plus):
        log.info("infant work started")
        if fare == "Student Fare Offer" or fare == "Senior Citizen Offer":
            while infant1 > 0:
                i.find_element(By.XPATH,"."+minus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        else:
            while infant1 != infant and infant1 < adult1:
                if infant1 > infant:
                    i.find_element(By.XPATH,"."+minus).click()
                else:
                    a.find_element(By.XPATH,"."+ plus).click()
                self.traveller(RoundtripLocate.adult(), RoundtripLocate.child(), RoundtripLocate.infant())
        log.info("infant work completed")

        log.info("travel adult1: " + str(adult1))
        log.info("travel child1: " + str(child1))
        log.info("travel infant1: " + str(infant1))

    def fares(self,flight,fare):
        if flight != "no":
            self.driver.find_element(By.XPATH, "// a[ @ title = '" + flight + "']").click()
            time.sleep(2)
        if fare != "no":
            self.driver.find_element(By.XPATH, "// a[ @ title = '" + fare + "']").click()
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

    def fcount(self,xpath1,xpath2,fare,Tfare):
        global count1,count2,countf1,countf2

        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        if fare!="no":
            count1 = len(self.driver.find_elements(By.XPATH, Tfare+xpath1))
            count2 = len(self.driver.find_elements(By.XPATH,Tfare+xpath2))
            log.info("No. of flights on one side are : " + str(count1))
            log.info("No. of flights on second side are : " + str(count2))
            countf1=count1
            countf2=count2
            if count1==0 or count2==0:
                count1 = len(self.driver.find_elements(By.XPATH, xpath1))
                count2 = len(self.driver.find_elements(By.XPATH, xpath2))
                log.info("No. of flights on one side are : " + str(count1))
                log.info("No. of flights on second side are : " + str(count2))
        else:
            count1 = len(self.driver.find_elements(By.XPATH,xpath1))
            count2 = len(self.driver.find_elements(By.XPATH,xpath2))
            log.info("No. of flights on one side are : " + str(count1))
            log.info("No. of flights on second side are : " + str(count2))

    def randomdiv(self,xpath1,xpath2,xpath3,css1,XS,CB,fare,Tfare,cflight):
        global flight1, flight2, Total_Fare, stop1
        RNDB1=random.randint(1, count1)
        RNDB2 = random.randint(1, count2)

        if cflight!="no":
            RNDB1=1
            RNDB2=1
        log.info("Random number1 generated is"+str(RNDB1))
        log.info("Random number2 generated is" + str(RNDB2))

        if fare!="no" and countf1!=0 and countf2!=0:
            fc1 = self.driver.find_element(By.XPATH, "(" + Tfare+xpath1 + ")[" + str(RNDB1) + "]")
            self.driver.execute_script("arguments[0].click();", fc1)
            fc2 = self.driver.find_element(By.XPATH, "(" +Tfare+xpath2 + ")[" + str(RNDB2) + "]")
            self.driver.execute_script("arguments[0].click();", fc2)
        else:
            fc1=self.driver.find_element(By.XPATH, "("+xpath1+")["+str(RNDB1)+"]")
            self.driver.execute_script("arguments[0].click();", fc1)
            fc2=self.driver.find_element(By.XPATH, "("+xpath2+")[" + str(RNDB2) + "]")
            self.driver.execute_script("arguments[0].click();", fc2)

        flight1=self.driver.find_element(By.XPATH, "("+xpath3+")[1]").text
        log.info("First flight selected is: "+flight1)
        flight2 = self.driver.find_element(By.XPATH,"("+xpath3+")[2]").text
        log.info("Second flight selected is: " + flight2)
        Total_Fare=self.driver.find_element(By.CSS_SELECTOR,css1).text
        log.info("Total fare needed to pay: " + Total_Fare)
        stop1=self.driver.find_element(By.XPATH,"("+XS+")[1]").text
        log.info("First stop is: " + stop1)
        stop2=self.driver.find_element(By.XPATH,"("+XS+")[2]").text
        log.info("Second stop is: " +stop2)
        b1=self.driver.find_element(By.CSS_SELECTOR,CB)
        self.driver.execute_script("arguments[0].click();", b1)

    def flightChoice(self,Fname1,Fname2,Tfare,fare,Flight,F1,F2,xpath1,xpath2,xpath3,css1,XS,CB,cflight):
        global flight1, flight2, Total_Fare, stop1
        if fare!="no":
            log.info("fares block")
            count1 = self.driver.find_elements(By.XPATH, Fname1+Tfare+Flight)
            count2 = self.driver.find_elements(By.XPATH, Fname2+Tfare+Flight)
        else:
            log.info("no fares block")
            count1=self.driver.find_elements(By.XPATH,Fname1+Flight)
            count2=self.driver.find_elements(By.XPATH,Fname2+Flight)
        c1=[]
        c2=[]
        if fare!="no":
            log.info("fares block")
            for i in range(1, len(count1) + 1):
                FlightName = self.driver.find_element(By.XPATH, "(" + Fname1+Tfare+Flight + ")[" + str(i) + "]").text
                c1.append(FlightName)

            log.info(c1)
            for j in range(1, len(count2) + 1):
                FlightName2 = self.driver.find_element(By.XPATH, "(" + Fname2+Tfare+Flight + ")[" + str(j) + "]").text
                c2.append(FlightName2)

            log.info(c2)
        else:
            log.info("no fares block")
            for i in range(1, len(count1) + 1):
                FlightName = self.driver.find_element(By.XPATH, "(" + Fname1+Flight+ ")[" + str(i) + "]").text
                c1.append(FlightName)

            log.info(c1)
            for j in range(1, len(count2) + 1):
                FlightName2 = self.driver.find_element(By.XPATH, "(" + Fname2 + Flight+ ")[" + str(j) + "]").text
                c2.append(FlightName2)

            log.info(c2)

        Number1=[]
        Number2 =[]
        pos1 = 0
        pos2=0
        for item in c1:
            if item ==F1:
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
        if len(Number1) == 0 or len(Number2)==0 :
            count1 = len(self.driver.find_elements(By.XPATH, xpath1))
            count2 = len(self.driver.find_elements(By.XPATH, xpath2))
            log.info("No. of flights on one side are : " + str(count1))
            log.info("No. of flights on second side are : " + str(count2))
            RNDF1 = random.randint(1, count1)
            RNDF2 = random.randint(1, count2)

        else:
            RNDF1 = random.choice(Number1)
            RNDF2 = random.choice(Number2)

        if cflight!="no":
            log.info("cheap flights block")
            if len(Number1) == 0 or len(Number2)==0 :
                RNDF1 = 1
                RNDF2 = 1
            else:
                log.info("no cheap flights block")
                RNDF1=Number1[0]
                RNDF2=Number2[0]
        log.info("Random number1 generated is" + str(RNDF1))
        log.info("Random number2 generated is" + str(RNDF2))
        if fare != "no" and (len(Number1) != 0 or len(Number2)!=0):
            log.info("fares block")
            fc1 = self.driver.find_element(By.XPATH, "(" + Tfare + xpath1 + ")[" + str(RNDF1) + "]")
            self.driver.execute_script("arguments[0].click();", fc1)
            fc2 = self.driver.find_element(By.XPATH, "(" + Tfare + xpath2 + ")[" + str(RNDF2) + "]")
            self.driver.execute_script("arguments[0].click();", fc2)
        else:
            log.info("no fares block")
            fc1 = self.driver.find_element(By.XPATH, "(" + xpath1 + ")[" + str(RNDF1) + "]")
            self.driver.execute_script("arguments[0].click();", fc1)
            fc2 = self.driver.find_element(By.XPATH, "(" + xpath2 + ")[" + str(RNDF2) + "]")
            self.driver.execute_script("arguments[0].click();", fc2)

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
        b1=self.driver.find_element(By.CSS_SELECTOR, CB)
        self.driver.execute_script("arguments[0].click();", b1)

    def paymentpage(self,bf1,TP,total):
        global stop1
        i=2
        if stop1 == "1 Stop":
            i=3
        else:
            if stop1=="2 Stop":
                i=4
        BufferFlight1=self.driver.find_element(By.XPATH,"("+bf1+")[1]").text
        BufferFlight2 = self.driver.find_element(By.XPATH,"("+bf1+")["+str(i)+"]").text
        ToPay=self.driver.find_element(By.XPATH,TP).text
        Total=self.driver.find_element(By.XPATH,total).text
        # print("bf1 is: " + BufferFlight1)
        # print("bf2 is: " + BufferFlight2)
        fb1 = re.split("\n",BufferFlight1)
        fb2 = re.split("\n",BufferFlight2)
        # print("flight1: "+fb1[0])
        # print("flight2: "+fb2[0])
        f1=fb1[0]
        f2 = fb2[0]
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
        log.info("Total_Fare obtain: " + str(Total_Fare))
        log.info("Total: " + str(Total))
        log.info("ToPay: " + str(ToPay))
        assert f1==flight1 and f2==flight2

    def noFlights(self):
        check=self.driver.find_element(By.CLASS_NAME, "no-result-text").is_displayed()
        log.info("No Flights Available")
        if check=="True":
            Noflights=self.driver.find_element(By.CLASS_NAME,"no-result-text").text
            log.info("No flights available"+Noflights)
            return Noflights
        else:
            return "Flights available"

