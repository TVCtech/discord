from datetime import datetime, date

def age_counter():

    print("Your date of birth (dd mm yyyy)")
    date_of_birth = datetime.strptime(input("->"), "%d %m %Y")
    #date_of_birth = datetime.strptime('07 06 1985', "%d %m %Y")
    today = date.today()
    d = today.year - date_of_birth.year
    print(f'Your age is {d} years, {d*12} months,{(d*12)*365} days,   ' )
    print(f'You have {80-d} years left, ')
        
    i = 1
    colum = 0
    row = 0
    aList = []
    while i <= d:
        i+=1
        x= "X"
        aList.append(x) 
    
    while i <=80:
        i+=1
        x= " "
        aList.append(x) 
    
    for element in range(int((len(aList))/10)):
        print(aList[colum:(colum+9)])
        colum+=10

age_counter()

