for i in range (1,4):
     print("Enter hours and hourly wage" , i)
     hour = input("Hours worked: ")
     hour = int(hour)
     rate = input ("Hourly rate: ")
     rate = int (rate)

     if hour > 40:
         sal = (40*rate)+ (1.5*rate*(hour-40))
     else:                           
            sal = hour*rate
            print("The salary of the worker", i, "is", sal)
         

