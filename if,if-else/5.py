# Write a Python program to check whether a given number is a perfect square. If it is, print "Perfect Square".
import math
num = int(input())
if math.isqrt(num) ** 2 == num:
    print("Perfect Square")