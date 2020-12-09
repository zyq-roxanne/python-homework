#2Optimize_Brute_Force
import time
from math import sqrt

def PN_X(n):
    time_start = time.time()
    number_pn = 0

    for i in range(2,n):
        for j in range(2,int((sqrt(i)+1)//1)):#judge whether a number can be divided by some number greater than 1 and smaller than the sqrt of itself with no remainder
            #print(j)
            if i % j == 0:
                break
        else:#for/while - else
            number_pn += 1
            
    time_end = time.time()
    return time_end - time_start, number_pn
    
print(PN_X(1000000))    