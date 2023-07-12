def Roundtripbutton():
    return "// a[ @ title = 'Round Trip']"

def departfrom():
    return "//input[@id='BE_flight_origin_city']"

def goingTo():
    return "//input[@id='BE_flight_arrival_city']"

def DepartDate():
    return "// input[ @ id = 'BE_flight_origin_date']"

def ReturnDate():
    return "//input[@id='BE_flight_arrival_date']"

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

def searchbutton():
    return "input[value = 'Search Flights']"

def radio1():
    return  "//input[@name='select0']"

def radio2():
    return  "//input[@name='select1']"

def Tfare():
    return "// div[ @class ='special-fare tipsy fs-9'] /../../../.."

def flight():
    return "//div[@class='wr-hr-center wr-width grid flex ']//div[@class='i-b pr']//p"

def TotalFare():
    return "p[class='i-b fs-22 bold']"

def stop():
    return "//div[@class='wr-hr-center wr-width grid flex ']//div[@class=' font-lightgrey fs-10 tipsy i-b fs-10']"

def booknow():
    return "button[autom ='booknow']"

def FlightChoice1():
    return "(//div[@class='flight-seg col-6 v-aligm-t'])[1]"

def FlightChoice2():
    return "(//div[@class='flight-seg col-6 v-aligm-t'])[2]"

def Flight():
    return "//p[@class='normal fs-10 fs-10 abs font-lightestgrey no-wrap mt-2 fl-no']"

def BufferFlight():
    return "//span[@class='ib fs-12 gray ng-binding']"

def topay():
    return "(//span[@class='pull-right tr ib fs-18']//span)[2]"

def total():
    return "//span[@class='ib gray-dark bold pull-right ng-binding fs-24']"