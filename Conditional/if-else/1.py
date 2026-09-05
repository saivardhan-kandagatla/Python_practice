# Check if a given year is a leap year.
num = int(input("Enter a year: "))
if(num % 4==0 and num % 100 != 0 or num % 400 == 0):
    print("it is leap year")
else:
    print("Not a leap year")
