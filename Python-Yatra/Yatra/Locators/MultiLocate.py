def MultiCitybutton():
    return "// a[ @ title = 'Multicity']"

def departfrom1():
    return "//input[@id='BE_flight_origin_city_1']"

def goingTo1():
    return "//input[@id='BE_flight_arrival_city1']"

def departfrom2():
    return "//input[@id='BE_flight_origin_city_2']"

def goingTo2():
    return "//input[@id='BE_flight_arrival_city2']"

def departfromn(i):
    return "//input[@id='BE_flight_origin_city_"+str(i)+"']"

def goingTon(i):
    return "//input[@id='BE_flight_arrival_city"+str(i)+"']"

def DepartDate1():
    return "// input[ @ id = 'BE_flight_origin_date_1']"

def DepartDate2():
    return "// input[ @ id = 'BE_flight_origin_date_2']"

def DepartDaten(i):
    return "// input[ @ id = 'BE_flight_origin_date_"+str(i)+"']"

def dropdown():
    return "//i[@class='icon icon-angle-right arrowpassengerBox']"

def adult():
    return "//span[@id='adultPax']"

def child():
    return "//span[@id='childPax']"

def infant():
    return "//span[@id='infantPax']"

def plus():
    return "/../..//span[@class='ddSpinnerPlus']"

def minus():
    return "/../..//span[@class='ddSpinnerMinus']"

def AddCity():
    return "flightsAddCity"

def searchbutton():
    return "input[value = 'Search Flights']"

def radio1():
    return  "//input[@name='select0']"

def radio2():
    return  "//input[@name='select1']"

def radion():
    return "//input[@name='select"

def move():
    return "text i-b bold"

def flight():
    return "//div[@class='wr-hr-center wr-width grid flex ']//div[@class='i-b pr']//p"

def TotalFare():
    return "p[class='i-b fs-22 bold']"

def stop():
    return "//div[@class='wr-hr-center wr-width grid flex ']//div[@class=' font-lightgrey fs-10 tipsy i-b fs-10']"

def booknow():
    return "button[autom ='booknow']"

def FlightChoice1():
    return "(//div[@class='flight-seg col-6 v-aligm-t'])[1]//p[@class='normal fs-10 fs-10 abs font-lightestgrey no-wrap mt-2 fl-no']"

def FlightChoice2():
    return "(//div[@class='flight-seg col-6 v-aligm-t'])[2]//p[@class='normal fs-10 fs-10 abs font-lightestgrey no-wrap mt-2 fl-no']"


def BufferFlight():
    return "//span[@class='ib fs-12 gray ng-binding']"

def topay():
    return "(//span[@class='pull-right tr ib fs-18']//span)[2]"

def total():
    return "//span[@class='ib gray-dark bold pull-right ng-binding fs-24']"