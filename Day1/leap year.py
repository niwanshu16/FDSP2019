n=int(input("enter a year "))
if n%100==0 :
      if n%400==0:
             print("Leap year")
      else :
            print("Not a leap year ")
else:
      if n%4==0:
          print("Leap year")
      else:
          print("Not a leap year")
    
