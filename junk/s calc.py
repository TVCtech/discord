import datetime
from datetime import date

def age_counter():
    l_date = datetime.date.today()
    # a = int(input("enter the year you were born: "))
    # b = int(input("enter the month you were born(1-12): "))
    # c = int(input("enter the day you were born:  "))
    a = 1985
    b = 6
    c = 7
    f_date = date(a, b, c)
    d = l_date.year - f_date.year
    print("Your age is ", d, "years /", d*12, "months / ", (d*12)*365, "days.", "\nYou have", 80-d, "years / ", 80*12-d*12,"months /", 80*12*365-d*12*365, "days left.", "\nYou have lived ", (d/80)*100, "%","percent of your life.")
    
    
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
    #print(aList)
   
    
    for element in range(int((len(aList))/10)):
        print(aList[colum:(colum+9)])
        colum+=10



    # import cmd
    # cli = cmd.Cmd()
    # cli.columnize(aList, displaywidth=20)  
        
   # print(aList)
    # elif i > d:
    #     i+=1
    #     x= " "
    #     aList = [[x] * 8] * 10
    #     print(*aList, sep="\n")

age_counter()

