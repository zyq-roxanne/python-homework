#4Sieve_of_Eratosthenes
import time

def PN_X(n):
    time_start = time.time()
    number_pn = 0

    is_prime_list = [1] * n#Create a list which contains 0 to n-1
    is_prime_list[0] = 0#0 is not prime
    is_prime_list[1] = 0#1 is not prime
    for i in range(2,n):
        if is_prime_list[i]:
            for x in range(2,(n-1)//i + 1):#最后一步应该是整除向上取整，从而避免了index out of range和最后一个数字无法筛去的问题
                is_prime_list[i*x] = 0

    number_pn = is_prime_list.count(1)
    time_end = time.time()
    return time_end - time_start, number_pn
    
print(PN_X(1000000))