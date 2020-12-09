#Miller_Robin
import time
def Miller_Robin(n):
    t = 0#calculate t and u through loop
    u = n-1
    while u % 2 == 0:
        u = u // 2
        t += 1

    test = [2,3]#testcase, note that it is a necessary condition, but not sufficient one
    index = 0#decide which number for test, here we verify 2 first
    while index in range(len(test)) and len(test) < n:
        a = test[index]
        ans = pow(a,u,n)

#through contiously take the square of ans, we can verrify the necessay condition
        for j in range(t):
            y1 = ans
            y2 = (pow(ans,2))%n
            if y2 == 1 and y1 != 1 and y1 != n-1:
                return False
            else:
                ans = y2

        if ans == 1:#it pass the verification of 2
            index += 1#here we verify 3
        else:
            return False

    else:#while-else reflects that the number n has passed the test 2 and 3
        return True

def PN_X(n):
    time_start = time.time()
    number_pn = 2 #note that we only consider odd number no smaller than 5 here

    for i in range(5,n,2):
        if Miller_Robin(i) == True:
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start,number_pn

print(PN_X(1000000))


#here we test extra: juduging whether a number over 10**9 is prime, since it' s not the main project, the testcase has been commented out
def is_prime(n):
    time_start = time.time()

    p = Miller_Robin(n)

    time_end = time.time()
    return time_end - time_start, p

#print(is_prime(1000000000000037))
#print(is_prime(1000000000000027))