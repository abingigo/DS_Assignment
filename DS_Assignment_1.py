#DIsclaimer: This code works in JDoodle, but only on Python 3 and not Python 2

#Function that returns probability of n people having the same birthday in 365 days
import decimal

def prob(n):
    decimal.getcontext().prec = 5000
    if n > 365:
        return 1
    c = 1
    for i in range(0, n):
        a = (365 - i) / 365
        c *= a
    return 1 - c

x = prob(int(input()))
print('%.100f'%x)