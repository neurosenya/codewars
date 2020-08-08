from math import sqrt
import time
start = time.time()

def list_squared(m, n):
    l = []
    for i in range(m, n+1):
        divsq_sum = sum([j**2 for j in range(1, i+1) if i % j == 0])
        mroot = sqrt(divsq_sum)
        if mroot == int(mroot):
            l.append([i, divsq_sum])
    return l


def list_squared_efficient(m, n):
    l = []
    for num in range(m, n+1):
        sqrt_num = int(sqrt(num)) + 1
        divs = []
        for i in range(1,sqrt_num):
            if num % i == 0 and i*i != num:
                divs.append(i)
                divs.append(int(num/i))
            elif num % i == 0 and i*i == num:
                divs.append(i)
        divsq_sum = sum([j**2 for j in divs])
        divsq_sum_root = sqrt(divsq_sum)
        if divsq_sum_root == int(divsq_sum_root):
            l.append([num, divsq_sum])
    return l


print("\n",list_squared_efficient(1,100000), "\n")
print("-----Execution time %s s ------" % (time.time() - start), "\n")
