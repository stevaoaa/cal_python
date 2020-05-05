# -*- coding: utf-8 -*-

"""
Python version of unix utility Cal 
"""


number_of_days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
def number_of_days(month, year):

    """
        Computes the number of days in a given month / year
        @param month: the month
        @param year: the year
        @return: The number of days of the month "month" in year "year".
    """

    if (is_leap(year) and month == 2):
        return 29

    if ( year == 1752 and month == 9 ):
        return 19
   
    return number_of_days_month[month]




def first_of_month(month, year):

    """
        This method computes the corresponding day of the week
        the first day of a given month.
        @param month: the month of the year

        @param year: the year 
        @return: A value between 0 and 6 that corresponds to the day 
        of the week that the day falls 
    """ 

    k = 0

    if (is_leap(year) and month > 2):
        k+= 1
        
    for i in range(0, month):
        k += number_of_days_month[i]

    if ( year == 1752 and month > 9 ):
        k -= 11

    k %= 7
    k = int(k + jan1(year)) % 7

    return k



def is_leap(year):
    """
        Checks whether a given year is leap year
        @param year: the year.
        @return: True if the year is leap and False otherwise.
    """

    if ( year <= 1752 ):

        if ( year % 4 == 0 ):
            return True
        else:
            return False

    else:

        if ( year % 400 == 0 ):
            return True
        if ( year % 100 == 0 ):
            return False
        if ( year % 4 == 0 ):
            return True

    return False




def jan1(year):

    """
        Computes the day of the week of the first day of the year.
        @param year: the year you want to compute the day of the week.
        @return: a value between 0 and 6 that indicates the day of the first week
        day of the year.
    """


    y, d = 0, 0

    """
        normal gregorian calendar
        one extra day per four years
    """

    y = year
    d = 4 + y + (y+3) /4

    """
        julian calendar
        regular gregorian
        less three days per 400
    """

    if(y > 1800):
        d -= (y-1701)/100
        d += (y-1601)/400

    """
        great calendar changeover instant
    """
    
    if(y > 1752):
        d += 3

    return int(d % 7)



def cal(dds, n):

    """
        Computes a string that represents the calendar for a given month
        
        @param dds: This parameter indicates which day of the week the month starts. 
        It must be a value between 0 and 6.
        @param n: Indicates how many days the month has. It can be a value between 28 and 31
        or the value 19, which indicates that it is the month of September 1752, when
        a change in the Julian / Gregorian calendar is considered. 
        
        @return: an string corresponding to the calendar for a given month
    """

    if ( n == 19 ):
        return "       1  2 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30"

    s = ""

    for k in range(0, dds):
        s += "   "

    cont = dds+1
    
    for k in range(1, n + 1):
        
        if ( k < 10 ): 
            s += " "
        
        s += str(k)
        
        if ( cont % 7 == 0):
            s += "\n"
        
        else:
            s += " "
        
        cont+= 1

    return s




if __name__ == "__main__":
    
    dayw = "Do Se Te Qa Qi Se Sa"

    smon = ["Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"]

    import sys

    number_of_parameters = len(sys.argv) 

    if(number_of_parameters >= 3 or number_of_parameters == 1):

        #print out just month
        if(number_of_parameters == 1):

            #current month
            import datetime
            today = datetime.datetime.today()

            m = today.month
            y = today.year
        
        else:

            m = 0

            #parse the month parameter
            try:
                m = int(sys.argv[1]) #argv[0] is  always the name of the python script. [1] is the first parameter
            except Exception as e:
                print("type error: " + str(e))

            if(m < 1 or m > 12):
                print("Cal: {}: invalid month.\n".format(sys.argv[1]))
                sys.exit(-1)

            y = 0

            #parse the year parameter
            try:
                y = int(sys.argv[2])

            except Exception as e:
                print("type error: " + str(e))

            if(y < 1 or y > 9999):
                print("Cal: {}: invalid year.\n".format(sys.argv[2]))
                sys.exit(-1)

        #print the result
        print("   {} {}\n".format(smon[m-1], y) )
        print("{}\n".format(dayw))

        dds = first_of_month(m, y)
        n   = number_of_days(m, y)
        result = cal(dds, n)

        print(result)
        print()
    

    #print the complet year
    else:
        
        y = 0

        #parse the year parameter
        try:
            y = int(sys.argv[1])

        except Exception as e:
            print("type error: " + str(e))

        if(y < 1 or y > 9999):
            print("Cal: {}: invalid year.\n".format(sys.argv[1]))
            sys.exit(-1)

        for z in range(1, 13):

            print("   {} {}\n".format(smon[z-1], y) )
            print("{}\n".format(dayw))

            dds = first_of_month(z, y)
            n   = number_of_days(z, y)
            
            result = cal(dds, n)

            print(result)
            print()