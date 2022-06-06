#Task 1
a = 3
b = 6
c = 7
total_sum = a + b + c 
average = total_sum / 3
print("The total_sum is :", total_sum)
print("The average sum is:", average)


#Task 2
Name = input("Please what is your name?")
print("Hello there",Name)

#Task 3
tempincelsius = input("Please Give a temperature in Celsius:")
fahrenheit_temp = (float(tempincelsius)*1.8)+ 32
#(float(celcius_temp)*1.8)+32
#print(float(fahrenheit_temp))
print("The temperature in Celsius is "+tempincelsius+" degree Celsius","and Fahrenheit degree is",fahrenheit_temp)

#Task 4
import datetime

year= datetime.datetime.now().year
name=input("Give your name:")
year_of_birth = int(input("Which year you were born:"))
#I don't know why the name is not separated from "You are"
print("Hello,", name + "You are %i years old in 2022" % (year - year_of_birth))

#Task 5
type_of_string= input("Give a string:")
number= int(input("Give a number:"))
results= type_of_string * number
print("The results are:", results)

#Tasks 6
from math import sqrt
print("General formula:-ax**2 + bx +c = 0")
a=int(input("Enter a(a!=0):"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

d= (b**2)-(4*a*c)
solution1=(-b + sqrt(d)) / (2 * a)
solution2=(-b - sqrt(d)) / (2 * a)
if d>0:
  print("Type of Roots:Two Distinct Real Roots")
elif d==0:
  print("Type of Roots:Two Equal Real Roots")
elif d<0:
  print("Type of Roots:Two complex Roots")
print(f"The solutions are {solution1} and {solution2}")









