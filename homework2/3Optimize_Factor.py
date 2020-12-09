#3Optimize_Factor
import time
from math import sqrt

def PN_X(n):
    time_start = time.time()
    number_pn = 0

    number_pn = 2#originally include 2 and 3
    for i in range(5,n,2):
        if i % 6 == 1 or i % 6 == 5:
            for j in range(2,int((sqrt(i)+1)//1)):#judge whether a number can be divided by some number greater than 1 and smaller than the sqrt of itself with no remainder
                if i % j == 0:
                    break
            else:#for/while - else
                number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn
    
print(PN_X(1000000))