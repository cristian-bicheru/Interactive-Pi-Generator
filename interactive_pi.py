# By: Cristian Bicheru
# Algorithm By The Chudnovsky Brothers
# Just A Simple Pi Calculating Program, Feel Free To Optimize!
##
from decimal import *
from math import *
import time
print("Enter The Desired Floating Point Precision:")
precision = int(input()) # Number of desired digits, more digits means more computing power required
getcontext().prec = precision
sumn = 0
n = -1
cycle = 1
print("Enable Dynamic Cycle Duration?") # Prints at regular time intervals vs. regular interation intervals
yon = input()
if yon == "y":
    dcycle = 1 # Enables dynamic cycling
    print("Set Time Interval:")
    intv = input()
    lastt = time.time() # Last cycle completion time variable
else:
    dcycle = 0 # Disables dynamic cycling
    print("Enter The Desired Cycle Duration:")
    cycledr = int(input()) # Number of iterations before printing in non-dynamic mode
while True:
    n += 1 # Below is the Chudnovsky Algorithm, it gives 1/pi, please ignore the likely excessive Decimal() s in the following code
    sumn = Decimal(sumn) + Decimal( Decimal( ((-1)**n) * Decimal(factorial(Decimal(6)*n)) * (13591409 + 545140134*n) ) / Decimal( Decimal(factorial(Decimal(3)*Decimal(n))) * Decimal((factorial(Decimal(n)))**Decimal(3)) * Decimal(Decimal(640320)**Decimal(3*n+3/2)) ) )
    if dcycle == 0: # Prints at regular intervals based on interation number
        if (n % cycledr) == 0:
            print("cycle " + str(cycle) + ", pi is: " + str(Decimal(Decimal(1)/(Decimal(sumn)*12))))
            cycle += 1
    if dcycle == 1: # Prints at regular intervals based on time interval
        cachedt = time.time()
        if (cachedt - lastt) >= int(intv):
            print("cycle " + str(cycle) + ", pi is: " + str(Decimal(Decimal(1)/(Decimal(sumn)*12))))
            cycle += 1
            lastt = time.time() # Update last cycle completetion time
