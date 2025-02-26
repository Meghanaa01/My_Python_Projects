def myfunc(fname,lname):
    ''' gives the first and last name with titling the names in format'''
    fname=input("enter first name").title()
    lname=input("enter last name").title()
    return fname,lname

myfunc('s','l')