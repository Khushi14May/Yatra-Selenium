import random
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

from Locators import OnewayLocate
from TestCases.Base import BaseClass


class Page(BaseClass):
    def __init__(self, driver):
        global log
        self.driver = driver
        log=self.loggingDemo()


    def oneway(self,xpath):
        bb=self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", bb)
        log.info("started working")

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
        log.info("Return "+city1)
        self.driver.find_element(By.XPATH,ID).click()
        self.driver.find_element(By.XPATH,ID).send_keys(city1)
        time.sleep(1)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,ID).send_keys(Keys.ENTER)

    def departDate(self,xpath,Ddate):
        log.info("Departure date is: "+Ddate)
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "// td[ @id = '" +Ddate+ "' and @data-date='" +Ddate+"']").click()
        time.sleep(3)


    def dropdown(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(3)


    def FlightClass(self,economy,fare):

        if fare == "Student Fare Offer" or fare=="Senior Citizen Offer" or fare=="Armed Forces Offer":
            economy="Economy"
            self.driver.find_element(By.XPATH, "//span[text()='" + economy + "']").click()
            time.sleep(2)
        else:
            self.driver.find_element(By.XPATH, "//span[text()='" + economy + "']").click()
            time.sleep(2)
        log.info("economy selected is: " + economy)

    def traveller(self,adult,child,infant):
        global adult1, child1, infant1,a,c,i
        a=self.driver.find_element(By.XPATH,adult)
        c=self.driver.find_element(By.XPATH,child)
        i=self.driver.find_element(By.XPATH,infant)
        adult1=int(a.find_element(By.XPATH,"./..//span[@class='adultcount']").text)
        child1=int(c.find_element(By.XPATH,"./..//span[@class='adultcount']").text)
        infant1=int(i.find_element(By.XPATH,"./..//span[@class='adultcount']").text)


    def adult(self,adult,minus,plus):
        while adult1!=adult:
            if adult<adult1 and adult<=9:
            # minus
                a.find_element(By.XPATH,"."+minus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
            else:
                a.find_element(By.XPATH,"."+plus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
        self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())

    def child(self,child,fare,minus,plus):
        if fare=="Student Fare Offer" or fare=="Senior Citizen Offer":
            while child1>0:
                c.find_element(By.XPATH,"."+minus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
        else:
            while child1!=child and adult1+child1<9:
                if child1>child:
                    c.find_element(By.XPATH,"."+minus).click()
                else:
                    c.find_element(By.XPATH, "."+plus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
        self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())

    def infant(self,infant,fare,minus,plus):
        if fare=="Student Fare Offer" or fare=="Senior Citizen Offer":
            while infant1>0:
                log.info(infant1)
                i.find_element(By.XPATH,"."+ minus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())
        else:
            while infant1!=infant and infant1<adult1:
                if infant1>infant:
                    i.find_element(By.XPATH,"."+ minus).click()
                else:
                    i.find_element(By.XPATH,"."+plus).click()
                self.traveller(OnewayLocate.adult(),OnewayLocate.child(),OnewayLocate.infant())

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

    def fcount(self,cname,fare,Tfare):
        global count,countf
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        if fare=="no":
            count=len(self.driver.find_elements(By.CLASS_NAME, cname))
            log.info("No of flights are there: "+str(count))
        else:
            count=len(self.driver.find_elements(By.XPATH,Tfare))
            countf = count
            if count==0:
                count = len(self.driver.find_elements(By.CLASS_NAME, cname))
            log.info("No of flights are there: " + str(count))

    def randomdiv(self,s1,f1,b1,b2,m1,m2,fare,Tfare,cflight):
        global Stop,FlightName,money,count
        RNDB=random.randint(1, count)
        if cflight!="no":
            RNDB=1
        log.info("Random number generated is" + str(RNDB))
        if fare!="no" and countf!=0:
            Stop=self.driver.find_element(By.XPATH,"("+Tfare+"//div[@class=' font-lightgrey fs-10 tipsy i-b fs-10'])["+str(RNDB)+"]").text
            log.info("Type of the stop: " +Stop)
            FlightName = self.driver.find_element(By.XPATH,"("+Tfare+"//span[ @class ='i-b text ellipsis'])["+str(RNDB)+"]").text
            log.info("Name of the flight selected: " + FlightName)
            button = self.driver.find_element(By.XPATH,"("+Tfare+"//button)["+str(RNDB)+"]").text
            log.info("value of button is: " + button)
        else:
            Stop=self.driver.find_element(By.XPATH,s1+"["+str(RNDB)+"]").text
            log.info("Type of the stop: "+Stop)
            FlightName=self.driver.find_element(By.XPATH,f1+"["+str(RNDB)+"]").text
            log.info("Name of the flight selected: " + FlightName)
            button=self.driver.find_element(By.XPATH,b1+"["+str(RNDB)+"]").text
            log.info("value of button is: "+button)

        if button=="View Fares":
            time.sleep(2)
            if fare!="no" and countf!=0:
                view=self.driver.find_element(By.XPATH, "(" + Tfare + "//button)[" + str(RNDB) + "]")
                self.driver.execute_script("arguments[0].click();", view)
                time.sleep(4)
                countB = len(self.driver.find_elements(By.XPATH,Tfare+b2))
                RNDb = random.randint(1, countB)
                log.info("Random number for book button generated is" + str(RNDb))
                money = self.driver.find_element(By.XPATH,"("+Tfare+"//div[@class='v-aligm-m i-b'])[" + str(RNDb) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                bb = self.driver.find_element(By.XPATH, "(" + Tfare+b2 + ")" + "[" + str(RNDb) + "]")
                self.driver.execute_script("arguments[0].click();", bb)
                time.sleep(5)
            else:
                view=self.driver.find_element(By.XPATH, b1+"["+str(RNDB)+"]//button")
                self.driver.execute_script("arguments[0].click();", view)
                time.sleep(4)
                countB=len(self.driver.find_elements(By.XPATH,b2))
                RNDb = random.randint(1, countB)
                log.info("Random number for book button generated is" + str(RNDb))
                money=self.driver.find_element(By.XPATH,m1+"["+str(RNDb)+"]").text
                log.info("Money of the flight is: "+money)
                time.sleep(2)
                bb=self.driver.find_element(By.XPATH,"("+b2+")"+"["+str(RNDb)+"]")
                self.driver.execute_script("arguments[0].click();", bb)
                time.sleep(5)

        else:
            if fare!="no" and countf!=0:
                money = self.driver.find_element(By.XPATH,"("+Tfare+"// div[@class ='i-b tipsy fare-summary-tooltip fs-18'])[" + str(RNDB) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                b = self.driver.find_element(By.XPATH, b1 + "[" + str(RNDB) + "]//button")
                self.driver.execute_script("arguments[0].click();", b)
                time.sleep(5)
            else:
                money=self.driver.find_element(By.XPATH, m2+"["+str(RNDB)+"]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                b=self.driver.find_element(By.XPATH,"("+Tfare+"//button)["+str(RNDB)+"]")
                self.driver.execute_script("arguments[0].click();", b)
                time.sleep(5)

    def flightChoice(self,Fname,cname,f1,s1,b1,b2,m1,m2,fare,Tfare,cflight):
        global Stop,FlightName,money,count
        log.info("count: "+str(count))
        if fare!="no":
            count=len(self.driver.find_elements(By.XPATH,Tfare+"//span[ @class ='i-b text ellipsis']"))
            flights = []
            for i in range(1, count + 1):
                FlightName = self.driver.find_element(By.XPATH,"("+Tfare+"//span[ @class ='i-b text ellipsis'])["+str(i)+"]").text
                flights.append(FlightName)
            log.info("flights: "+str(flights))
        else:
            flights=[]
            for i in range(1,count+1):
                FlightName= self.driver.find_element(By.XPATH,f1+"[" + str(i) + "]").text
                flights.append(FlightName)
            log.info("flights: "+str(flights))
        Number = []
        pos = 0
        for item in flights:
            if item ==Fname:
                index = flights.index(item, pos)
                Number.append(index + 1)
            pos += 1
        #
        log.info("Number list: "+str(Number))
        if len(Number)==0:
            count = len(self.driver.find_elements(By.CLASS_NAME, cname))
            RNDF=random.randint(1,count)
        else:
            RNDF=random.choice(Number)

        if cflight!="no":
            if len(Number) == 0:
                RNDF=1
            else:
                RNDF = Number[0]
        log.info("Random number generated is: " + str(RNDF))

        if fare!="no" and len(Number)!=0:
            Stop = self.driver.find_element(By.XPATH,"(" + Tfare + "//div[@class=' font-lightgrey fs-10 tipsy i-b fs-10'])[" + str(RNDF) + "]").text
            log.info("Type of the stop: " + Stop)
            FlightName = self.driver.find_element(By.XPATH,"(" + Tfare + "//span[ @class ='i-b text ellipsis'])[" + str(RNDF) + "]").text
            log.info("Name of the flight selected: " + FlightName)
            button = self.driver.find_element(By.XPATH, "(" + Tfare + "//button)[" + str(RNDF) + "]").text
            log.info("value of button is: " + button)
        else:
            Stop = self.driver.find_element(By.XPATH, s1+"["+str(RNDF)+"]").text
            log.info("Type of the stop: " + Stop)
            FlightName = self.driver.find_element(By.XPATH,f1+"["+str(RNDF)+"]").text
            log.info("Name of the flight selected: " + FlightName)
            button = self.driver.find_element(By.XPATH,b1+"["+str(RNDF)+"]").text
            log.info("value of button is: " + button)
        if button == "View Fares":
            time.sleep(2)
            if fare != "no" and len(Number)!=0:
                view = self.driver.find_element(By.XPATH, "(" + Tfare + "//button)[" + str(RNDF) + "]")
                self.driver.execute_script("arguments[0].click();", view)
                time.sleep(4)
                countB = len(self.driver.find_elements(By.XPATH, Tfare + b2))
                RNDb = random.randint(1, countB)
                log.info("Random number generated is" + str(RNDb))
                money = self.driver.find_element(By.XPATH,"("+Tfare + "//div[@class='v-aligm-m i-b'])[" + str(RNDb) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                bb = self.driver.find_element(By.XPATH, "(" + Tfare + b2 + ")" + "[" + str(RNDb) + "]")
                self.driver.execute_script("arguments[0].click();", bb)
                time.sleep(5)
            else:
                view = self.driver.find_element(By.XPATH, b1 + "[" + str(RNDF) + "]//button")
                self.driver.execute_script("arguments[0].click();", view)
                time.sleep(4)
                countB = len(self.driver.find_elements(By.XPATH, b2))
                RNDb = random.randint(1, countB)
                log.info("Random number generated is" + str(RNDb))
                money = self.driver.find_element(By.XPATH, m1 + "[" + str(RNDb) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                bb = self.driver.find_element(By.XPATH, "(" + b2 + ")" + "[" + str(RNDb) + "]")
                self.driver.execute_script("arguments[0].click();", bb)
                time.sleep(5)

        else:
            if fare != "no" and len(Number)!=0:
                money = self.driver.find_element(By.XPATH,"("+Tfare + "// div[@class ='i-b tipsy fare-summary-tooltip fs-18'])[" + str(RNDF) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                b = self.driver.find_element(By.XPATH, b1 + "[" + str(RNDF) + "]//button")
                self.driver.execute_script("arguments[0].click();", b)
                time.sleep(5)
            else:
                money = self.driver.find_element(By.XPATH, m2 + "[" + str(RNDF) + "]").text
                log.info("Money of the flight is: " + money)
                time.sleep(2)
                b = self.driver.find_element(By.XPATH, "(" + Tfare + "//button)[" + str(RNDF) + "]")
                self.driver.execute_script("arguments[0].click();", b)
                time.sleep(5)
    def noFlights(self):
        check=self.driver.find_element(By.CLASS_NAME, "no-result-text").is_displayed()
        log.info("No Flights Available")
        if check==True:
            Noflights=self.driver.find_element(By.CLASS_NAME,"no-result-text").text
            log.info("flights: "+str(Noflights))
            return Noflights
        else:
            return "Flights available"

    def paymentpage(self,bf1,TP,total):
        global money
        BufferFlight=self.driver.find_element(By.XPATH,bf1).text
        ToPay=self.driver.find_element(By.XPATH,TP).text
        Total=self.driver.find_element(By.XPATH,total).text
        fb1 = re.split("\n", BufferFlight)
        f1 = fb1[0]
        money1=0
        money=re.sub(",","",str(money))
        money=int(money)
        Total=re.sub("Rs. ","",Total)
        ToPay= re.sub(",", "",ToPay)

        if FlightName=="IndiGo" or FlightName=="SpiceJet" or FlightName=="Akasa Air":
            money1=(int(money)*(int(adult1)+int(child1))+(int(infant1) * 1500))
        if FlightName=="Air Asia":
            money1 = (int(money)*(int(adult1)+int(child1))+(int(infant1) * 3000))
        if FlightName=="Vistara":
            money1 = (int(money)*(int(adult1)+int(child1))+(int(infant1)  * 1544))
        if FlightName=="Alliance Air":
            money1 = (int(money)*(int(adult1)+int(child1))+(int(infant1)  * 1575))
        if FlightName=="Air India":
            f1=FlightName
            log.info("After,compile:"+f1)
            money1 = (int(money)*(int(adult1)+int(child1))+(int(infant1)  * 1491))


        Ttraveller=int(adult1) + int(child1) + int(infant1)
        log.info("No. of Adults: "+str(adult1))
        log.info("No. of childs: "+ str(child1))
        log.info("No. of Infants: "+str(infant1))
        log.info("total travellers: "+str(Ttraveller))
        log.info("FlightName of paymentpage: "+f1)
        log.info("FlightName: "+str(FlightName))
        log.info("After calculating money: "+str(money1))
        log.info("money of flight selected as per 1 traveller(adult): "+str(money))
        log.info("Total: "+str(Total))
        log.info("ToPay: "+str(ToPay))
        assert f1==FlightName
