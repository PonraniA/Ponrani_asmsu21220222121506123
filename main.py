yr=int(input("Enter yr"))
if(yr%400==0)and(yr%100==0):
  print("{0}is a leap". format(yr))
elif(yr%4==0)and(yr%100!=0):
  print("{0}is a leap". format(yr))
else: 
  print("{0}is a not leap year". format(yr))